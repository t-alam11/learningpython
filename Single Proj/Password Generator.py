import random


def play():
    user = input("Choose rock (r), paper (p), scissors (s): ")
    computerchoice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computerchoice}")

    if (user == "r" and computerchoice == "rock") or (user == "p" and computerchoice == "paper") or (
            user == "s" and computerchoice == "scissors"):
        print("You tied")

    elif (user == "r" and computerchoice == "scissors") or (user == "p" and computerchoice == "rock") or (
            user == "s" and computerchoice == "paper"):
        print("You won")

    else:
        print("You lose")

    playagain = input("Do you want to play again? (y/n): ")
    if playagain == "y":
        while True:
            play()
    else:
        print("Thank you for playing")
        exit()

play()