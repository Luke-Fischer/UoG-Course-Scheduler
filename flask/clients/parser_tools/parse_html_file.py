from .data_structs import UniversityCourse
import sys
import re 


# parse_html_file, returns a list of UniversityCourse objects that then need ot be written to the csv.
def parse_html_file(filePointer):
    textFromFile = readFile(filePointer)
    # Compile Regular Expressions
    # Regular expression to find data by field.
    # Regular expressoin for finding a course's credit worth
    regexCredit = re.compile(r"(?<=p id=\"SEC_MIN_CRED_).*(?<=\">)([0-9.]*)", re.IGNORECASE )
    # Regular expressoin for finding a course's Faculty 
    regexFaculty = re.compile(r"(?<=p id=\"SEC_FACULTY_INFO_).*(?<=\">)([a-z\. ]*)", re.IGNORECASE)
    # Regular expressoin for finding a course's Capacity 
    regexCapacity = re.compile(r"(?<=p id=\"LIST_VAR5_).*(?<=\">)([0-9\/ a-z\-]*)", re.IGNORECASE)
    # Regular expressoin for finding a course's Location 
    regexLocation = re.compile(r"(?<=p id=\"SEC_LOCATION_).*(?<=\">)([A-Z \-]*)", re.IGNORECASE)
    # Regular expressoin for finding a course's Academic Level 
    regexAcademicLevel = re.compile(r"(?<=p id=\"SEC_ACAD_LEVEL_).*(?<=\">)([A-Z \-]*)", re.IGNORECASE)
    # Regular expressoin for finding a course's Status 
    regexStatus = re.compile(r"(?<=p id=\"LIST_VAR1_).*(?<=\">)([a-z ]*)", re.IGNORECASE)
    # Regular expressoin for finding a course's Term (Year/semester) 
    regexTerm = re.compile(r"(?<=p id=\"WSS_COURSE_SECTIONS_).*(?<=\">)([a-z 0-9]*)", re.IGNORECASE)
    # Regular expressoin for finding a course's Meeting information 
    regexMeetingInfo = re.compile(r"(?<=name=\"SEC\.MEETING\.INFO_)[0-9]{1,5}\" value=\"(?<=value=\")([0-9\/ \-a-z:,\n]*)", re.IGNORECASE)
    # Regular expression for finding a course's Section title, based on the html structure the quotes and greater than come before the data,
    # which alwayus starts with 3 or 4 capital letters and a star symbol.
    regexSectionTitle = re.compile(r"(?<=\">)([A-Z]{2,4}\*[0-9\/ \*\(\)\-a-z:,\n]*)", re.IGNORECASE)
    # Search for info using regular expressions.
    courseCredits = getDataByField(regexCredit, textFromFile)
    courseFaculty = getDataByField(regexFaculty, textFromFile)
    courseCapacity = getDataByField(regexCapacity, textFromFile)
    courseLocation = getDataByField(regexLocation, textFromFile)
    courseAcademicLevel = getDataByField(regexAcademicLevel, textFromFile)
    courseStatus = getDataByField(regexStatus, textFromFile)
    courseTerm = getDataByField(regexTerm, textFromFile)
    courseMeetingInfo = getDataByField(regexMeetingInfo, textFromFile)
    # remove the start and end dat text from the meeting info.
    courseMeetingInfo = removeStartEndDate(courseMeetingInfo)
    courseSectionTitle = getDataByField(regexSectionTitle, textFromFile)
   
    # Create the List of UniversityCourse objects
    UniversityCourseObjList = createObjList(
            courseTerm, courseStatus, courseSectionTitle, courseLocation, courseMeetingInfo,courseFaculty, courseCapacity, courseCredits, courseAcademicLevel)  
            
    # return the object list
    return UniversityCourseObjList

def readFile(filePointer):
    # read the file contents into memory as plain text
    textFromFile = filePointer.read()
    filePointer.close()
    return(textFromFile)

def getDataByField(regexForField, textFromFile):
    fieldData = re.findall(regexForField ,textFromFile)
    return fieldData

# remove the start-to-end-date from the Section Meeting Info list (courseMeetingInfoList[])
# information on re.sub() from https://flexiple.com/python/python-regex-replace/
def removeStartEndDate(meetingInfoList):
    currElement = 0
    while (currElement < len(meetingInfoList) ):
        #use a regex to do string replacement.
        #regex looks for 4 digits then a forward slash 2 digits a forward slash and an optional dash. It also removes the trailing space.
        #this gets data in the form 1234/56/78-9012/34/56, and replaces it with an empty string to remove the date (yyyy/mm/dd-yyyy/mm/dd)
        meetingInfoList[currElement] = re.sub(r"\d{4}/\d{2}/\d{2}-* *",'',meetingInfoList[currElement])
        currElement = currElement+1

    return meetingInfoList

def createObjList(term,status,title,location,meeting,faculty,capacity,credit,acadLevel):
    currCourse = 0  # loop counter vairable
    numCourses = len(title) # number of courses
    coursesList = [] #list to store the UniversityCourse class objects
    # Order of argument to be passed to __init__
    # term, status, sectionNameTitle, location, meetingInfo,
    # faculty, capacity, creditsWorth, academic Level

    # create all the UniversityCourse class objects.
    while(currCourse < numCourses):
        # keep appending a new class object to the list.
        coursesList.append( UniversityCourse(
            term[currCourse], status[currCourse],
            title[currCourse], location[currCourse],
            meeting[currCourse], faculty[currCourse],
            capacity[currCourse], credit[currCourse],
            acadLevel[currCourse])  )

        currCourse = currCourse+1
    return coursesList
    


