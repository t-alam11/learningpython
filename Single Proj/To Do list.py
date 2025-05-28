#To do list add tasks, remove tasks, show all tasks, exit program

tasks=[]

def removal(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed\n")

def menu():
    print("--------------------------\n")
    print("Welcome to the ToDo List\n")
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. See the tasks list")
    print("4. Exit")

while True:
    menu()
    choice=int(input("\nEnter your choice: "))

    if choice==1:
        tasks.append(input("Enter a task: "))
        print("Task added\n")

    elif choice==3:
        if len(tasks)==0:
            print("No tasks here\n")
        else:
            for elem in tasks:
                print(elem)

    elif choice==4:
        print("Thank you , Goodbye\n")
        break

    elif choice==2:
        if len(tasks)==0:
            print("No tasks here\n")
        else:
            for elem in tasks:
                print(elem)
            deletion=input("Which task would you like to remove? ")
            removal(deletion)




