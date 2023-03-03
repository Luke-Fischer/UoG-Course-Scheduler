import os
import copy
import json

import pandas as pd
import pyparsing as pp
from datetime import datetime, date

#from sql_client import SQLClient
from clients.sql_client import SQLClient
from clients.parser_tools.parse_html_file import parse_html_file
from clients.parser_tools.write_to_csv_file import write_to_csv


ROOM_LIST = ["AC", "ALEX", "ANCC", "ANNU", "ARB", "BMED", "CCLC", "CRB", "CRLM", "CRSC", "CSB", "DAIR", "DH", "ECBA",
    "ESRC", "FEDB", "FS", "FVMI", "GFTC", "GRC", "GRHM", "GTI", "HUTT", "JASAC", "JH", "JTP", "LA", "LENN", "LLC",
    "MAC", "MACN", "MACS", "MAH", "MASS", "MCKN", "MCLN", "MINS", "OVCM", "PAHL", "REYN", "RICH", "ROZH", "SB", 
    "SRES", "SSC", "THRN", "UC", "WMEM", "ZAV"]

# Data Instance Format:
# 1) term: String
# 2) status: String ["Open" or "Closed"]
# 3) section:
#   i)   full: full string
#   ii)  course: String "ACCT*1220"
#   iii) section_num: String "7760"
#   iv)  course_name: String "Intro to Finance I"
# 4) location: String
# 5) meeting: {"lectures": ..., "labs": ..., "exams": ...}
#   i)   lec: list or tuplet (begin_time, end_time, day_of_week)
#   ii)  labs: list or tuplet (begin_time, end_time, day_of_week)
#   iii) exam: list or tuplet (begin_time, end_time, date)
#      note: exams last entry is the exact date, not the day of week
# 5) meeting_info: String
# 6) faculty: String
# 7) spots: {"availability" : int, "capacity": int}
# 9) credits: String
#10) academic_level: String

