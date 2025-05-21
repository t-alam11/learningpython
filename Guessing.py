import random

def guessing(guess):
    answer=0
    computer=random.randint(1,guess)
    while computer!=answer:
        answer=int(input(f"Guess the number between 1 and {guess}: "))
        if answer>computer:
            print ("Too high")
        elif answer<computer:
            print("Too low")

    print(f"You guessed right!, it was {answer}")


guessing(10)

