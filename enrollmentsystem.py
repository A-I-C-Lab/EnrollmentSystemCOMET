import re

def inputStudent(students):
    while True:
        name = input("Input student name: ")
        if not re.match("^[\sA-Za-z]*$", name):
            print("Error: Only letters are allowed")
            continue
        break
    while True:
        try:
            ID = int(input("Input student ID: "))
        except ValueError:
            print("Error: Only numbers are allowed")
            continue
        if(len(str(ID))!= 8):
            print("ID Number must contain exactly 8 numbers")
            continue
        ID = str(ID)
        if(checkStudent(ID,students)):
            print("Error: ID already exists")
            continue
        break
    return createStudent(name,ID)

def createStudent(name, ID, grades = {}):
    newStudent = Student(name,ID)
    newStudent.grades = grades
    print("Student Added:")
    print("NAME: " + newStudent.name)
    print("ID: " + newStudent.ID + "\n")
    return newStudent

def checkUnits(units):
    i = 0.0
    while (i<=4.0):
        if (units==i):
            return True
        i = i+0.5
    return False

def inputCourse(courses):
    while True:
        courseCode = input("Input course code: ")
        if not re.match("^[A-Z0-9-]*$", courseCode):
            print("Error: Course Code must consist of only uppercase letters, numbers and dash")
            continue
        if (len(courseCode)!=7):
            print("Error: Course Code must consist of exactly 7 characters")
            continue
        if(checkCourse(courseCode,courses)):
            print("Error: Course already exists")
            continue
        break
    while True:
        units = input("Input number of units for " + courseCode + ": ")
        if not re.match("^[0-4.5]",units):
            print("Error: Unit's value must be in the range from 0 to 4 (including floating)")
            continue
        units = float(units)
        if not checkUnits(units):
            print("Error: Unit's value must be 0 to 4 units only (in increments of 5)")
            continue
        else:
            for course in courses:
                if (course.code==courseCode):
                    print("Error: Course already exists")
                    continue
            break
    return createCourse(courseCode,units)

def createCourse(courseCode, units):
    newCourse = Course(courseCode,units)
    print("Course created:")
    print("COURSECODE: " + newCourse.code)
    print("UNITS: " + str(newCourse.units) + "\n")
    return newCourse

def inputCourse2(courses):
    while True:
        courseCode = input("Input course code: ")
        if not re.match("^[A-Z0-9-]*$", courseCode):
            print("Error: Course Code must consist of only uppercase letters, numbers and dash")
            continue
        if (len(courseCode)!=7):
            print("Error: Course Code must consist of exactly 7 characters")
            continue
        if(checkCourse(courseCode,courses)):
            print("Error: Course already exists")
            continue
        return courseCode

def checkStudent(ID, students):
    for student in students:
        if(student.ID==ID):
            return True
    return False

def checkEnrolled(ID, course):
    print("check enrolled")
    for student in course.studentsEnrolled:
        if (student.ID == ID):
            print("ahh")
            return True
    print("false")
    return False


def getStudent(ID, students):
    for student in students:
        if(student.ID==ID):
            return student
    return None

def checkCourse(courseCode, courses):
    for course in courses:
        if(course.code==courseCode):
            return True
    return False

def getCourse(courseCode, courses):
    for course in courses:
        if(course.code==courseCode):
            return course
    return None

def dropAll(ID, courses):
    for course in courses:
        for student in course.studentsEnrolled:
            if(student.ID==ID):
                print("Dropped student in " + course.code)
                course.studentsEnrolled.remove(student)



def viewAllStudents(students):
    for student in students:
        print("NAME: " + student.name)
        print("ID: " + student.ID)
        print(student.grades)
        print("\n\n")

class Student:
    name = ""
    ID = "0"
    grades = {}

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def editName(self):
        while True:
            name = input("Input student name: ")
            if not re.match("^[\sA-Za-z]*$", name):
                print("Error: Only characters a-z are allowed")
                continue
            break
        self.name = name
        print("Student Info Updated:")
        print("NAME: " + self.name)
        print("ID: " + self.ID)

    def editID(self):
        while True:
            try:
                ID = int(input("Input student ID: "))
            except ValueError:
                print("Error: Only numbers are allowed")
                continue
            if(len(str(ID))!= 8):
                print("ID Number must contain exactly 8 numbers")
                continue
            break
        self.ID = str(ID)   
        print("Student Info Updated:")
        print("NAME: " + self.name)
        print("ID: " + self.ID)

    def enrollStudent(self,code,grade):
        newGrade = {code:grade}
        self.grades = newGrade

    def editGrade(self,code,grade):
        self.grades[code] = grade

    def removeGrade(self, code):
        del self.grades[code]

        
