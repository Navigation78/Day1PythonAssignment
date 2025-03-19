
# Get input
firstNum = float(input("Enter the first number: "))
secondNum = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

#calculations

if operation == "+":
    result = firstNum + secondNum
    print(f"{firstNum} + {secondNum} = {result}")
elif operation == "-":
    result = firstNum - secondNum
    print(f"{firstNum} - {secondNum} = {result}")
elif operation == "*":
    result = firstNum * secondNum
    print(f"{firstNum} * {secondNum} = {result}")
elif operation == "/":
    if num2 != 0:
        result = firstNum / secondNum
        print(f"{firstNum} / {secondNum} = {result}")
    else:
        print(" Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
