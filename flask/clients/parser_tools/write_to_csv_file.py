from .data_structs import UniversityCourse

#Writes the list of courses to memory
def write_to_csv(coursesList, filename):
    print("Writing CSV...")
    
    #open csv file
    csv_file = open(filename, 'w')

    #write headers to file
    csv_file.write("Term,Status,Section Name and Title,Location,Meeting Information,Faculty,Availablity/Capacity,Credits,Academic Level\n")

    for i in range(0, len(coursesList)):
        #write course as string to file
        csv_row_string = course_to_string(coursesList[i])
        csv_file.write(csv_row_string)

        #add newline if not final course
        if i < len(coursesList) -1:
            csv_file.write('\n')

    #close file
    csv_file.close()

#returns the course as a comma delimited string
def course_to_string(university_course):
    def helper(input):
        return str(input).replace(",", ";").replace("\n", "")

    course = helper(university_course.term) + ","
    course += helper(university_course.status) + ","
    course += helper(university_course.sectionNameTitle) + ","
    course += helper(university_course.location) + ","
    course += helper(university_course.meetingInfo) + ","
    course += helper(university_course.faculty) + ","
    course += helper(university_course.capacityRemaining) + " / "
    course += helper(university_course.capacityTotal) + ","
    course += helper(university_course.creditsWorth) + ","
    course += helper(university_course.acadLevel)

    return course





