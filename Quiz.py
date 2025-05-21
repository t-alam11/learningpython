from Questions import *

questiontoask = [
    "What is the capital of France?\nA) Rome\nB) Madrid\nC) Paris\nD) Berlin\n",
    "Which animal is known as the 'King of the Jungle'?\nA) Elephant\nB) Tiger\nC) Lion\nD) Bear\n",
    "How many legs does a spider have?\nA) 6\nB) 8\nC) 10\nD) 12\n",
    "What is the freezing point of water in Celsius?\nA) 0°C\nB) 10°C\nC) 32°C\nD) 100°C\n",
    "What color do you get when you mix red and white?\nA) Purple\nB) Orange\nC) Pink\nD) Brown\n",
]
questions=[
    Questions(questiontoask[0],"c"),
    Questions(questiontoask[1],"c"),
    Questions(questiontoask[2],"b"),
    Questions(questiontoask[3],"a"),
    Questions(questiontoask[4],"c")
]

def quiz(questions):
    score=0
    for question in questions:
        answer2 = input(question.question).lower()
        if answer2 == question.answer:
            print("Correct")
            score+=1
        else:
            print("Incorrect")
    print(f"You got {score} out of {len(questiontoask)} correct, Well Done!")

    playagain=input("Do you want to play again? (y/n): ")
    if playagain == "y":
        while True:
            quiz(questions)
    else:
        exit()


quiz(questions)