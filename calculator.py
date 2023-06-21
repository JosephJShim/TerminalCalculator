def calculate():
    a, b, op = userInput()
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    formatResult = str(result)
    print("Result is " + formatResult)
    loop()

def userInput():
    a = float(input("Enter first number: "))

    b = float(input("Enter second number: "))

    op = input("Enter operation (+, -, *, /): ")

    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Invalid operation entered")
        userInput()    
    return a, b, op

def loop(): 
    choice = input("Want to continue (Y, N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        exit
    else:
        print("Invalid Input")
        loop()

calculate()