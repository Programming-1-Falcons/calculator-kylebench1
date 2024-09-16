while True:
    num1 = float(input("Enter Numerical Value 1: "))
    operation = input("Enter Operation Character: ")
    num2 = float(input("Enter Numerical Value 2: "))

    if operation == "+":
        result = (num1+num2)
    if operation == "-":
        result = (num1-num2)
    if operation == "*":
        result = (num1*num2)
    if operation == "/":
        result = (num1/num2)
    if operation in "+-*/":
        print(num1, operation, num2, "=", result)
    else: 
        print("Syntax Error")