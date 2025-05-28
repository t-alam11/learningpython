import csv

with open("contactbooky.csv", "a", newline="") as f:
    writer = csv.writer(f)
    f.seek(0, 2)
    if f.tell() == 0:
        writer.writerow(["Name", "Number"])


def book():
    print("\nCONTACT BOOK")
    print("---------------------------------\n")
    print("1.Add a contact")
    print("2.Show all contacts")
    print("3.Delete a contact")
    print("4.Search for a contact")
    print("5.Exit\n")

while True:
    book()
    choice = int(input("Enter your choice(1-5): "))
    if choice == 1:
        name = input("Enter a name: ")
        number = int(input("Enter a number: "))
        with open("contactbooky.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, number])
        print(f"{name} added\n")

    elif choice == 2:
        with open("contactbooky.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    elif choice == 5:
        exit()

    elif choice == 3:
        deleteName=input("Enter a name: ").strip().lower()
        contacts=[]

        with open("contactbooky.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].strip().lower() != deleteName:
                    contacts.append(row)

        with open("contactbooky.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(contacts)

        print(f"{deleteName} deleted\n")

    elif choice == 4:
        searchName=input("Enter a name: ").strip().lower()
        searchNum=int(input("Enter a number: "))
        with open("contactbooky.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].strip().lower() == searchName or row[1].strip().lower():
                    print(f"{row} found\n")


