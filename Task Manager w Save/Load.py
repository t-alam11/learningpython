import json

from LoadCl import Task

def menu():
    print("Welcome to your Task Manager")
    print("------------------------------\n")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit\n")

try:
    with open("tasks.json", "r") as tasks:
        currTasks = json.load(tasks)
        if isinstance(currTasks, dict):
            currTasks=[currTasks]
        with open("tasks.json", "w") as task_fix:
            json.dump(currTasks, task_fix,indent=4)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    currTasks = []
    with open("tasks.json", "w") as tasks:
        json.dump(currTasks,tasks, indent=4)


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        title= input("Enter your title: ").lower()
        deadline = input("Enter your deadline: ")
        complete = input("Did you complete it? (y/n): ").lower()
        while complete not in ["y", "n"]:
            complete = input("Do you complete it? (y/n): ").lower()


        newTask = Task(title, deadline, complete)

        task_dict = {
            "title": newTask.title,
            "deadline": newTask.deadline,
            "complete": newTask.complete
        }
        with open("tasks.json","r") as tasks:
            currTasks = json.load(tasks)
            currTasks.append(task_dict)
        with open("tasks.json","w") as tasks:
            json.dump(currTasks,tasks, indent=4)

        print("Task added\n")

    elif choice == "2":
        with open("tasks.json","r") as tasks:
            currTasks = json.load(tasks)
        if not currTasks:
            print("No tasks added")
        else:
            print(currTasks)

    elif choice == "3":
        title= input("Enter the title of the task you completed: ").lower()
        for task in currTasks:
            if "title" in task and task["title"] ==title:
                task["complete"] = "y"
        with open("tasks.json","w") as tasks:
            json.dump(currTasks,tasks, indent=4)
        print("Task completed\n")

    elif choice == "4":
        title= input("Enter the title of the task you want to delete: ").lower()
        newList=[]
        for task in currTasks:
            if "title" in task and task["title"] !=title:
                newList.append(task)

        with open("tasks.json","w") as tasks:
            json.dump(newList,tasks, indent=4)

        print("Task removed\n")

    elif choice == "5":
            quit()