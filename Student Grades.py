#Grades

import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Student Name", "Grade"])

def menu():
    print("\nWelcome to Student Grades!")
    print("-----------------------------\n")

    print("Choose an option: \n")
    print("1. Add a student")
    print("2. View all students")
    print("3. Delete a student")
    print("4. Calculate average student grades")
    print("6. Exit\n")



while True:
    menu()
    choice=int(input("Enter your choice: "))
    if choice==1:
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        with open("students.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, grade])
            print(f"{name} added\n")

    elif choice==2:
        with open("students.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    elif choice==3:
        deleteName=input("Enter student name: ")
        newList=[]

        with open("students.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != deleteName:
                    newList.append(row)

        with open("students.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(newList)
            print(f"{deleteName} removed\n")


    elif choice==4:
        totalNum= 0
        count=0
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                totalNum+= float(row[1])
                count+=1
        if count>0:
                    newTotal= totalNum/count
                    print(f"The average grade is {newTotal}\n")

    elif choice==5:
        quit()







