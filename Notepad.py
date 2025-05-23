import json

notes_json={}

with open("notes.json","w") as f:
    json.dump(notes_json,f,indent=4)

def notepad():
    print("\nNotepad")
    print("-------------------\n")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Delete a note")
    print("4. Search for a note")
    print("5. Exit")

while True:
    notepad()
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter your title: ").lower()
        content = input("Enter your note: ").lower()
        data={
            "title": title,
            "content": content
        }
        with open("notes.json","r") as f:
         checkData = json.load(f)
        newList = []
        newList.append(checkData)
        if len(newList) == 0:
            with open("notes.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Note added")
        else:
            with open("notes.json", "r") as f:
                currentData = json.load(f)
            newNote = []
            newNote.append(currentData)
            newEntry = {"title": title, "content": content}
            newNote.append(newEntry)
            with open("notes.json", "w") as f:
                json.dump(newNote, f, indent=4)
                print("New note added")

    elif choice == "2":
        with open("notes.json","r") as f:
            currentData = json.load(f)
            print(currentData)

    elif choice == "3":
        deleteTitle= input("Enter the title of the note you want to delete: ").lower()
        newList = []
        with open("notes.json","r") as f:
            currentData = json.load(f)
        for note in currentData:
            if "title" in note and note["title"].strip() != deleteTitle:
                newList.append(note)

        with open("notes.json","w") as f:
            json.dump(newList, f, indent=4)
            print("Note deleted")

    elif choice == "4":
        searchNote= input("Enter the note you want to search: ").lower()
        with open("notes.json","r") as f:
            currentData = json.load(f)
        for note in currentData:
            if "title" in note and note["title"].strip() == searchNote:
                print(note)

    elif choice == "5":
        exit()