class Course:
    code = "" # 7 characters(Capital Letters, Numbers, Dash)
    units = 0.0 # floating, 0 to 4
    studentsEnrolled = [];
    
    def __init__(self,code,units):
        self.code = code
        self.units = units
        
    def editCode(self,code):
        self.code = code

    def editUnits(self,units):
        self.units = units

    def enrollStudent(self, student):
        self.studentsEnrolled.append(student)

    def dropStudent(self, student):
        for student2 in self.studentsEnrolled:
            if (student2.ID==student.ID):
                self.studentsEnrolled.remove(student2)
                print("Successfully dropped. ")
            else:
                print("Student not found. ")
                break

def main():
    students = []
    courses = []

    while(True):
        try:
            choice = int(input("1 - Add Student\n2 - Edit Student Info\n3 - Delete Student\n4 - Add Course\n5 - Edit Course\n6 - Enroll a student in a course\n7 - Drop a student from a course\n8 - Set a student's grade for a course\n9 - View a student's report card:\n10 - View all students in a course\n11 - View all students\n"))
        except ValueError:
            print("Error: Invalid input")
            continue
        if(choice==1):
            students.append(inputStudent(students))
        elif(choice==2):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                while True:
                    editChoice = int(input("1 - Edit name\n2- Edit ID number:\n"))
                    student = getStudent(ID,students)
                    if (editChoice == 1):
                        student.editName()
                        break
                    elif (editChoice == 2):
                        student.editID()
                        break
                    else:
                        print("Invalid")
            else:
                print("Error: ID number does not exist")
                        
        elif(choice==3):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                student = getStudent(ID,students)
                print("Student removed:")
                print("NAME: " + student.name)
                print("ID: " + str(student.ID))
                dropAll(ID,courses)
                students.remove(student)  ##CHECK IF WORKING
            else:
                print("Error: ID number does not exist")
                    
        elif(choice==4):
            newCourse = inputCourse(courses)
            courses.append(newCourse)
            
        elif(choice==5):
            courseCode = input("Enter the Course Code:\n")
            if(checkCourse(courseCode,courses)):
                while True:
                    courseEditChoice = int(input("1 - Edit Course Code\n2 - Edit Units:\n"))
                    course = getCourse(courseCode,courses)
                    if (courseEditChoice == 1):
                        course.editCode(inputCourse2(courses))
                        break
                    elif (courseEditChoice == 2):
                        course.editUnits()
                        break
                    else:
                        print("Invalid choice")
            else:
                print("Error: Course does not exist")

        elif(choice==6):
            ID = input("Enter the ID number of the student: \n")
            if(checkStudent(ID,students)):
                student = getStudent(ID, students)
                courseCode = input("Enter the course code: \n")
                if(checkCourse(courseCode,courses)):
                    course = getCourse(courseCode,courses)
                    if (checkEnrolled(str(ID), course)):
                        print("ERROR: Student is already enrolled in the course")
                    else:
                        course.enrollStudent(student)
                        print("Student enrolled: ")
                        print("NAME: " + student.name)
                        print("ID: " + student.ID)
                        print("COURSE: " + course.code)
                        print("UNITS: " + str(course.units))
                else:
                    print("Error: Course does not exist")
            else:
                print("Error: ID number does not exist")

        elif(choice==7):
            ID = input("Enter the ID number of the student: \n")
            if(checkStudent(ID,students)):
                courseCode = input("Enter the course code: \n")
                if(checkCourse(courseCode,courses)):
                    course = getCourse(courseCode,courses)
                    if(checkEnrolled(ID,course)):
                        course = getCourse(courseCode,courses)
                        student = getStudent(ID,students)
                        course.dropStudent(student)
                    else:
                        print("Error: Student is not enrolled in class")
                else:
                    print("Error: Course does not exist")
            else:
                print("Error: ID Number does not exist")

        elif(choice==8):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                courseCode = input("Enter the course code:\n")
                if(checkCourse(courseCode, courses)):
                    course = getCourse(courseCode,courses)
                    if(checkEnrolled(ID,course)):
                        student = getStudent(ID,students)
                        grade = float(input("Enter the grade of the student:\n"))
                        while True:
                            if (checkUnits(grade)):
                                student.editGrade(courseCode,grade)
                                break
                            else:
                                print("Error: Invalid grade")
                    else:
                        print("Error: Student is not enrolled in course")
                else:
                    print("Error: Course does not exist")
            else:
                print("Error: ID number does not exist")

        elif(choice==9):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                student = getStudent(ID,students)
                print(student.grades)
            else:
                print("Error: ID number does not exist")

        elif(choice==10):
            courseCode = input("Enter the course code: ")
            if(checkCourse(courseCode,courses)):
                course = getCourse(courseCode, courses)
                i = 1
                for student in course.studentsEnrolled:
                    print("Student #" + str(i))
                    print("NAME: " + student.name)
                    print("ID: " + student.ID)
                    i += 1
            else:
                print("Error: Course does not exist")
        elif(choice==11):
            viewAllStudents(students)


if __name__== "__main__":
  main()


'''
1. View Top 5 Students
2. More error checking
'''
