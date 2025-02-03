import random

def  trollcalculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation: ")

    if operation == "+":
        answer= num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        if num2!= 0:
            answer = num1 / num2
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation!")
        return

    random_answer = random.uniform(answer -10,answer+10)

    print(f"The result is : {random_answer:.2f}")

trollcalculator()