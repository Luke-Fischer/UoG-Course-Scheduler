import psycopg2
from psycopg2 import OperationalError
from datetime import datetime, date

DATABASE = "course_scheduler"
USER = "postgres"
PASSWORD = "group_301-!"
HOST = "course-scheduler-data.csez3smecwky.us-east-2.rds.amazonaws.com"
PORT = 5432

class SQLClient:
    def __init__(self):
        try:
            self.db = psycopg2.connect(
                database="course_scheduler",
                user="postgres",
                password="group_301-!",
                host="course-scheduler-data.csez3smecwky.us-east-2.rds.amazonaws.com",
                port=5432,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print("Error occurred in connecting to the DB")

    def drop_tables(self):
        drop_script =   '''
                        DROP TABLE IF EXISTS course_additional_information;
                        DROP TABLE IF EXISTS course_meetings;
                        DROP TABLE IF EXISTS course_names;
                        DROP TABLE IF EXISTS course_section_availability;
                        DROP TABLE IF EXISTS course_section_instructors;
                        DROP TABLE IF EXISTS course_sections;
                        DROP TABLE IF EXISTS course_term;
                        '''
        try:
            with self.db.cursor() as curs:
                curs.execute(drop_script)
                print("Dropped Tables: SUCCESS")
            self.db.commit()
        except OperationalError as e:
            print("Error in dropping tables: "'{e}')

    def create_tables(self):
        create_script = '''
                        CREATE TABLE IF NOT EXISTS course_names (
                            course_id integer,
                            course_code varchar(50),
                            course_name varchar(50)
                        );

                        CREATE TABLE IF NOT EXISTS course_sections (
                            course_id integer,
                            course_section varchar(50)
                        );

                        CREATE TABLE IF NOT EXISTS course_meetings (
                            course_id integer,
                            course_section varchar(50),
                            meeting_type varchar(50),
                            meeting_start_time varchar(50),
                            meeting_end_time varchar(50),
                            meeting_building varchar(50),
                            meeting_room_num integer,
                            meeting_day varchar(50)
                        );

                        CREATE TABLE IF NOT EXISTS course_section_instructors (
                            course_id integer,
                            course_section varchar(50),
                            course_section_instructor varchar(50)
                        );

                        CREATE TABLE IF NOT EXISTS course_term (
                            course_id integer,
                            course_year integer,
                            course_semester varchar(50)
                        );

                        CREATE TABLE IF NOT EXISTS course_section_availability (
                            course_id integer,
                            course_section varchar(50),
                            course_section_remaining_capacity integer,
                            course_section_total_capacity integer,
                            course_section_status varchar(50)

                        );

                        CREATE TABLE IF NOT EXISTS course_additional_information (
                            course_id integer,
                            course_location varchar(50),
                            course_credits decimal,
                            course_academic_level varchar(50)
                        );'''
        try:
            with self.db.cursor() as curs:
                curs.execute(create_script)
                print("Create Tables: SUCCESS")
            self.db.commit()
        except OperationalError as e:
            print("Error in creating tables: "'{e}')

    def get_all_courses(self):
        count = 0
        returnString = "["
        prevCode = ""
        prevSection = ""
        num = 0
        with self.db.cursor() as curs:
            curs.execute("select course_names.course_code, course_names.course_name, course_sections.course_section, course_section_instructors.course_section_instructor, course_term.course_year, course_term.course_semester, course_section_availability.course_section_remaining_capacity, course_section_availability.course_section_total_capacity, course_section_availability.course_section_status, course_additional_information.course_location, course_additional_information.course_credits, course_additional_information.course_academic_level, course_meetings.meeting_building, course_meetings.meeting_room_num, course_meetings.meeting_type, course_meetings.meeting_day, course_meetings.meeting_start_time, course_meetings.meeting_end_time FROM ((((((course_names INNER JOIN course_sections ON course_names.course_id = course_sections.course_id) INNER JOIN course_meetings ON course_names.course_id = course_meetings.course_id) INNER JOIN course_section_instructors ON course_names.course_id = course_section_instructors.course_id) INNER JOIN course_term ON course_names.course_id = course_term.course_id) INNER JOIN course_section_availability ON course_names.course_id = course_section_availability.course_id) INNER JOIN course_additional_information ON course_names.course_id = course_additional_information.course_id)")
            output = curs.fetchall()
            for row in output:
                code = str(row[0])
                section = str(row[2])
                
                #New section
                if ((section != prevSection) or (code != prevCode)) :
                    num = num + 1
                    if (count != 0):
                        returnString += "], "
                    count = 1
                    prevCode = code
                    prevSection = section
                    returnString += ('["%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[14], row[12], row[13], row[15], row[16], row[17]))
                else:
                    returnString += (', "%s", "%s", "%s", "%s", "%s", "%s"' % (row[14], row[12], row[13], row[15], row[16], row[17]))
                
            curs.close()
            returnString += "]]"
            return str(returnString)

    def close(self):
        self.db.close()

