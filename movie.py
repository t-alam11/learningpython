import json
try:
    with open('movie.json', 'r') as f:
        movie = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    movie = []
    with open('movie.json', 'w') as f:
        json.dump(movie, f,indent=4)


def menu():
    print("\nWelcome to Movie List")
    print("------------------------\n")
    print("1.Add a movie")
    print("2.View all movies")
    print("3.Search for specific movie")
    print("4.Delete a movie")
    print("5.Mark a movie as watched")
    print("6.Exit\n")

while True:
    menu()
    choice=input("Enter your choice: ")

    if choice=="1":
        title=input("Enter movie title: ").capitalize()
        year=input("Enter movie year: ")
        if_watched= input("Enter if you have watched this movie(y/n): ").lower()
        movie = {"title": title, "year": year, "if_watched": if_watched}
        with open("movie.json","r") as f:
            currData=json.load(f)
            oldList = []
            oldList.append(currData)
            oldList.append(movie)
            with open("movie.json","w") as f:
                json.dump(oldList,f,indent=4)
            print("Movie added\n")

    elif choice=="2":
        with open("movie.json","r") as f:
            currData=json.load(f)
            print(currData)

    elif choice=="3":
        title=input("Enter movie title: ").capitalize()
        with open("movie.json","r") as f:
            currData=json.load(f)
            for movie in currData:
                if "title" in movie and movie["title"]==title:
                    print(movie)

    elif choice=="4":
        title=input("Enter movie title: ").capitalize()
        with open("movie.json","r") as f:
            currData=json.load(f)
        newList=[]
        for movie in currData:
            if "title" in movie and movie["title"] !=title:
                newList.append(movie)
        with open("movie.json","w") as f:
            json.dump(newList,f,indent=4)
            print("Movie deleted\n")

    elif choice=="5":
        title=input("Enter movie you want to change to watched: ").capitalize()
        with open("movie.json", "r") as f:
            currData = json.load(f)
        for movie in currData:
            if "title" in movie and movie["title"]==title:
                movie["if_watched"]="y"

        with open("movie.json","w") as f:
            json.dump(movie,f,indent=4)
            print("Movie changed to watched\n")

    elif choice=="6":
        exit()