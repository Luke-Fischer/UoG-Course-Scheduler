

class UniversityCourse:
    # An individual course listed on webadvisor
    # each field is a string (use explicit types so capacity isn't converted.

    def __init__(self, term, status, sectionNameTitle, location, meetingInfo, faculty, capacity, creditsWorth, acadLevel):
        #Initialize the values in the class objects.
        self.term = term
        self.status = status
        self.sectionNameTitle = sectionNameTitle
        self.location = location
        self.meetingInfo = meetingInfo
        self.faculty = faculty
        # Test for a null capacity, before trying to split the string.
        if ("" == capacity):
            self.capacityRemaining = ""
            self.capacityTotal = ""
        else:
            self.capacityRemaining = capacity.strip().split('/')[0]
            self.capacityTotal = capacity.strip().split('/')[1]
        self.creditsWorth = creditsWorth
        self.acadLevel = acadLevel

        # Standardized indexes used for accessing data columns
        self.COURSE_INDEX_MAPPING = {
            1: self.term,
            2: self.status,
            3: self.sectionNameTitle,
            4: self.location,
            5: self.meetingInfo,
            6: self.faculty,
            7: self.capacityRemaining,
            8: self.capacityTotal,
            9: self.creditsWorth,
            10: self.acadLevel
        }

    def printClass(uniCourse):
        print(uniCourse.term)
        print(uniCourse.status)
        print(uniCourse.sectionNameTitle)
        print(uniCourse.location)
        print(uniCourse.meetingInfo)
        print(uniCourse.faculty)
        print(uniCourse.capacityRemaining,'/', uniCourse.capacityTotal)
        print(uniCourse.creditsWorth)
        print(uniCourse.acadLevel)

    def __str__(self):
        out_str = f"""Term:           {self.term}
Status:         {self.status}
Section Title:  {self.sectionNameTitle}
Location:       {self.location}
Meeting Info:   {self.meetingInfo}
Faculty:        {self.faculty}
Capacity:       {self.capacityRemaining} / {self.capacityTotal}
Credits Worth:  {self.creditsWorth}
Academic Level: {self.acadLevel}"""

        return out_str

    # Inputs a column index and returns its value
    def get_value_from_column_index(self, index : int):
        return str(self.COURSE_INDEX_MAPPING[index])

    def get_all_string_values(self):
        return [
            str(self.term),
            str(self.status),
            str(self.sectionNameTitle),
            str(self.location),
            str(self.meetingInfo),
            str(self.faculty),
            str(self.capacityRemaining),
            str(self.capacityTotal),
            str(self.creditsWorth),
            str(self.acadLevel)
        ]