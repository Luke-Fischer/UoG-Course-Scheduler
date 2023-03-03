import csv
from .data_structs import UniversityCourse

#prints out list of courses
def print_courses_list(coursesList):
    for i in range (0, len(coursesList)):
        coursesList[i].printClass()


#reads in a csv file
def read_csv(filename):
    print("Reading CSV...")

    #open csv file
    with open(filename) as csvFile:

        #setup reader
        csvReader = csv.reader(csvFile, delimiter = ',')
        lineCount = 0
        coursesList = []

        #loop through rows in csv
        for row in csvReader:

            #Don't read in headers to list
            if lineCount > 0:
                #add course info to list of courses
                coursesList.append(UniversityCourse(*row))
            
            lineCount += 1

        print(f"Read through {lineCount-1} courses")

        print_courses_list(coursesList)
        
        return coursesList
