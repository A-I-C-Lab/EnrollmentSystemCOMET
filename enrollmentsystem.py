import re

def inputStudent():
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
        break

    return createStudent(name,str(ID))
        
    
def createStudent(name, ID, grades = {}):
    newStudent = Student(name,ID)
    newStudent.grades = grades
    print("Student Added:")
    print("NAME: " + newStudent.name)
    print("ID: " + str(newStudent.ID)+ "\n")
    return newStudent

def inputCourse():
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
        break
    return createCourse(courseCode,units)

def createCourse(courseCode, units):
    newCourse = Course(courseCode,units)
    print("Course created:")
    print("COURSECODE: " + newCourse.code)
    print("UNITS: " + str(newCourse.units) + "\n")
    return newCourse

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

    def insertGrade(self,code,grade):
        newGrade = {code:grade}
        self.grades = newGrade

    def editGrade(self,code,grade):
        self.grades[code] = grade

    def removeGrade(self, code):
        del self.grades[code]
        

        
class Course:
    code = "" # 7 characters(Capital Letters, Numbers, Dash)
    units = 0.0 # floating, 0 to 4
    
    def __init__(self,code,units):
        self.code = code
        self.units = units
        
    def editCode(self,code):
        self.code = code

    def editUnits(self,units):
        self.units = units

def main():
    students = []
    courses = []
    while(True):
        choice = int(input("1 - Add Student\n2 - Edit Student Info\n3 - Delete Student\n4 - Add Course\n5 - Edit Course\n6 - Create a course\n7 - Enroll a student in a course\n8 - Drop a student from a course\n9 - Set a student's grade for a course\n10 - View a student's report card:\n"))
        if(choice==1):
            students.append(inputStudent())
        elif(choice==2):
            ID = input("Enter the ID number of the student:\n")
            for student in students:
                if (student.ID==ID):
                    while True:
                        editChoice = int(input("1 - Edit name\n2- Edit ID number:\n"))
                        if (editChoice==1):
                            student.editName()
                            break
                        elif(editChoice==2):
                            student.editID()
                            break
                        else: print("Invalid")
                        
        elif(choice==3):
            name = input("Enter the name of the student:\n")
            for student in students:
                if(student.name==name):
                    student[student].remove() ##CHECK IF WORKING
                    
        elif(choice==4):
            newCourse = inputCourse()
            courses.append(newCourse)
            
        elif(choice==5):
            courseCode = input("Enter the Course Code:\n")
            for course in courses:
                if (course.code==courseCode):
                    while True:
                        courseEditChoice = int(input("1 - Edit Course Code\n2 - Edit Units:\n"))
                        if(courseEditChoice==1):
                            course.editCode()
                            break
                        elif(coursEditChocie==2):
                            course.editUnits()
                            break
                        else: print("Invalid choice")
            
        elif(choice==6):
            courses.append(inputCourse())
        elif(choice==7):
            pass
            #enroll
        elif(choice==8):
            pass
            #drop
        elif(choice==9):
            ID = input("Enter the ID number of the student:\n")
            courseCode = input("Enter the course code:\n")
            grade = float(input("Enter the grade of the student:\n"))
            for student in students:
                if (student.ID == ID):
                    student.insertGrade(courseCode,grade)
                    break

        elif(choice==10):
            ID = input("Enter the ID number of the student:\n")
            for student in students:
                if(student.ID == ID):
                    print(student.grades)

if __name__== "__main__":
  main()





