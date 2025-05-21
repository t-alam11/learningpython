#Calculator
number1=float(input("Provide the first number: "))

while True:
    operate = input("Enter the operator you want to use (+,-,*,/): ")
    if operate in ["+","-","*","/"]:
        break
    else:
        print("Invalid operator, provide correct one")

number2=float(input("Provide the second number: "))

if operate == "+":
    print(number1+number2)
elif operate == "-":
    print(number1-number2)
elif operate == "*":
    print(number1*number2)
elif operate == "/":
    print(number1/number2)

