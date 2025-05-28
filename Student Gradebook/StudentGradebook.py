
import json
from studentCl import Student
try:
    with open("student.json", "r") as st:
        currSt= json.load(st)
    if isinstance(currSt,dict):
        currSt=[currSt]
except (FileNotFoundError,json.JSONDecodeError):
    currSt=[]
    with open("student.json", "w") as st:
        json.dump(currSt,st,indent=4)

def menu():
    print("Welcome to Student Grade Book")
    print("---------------------------------\n")
    print("1.Add Student")
    print("2.View Student")
    print("3.Update marks")
    print("4.Calculate average grade")
    print("5.Exit\n")

while True:
    menu()
    choice=int(input("Enter your choice: "))

    if choice==1:
        name=input("Enter student name: ").lower()
        id=int(input("Enter student id: "))
        gradeList = []
        while True:
            subject = input("Enter subject: ").lower()
            grade = input("Enter grade: ")
            done = input("Are you done? (y/n): ")
            subject_dict={
                "subject":subject,
                "grade":grade
            }
            gradeList.append(subject_dict)
            if done == "y":
                break


        newStudent=Student(name,id,grade=gradeList)
        student_dict={
            "name":newStudent.name,
            "id":newStudent.id,
            "grade": newStudent.grade
        }

        currSt.append(student_dict)

        with open("student.json", "w") as st:
            json.dump(currSt,st,indent=4)

        print("Student added\n")

    elif choice==2:
        with open("student.json", "r") as st:
            currSt= json.load(st)

        if not currSt:
            print("No students\n")
        else:
            print(str(currSt) + "\n")

    elif choice==3:
        id=int(input("Enter student id: "))
        subject=input("Enter subject: ").lower()
        grade=input("Enter new grade: ")

        for student in currSt:
            if "id" in student and student["id"]==id:
                for st_grade in student["grade"]:
                    if st_grade["subject"]==subject:
                        st_grade["grade"]= grade

        with open("student.json", "w") as st:
            json.dump(currSt,st,indent=4)

        print("Student grade updated\n")

    elif choice==4:
        id=int(input("Enter student id: "))

        numList=[]
        for student in currSt:
            if "id" in student and student["id"]==id:
                for st_grade in student["grade"]:
                    numList.append(st_grade["grade"])
        total = 0
        for num in numList:
            total += int(num)
            average = total / len(numList)

        print(f"\nStudent grade average is: {average}\n")


    elif choice==5:
        quit()







