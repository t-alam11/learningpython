#Password Generator

import random
import string

length=int(input("Enter the length of the password: "))

chars=string.ascii_letters
chars += string.digits
chars += string.punctuation

pwd=""

for i in range(length):
    nextchar=random.choice(chars)
    pwd += nextchar

print(f"Your generated password is: {pwd}")