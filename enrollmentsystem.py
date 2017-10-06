import re

def inputStudent(students):
    while True:
        name = input("Input student name: ")
        if not re.match("^[\sA-Za-z]*$", name):
            print("Error: Only characters a-z are allowed")
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
        if(checkStudent(ID,students)):
            print("Error: ID already exists")
            continue
        break

    return createStudent(name,str(ID))

def createStudent(name, ID, grades = {}):
    newStudent = Student(name,ID)
    newStudent.grades = grades
    print("Student Added:")
    print("NAME: " + newStudent.name)
    print("ID: " + str(newStudent.ID)+ "\n")
    return newStudent

def inputCourse(courses):
    while True:
        courseCode = input("Input course code: ")
        if not re.match("^[A-Z0-9-]*$", courseCode):
            print("Error: Course Code must consist of only uppercase letters, numbers and dash")
            continue
        if (len(courseCode)!=7):
            print("Error: Course Code must consist of exactly 7 characters")
            continue
        break
    while True:
        units = input("Input number of units for " + courseCode + ": ")
        if not re.match("^[0-4.5]",units):
            print("Error: Unit's value must be in the range from 0 to 4 (including floating)")
            continue
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

def checkStudent(ID, students):
    for student in students:
        if(student.ID==ID):
            return True
    return False

def getStudent(ID, students):
    for student in students:
        if(student.ID==ID):
            return student
    return null

def checkCourse(courseCode, courses):
    for course in courses:
        if(course.code==courseCode):
            return True
    return False

def getCourse(courseCode, courses):
    for course in courses:
        if(course.code==courseCode):
            return course
    return null

def dropAll(ID, courses):
    for course in courses:
        for student in course.studentsEnrolled:
            if(student.ID==ID):
                print("Dropped student in " + course.code)
                course.studentsEnrolled.remove(student)

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
        choice = int(input("1 - Add Student\n2 - Edit Student Info\n3 - Delete Student\n4 - Add Course\n5 - Edit Course\n6 - Create a course\n7 - Enroll a student in a course\n8 - Drop a student from a course\n9 - Set a student's grade for a course\n10 - View a student's report card:\n"))
        if(choice==1):
            students.append(inputStudent(students))
        elif(choice==2):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                while True:
                    editChoice = int(input("1 - Edit name\n2- Edit ID number:\n"))
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
                        course.editCode()
                        break
                    elif (coursEditChocie == 2):
                        course.editUnits()
                        break
                    else:
                        print("Invalid choice")
            else:
                print("Error: Course does not exist")

        elif(choice==6):
            courses.append(inputCourse())
        elif(choice==7):
            ID = input("Enter the ID number of the student: \n")
            if(checkStudent(ID,students)):
                courseCode = input("Enter the course code: \n")
                if(checkCourse(courseCode,courses)):
                    course = getCourse(courseCode,courses)
                    student = getStudent(ID,students)
                    course.enrollStudent(student)
                    print("Student enrolled: ")
                    print("NAME: " + student.name)
                    print("ID: " + student.ID)
                    print("COURSE: " + course.code)
                    print("UNITS: " + course.units)
                else:
                    print("Error: Course does not exist")
            else:
                print("Error: ID number does not exist")

        elif(choice==8):
            ID = input("Enter the ID number of the student: \n")
            if(checkStudent(ID,students)):
                courseCode = input("Enter the course code: \n")
                if(checkCourse(courseCode,courses)):
                    course = getCourse(courseCode,courses)
                    student = getStudent(ID,students)
                    course.dropStudent(student)
                else:
                    print("Error: Course does not exist")
            else:
                print("Error: ID Number does not exist")

        elif(choice==9):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                courseCode = input("Enter the course code:\n")
                if(checkCourse(courseCode, courses)):
                    course = getCourse(courseCode,courses)
                    student = getStudent(ID,students)
                    grade = float(input("Enter the grade of the student:\n"))
                    student.insertGrade(courseCode,grade)
                else:
                    print("Error: Course does not exist")
            else:
                print("Error: ID number does not exist")

        elif(choice==10):
            ID = input("Enter the ID number of the student:\n")
            if(checkStudent(ID,students)):
                student = getStudent(ID,students)
                print(student.grades)
            else:
                print("Error: ID number does not exist")

        elif(choice==11):
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


if __name__== "__main__":
  main()


'''
1. View All Students Enrolled
2. View Top 5 Students
3. Fix the incrementation of grades
4. Drop a student in a course
5. Fix duplicate entries of ID
'''