class DataParser():
    data : dict

    def __init__(self, path : str):
        load_from = path.split(".")[-1]

        assert load_from in ["json", "csv", "html"]
        
        if load_from == "html":
            with open(path, "r") as fp:
                UniversityObjList = parse_html_file(fp)
                csv_file_name = path.replace(".html", ".csv").split("/")[-1]
                write_to_csv(UniversityObjList, csv_file_name)

            self.parse_csv(csv_file_name)

        elif load_from == "csv":
            self.parse_csv(path)
        else: #json
            self.load_from_json(path)

    def dump_to_db(self, sql_client : SQLClient):
        if sql_client is None:
            sql_client = SQLClient()

        fn_list = (
            self._db_course_additional_information,
            self._db_course_meetings,
            self._db_course_names ,
            self._db_course_section_availability ,
            self._db_course_section_instructors ,
            self._db_course_sections ,
            self._db_course_term, 
        )

        for id, row in enumerate(self.data):
            for fn in fn_list:
                function_list = fn(id, row)

                for (str_out, inserts) in function_list:
                    with sql_client.db.cursor() as curs:
                        curs.execute(str_out, inserts)
                        curs.close()

        sql_client.db.commit()

        print("SQL Upload Success...")
  
    def _db_course_additional_information(self, id, row):
        str_out = "INSERT INTO course_additional_information VALUES (%s, %s, %s, %s);"

        ins_out = (id, row['location'], row['credits'], row['academic_level'])

        return [(str_out, ins_out)]

    def _db_course_meetings(self, id, row):

        list_out = []

        for time_info in row["meeting"]["lec"]:
            str_out = "INSERT INTO course_meetings VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            ins_out = (id, row['section']['section_num'], "lec", time_info[0], time_info[1], time_info[3], time_info[4], time_info[2])
            list_out.append((str_out, ins_out))

        for time_info in row["meeting"]["lab"]:
            str_out = "INSERT INTO course_meetings VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            ins_out = (id, row['section']['section_num'], "lab", time_info[0], time_info[1], time_info[3], time_info[4], time_info[2])
            list_out.append((str_out, ins_out))

        for time_info in row["meeting"]["exam"]:
            str_out = "INSERT INTO course_meetings VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            ins_out = (id, row['section']['section_num'], "exam", time_info[0], time_info[1], time_info[3], time_info[4], time_info[2])
            list_out.append((str_out, ins_out))

        return list_out

    def _db_course_names(self, id, row):
        str_out = "INSERT INTO course_names VALUES (%s, %s, %s);"

        ins_out = (id, row['section']['course'], row['section']['course_name'])

        return [(str_out, ins_out)]

    def _db_course_section_availability(self, id, row):
        str_out = "INSERT INTO course_section_availability VALUES (%s, %s, %s, %s, %s);"

        ins_out = (id, row['section']['section_num'], row['spots']['availability'], row['spots']['capacity'], "closed" if row['spots']['availability'] == 0 else "open")

        return [(str_out, ins_out)]

    def _db_course_section_instructors(self, id, row):
        str_out = "INSERT INTO course_section_instructors VALUES (%s, %s, %s);"

        ins_out = (id, row['section']['section_num'], row['faculty'])

        return [(str_out, ins_out)]

    def _db_course_sections(self, id, row):
        str_out = "INSERT INTO course_sections VALUES (%s, %s);"

        ins_out = (id, row['section']['section_num'])

        return [(str_out, ins_out)]

    def _db_course_term(self, id, row):
        str_out = "INSERT INTO course_term VALUES (%s, %s, %s);"

        info = row['term'].split(" ")

        ins_out = (id, info[1], info[0])

        return [(str_out, ins_out)]

    def load_from_json(self, path : str):
        with open(path) as json_file:
            self.data = json.load(json_file)

        for course in self.data:
            meeting = course["meeting"]
            for lec in meeting["lec"]:
                lec[0] = datetime.fromisoformat(lec[0])
                lec[1] = datetime.fromisoformat(lec[1])
            for lab in meeting["lab"]:
                lab[0] = datetime.fromisoformat(lab[0])
                lab[1] = datetime.fromisoformat(lab[1])
            for exam in meeting["exam"]:
                exam[0] = datetime.fromisoformat(exam[0])
                exam[1] = datetime.fromisoformat(exam[1])

        print(f"Loaded successfully from {path}")

    def push_to_database(self, sql_client : SQLClient):
        pass

    def save_to_json(self, path : str):
        with open(path, "w") as fp:
            json.dump(self.data, fp, default=json_serial)

    def parse_csv(self, path : str):
        if not os.path.isfile(path):
            raise Exception(f"Invalid file path: {path}")

        df = pd.read_csv(path)
        df = df.reset_index()

        self.data = list()

        for index, row in df.iterrows():
            out = {}

            # Easy ones:
            out["term"] = row["Term"]
            out["status"] = row["Status"]
            out["location"] = row["Location"]
            out["faculty"] = row["Faculty"]
            out["credits"] = row["Credits"]
            out["academic_level"] = row["Academic Level"]

            # spots: availability and capacity
            out["spots"] = self.__parse_spots(row["Availablity/Capacity"])

            # section
            out["section"] = self.__parse_section(row["Section Name and Title"])

            # meeting
            out["meeting"] = self.__parse_meeting(row["Meeting Information"])

            self.data.append(out)

        print(out)

    def __parse_meeting(self, parse : str) -> dict:
        out = dict()
        out["lec"] = list()
        out["lab"] = list()
        out["exam"] = list()

        if pd.isnull(parse):
            return out

        types = ["LEC", "LAB", "EXAM", "SEM"]

        for type in types:
            parse = parse.replace(type, " " + type + " ")

        any_header = (pp.Literal("LEC") | pp.Literal("LAB") | pp.Literal("EXAM") | pp.Literal("SEM"))
        
        # Wow a context free grammar. Who knew these nerds weren't kidding that they were useful?
        expr = pp.Forward()
        expr << (pp.StringStart() ^ any_header) + ... +  pp.FollowedBy(any_header ^ pp.StringEnd()) + (expr ^ pp.StringEnd())

        parsed = expr.parse_string(parse)

        while len(parsed) != 0:
            head = parsed[0].strip()
            if head in types and len(parsed) > 1:
                out = self.__parse_date_times(dict_obj = out, type = head, date = parsed[1])

            parsed.pop(0)

        # Finding Rooms:
        rooms_ordered, numbers_ordered = self.__return_ordered_rooms(parse)

        while len(rooms_ordered) < 3:
            rooms_ordered.append("")

        while len(numbers_ordered) < 3:
            numbers_ordered.append(0)

        for i, (room, num) in enumerate(zip(rooms_ordered, numbers_ordered)):
            if i == 0:
                for example in out['lec']:
                    example.append(room) 
                    example.append(num) 
            elif i == 1:
                for example in out['lab']:
                    example.append(room) 
                    example.append(num) 
            elif i == 2:
                for example in out['exam']:
                    example.append(room) 
                    example.append(num) 
            else:
                break

        return out

    def __return_ordered_rooms(self, parse : str) -> list():
        tuple_list = list()

        parse = parse.replace(";", "  ")
        parse = " " + parse + " "

        for room in ROOM_LIST:
            try:
                idx = parse.index(" " + room + " ")
                tuple_list.append((idx, room))
            except ValueError:
                continue

        sorted_room_list = sorted(tuple_list, key=lambda tup: tup[0])
        sorted_rooms = [room_t[1] for room_t in sorted_room_list]

        sorted_nums = []

        parse_split = parse.split()
        for i, room in enumerate(sorted_rooms):
            room_idx = parse_split.index(room)

            room_number = parse_split[room_idx + 1]

            if room_idx < 0 or room_idx >= len(parse_split) - 1:
                sorted_nums.append(0)
                continue

            if room_number.upper() == "ROOM":
                room_number = parse_split[room_idx + 2]

            if room_number.isdigit():
                sorted_nums.append(int(room_number))
            else:
                sorted_nums.append(0)

        return sorted_rooms, sorted_nums

    def __parse_date_times(self, dict_obj, type : str , date : str):
        out = copy.deepcopy(dict_obj)

        type = type.lower()
        type = "lab" if type == "sem" else type

        parser = pp.Combine(pp.Word(pp.nums) + ":" + pp.Word(pp.nums) + (pp.Literal("AM") ^ pp.Literal("PM")))

        start_time = None
        end_time = None

        for index, (tokens, start, end) in enumerate(parser.scan_string(date)):
            my_date = datetime.strptime(tokens[0], "%I:%M%p")

            if index == 0:
                start_time = my_date
            elif index == 1:
                end_time = my_date
            else:
                break

        days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]

        for day in days:
            if day in date:
                out[type].append( [start_time, end_time, day] )

        return out

    def __parse_spots(self, parse : str) -> dict:
        out = dict()

        parse = parse.replace(" ", "")

        if parse == "":
            out["availability"] = 0
            out["capacity"] = 0
            return out

        split = parse.split("/")

        if split[0] == "":
            out["availability"] = 0
        else:
            out["availability"] = int(split[0])

        if split[1] == "":
            out["capacity"] = 0
        else:
            out["capacity"] = int(split[1])

        return out
        
    def __parse_section(self, parse : str) -> dict:
        out = dict()

        out["full"] = parse

        # EX: ACCT*1220*0101 (6573) Intro Financial Accounting
        parser = pp.Word(pp.alphas) + "*" + pp.Word(pp.nums) + "*" + \
            pp.Word(pp.nums + pp.alphas) + "(" +  pp.Word(pp.nums) + ")" + pp.Word(pp.alphas + " " + pp.nums)

        parsed = parser.parse_string(out["full"])

        out["course"] = parsed[0] + parsed[1] + parsed[2]
        out["section_num"] = parsed[4]
        out["course_name"] = parsed[-1]

        return out
    
    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

if __name__ == "__main__":
    dp = DataParser("/home/nvinden/School/CIS3760/flask/data/only_cis.json")
    dp.save_to_json("/home/nvinden/School/CIS3760/flask/data/only_cis.json")

    print("test")

    #sql = SQLClient()
    #sql.drop_tables()
    #sql.create_tables()

    #dp.dump_to_db(sql)