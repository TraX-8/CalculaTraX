# CalculaTraX
# Copyright (c) 2026 TraX Software
# Licensed under the MIT License


import calculator.operations, calculator.interface

state = True
a = ""
b = ""
operation = ""

def ask_operation():
    while True:
        op = input("Enter the operation (+, *, /, -) : ")
        calculator.interface.line()
        if op in ["+", "*", "/", "-", "**"]:
            return op
        print("This isn't a valid operation. Please retry.")

calculator.interface.appboot("CalculaTraX", "2026, v1.3 BETA", "TraX")



while state == True:
    calculator.interface.line()
    while a == "":
        a = input("Enter the first number (or quit): ")
        try :
            a.lower()
        except:
            a = ""
        if a.lower() == "quit":
            state = False
            raise SystemExit(1)
        try:
            int(a)
            a = int(a)
        except:
            print("Value must be an integer.")
            a = ""
    calculator.interface.line()

    operation = ask_operation()

    while b == "":
        b = input("Enter the second number: ")
        try:
            int(b)
            b = int(b)
        except:
            print("Value must be an integer.")
            b = ""
        if operation == "/" and b == 0:
            print("Error : division by zero.")
            b = ""
    calculator.interface.line()


    match operation :
        case "+":
            result = calculator.operations.sum(a, b)
            operation_text = "sum"
        case "*":
            result = calculator.operations.multiply(a, b)
            operation_text = "multiplication"
        case "/":
            result = calculator.operations.divide(a, b)
            operation_text = "division"
        case "-":
            result = calculator.operations.subtract(a, b)
            operation_text = "subtraction"
        case "**":
            result = calculator.operations.exponent(a, b)
            operation_text = "power"
        case _ :
            print("This shouldn't happen. Invalid operation.")
            raise SystemExit(1)

    if result == "Err : div by 0":
        print("Error : division by zero. This shouldn't happen.")
        raise SystemExit(1)

    print("The "+ operation_text +" of", a, "and", b, "is:")


    try:
        if len(str(result)) < 10:
            calculator.interface.textbox(10, str(result))
        elif len(str(result)) > 10 and len(str(result)) < 20:
            calculator.interface.textbox(20, str(result))
        else:
            calculator.interface.textbox(30, str(result))
    except:
        calculator.interface.textbox(50, "The result contains too much digits.")
        
    if state == True:
        a = ""
        b = ""
    else:
        break
