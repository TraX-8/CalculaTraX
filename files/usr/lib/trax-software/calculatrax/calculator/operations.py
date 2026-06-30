def sum(a, b):
    try:
        int(a)
        int(b)
    except:
        print("The numbers must be integers.")
        return ValueError
    result = a + b
    return result

def multiply(a, b):
    try:
        int(a)
        int(b)
    except:
        print("The numbers must be integers.")
        return ValueError
    result = a * b
    return result

def divide(a, b):
    try:
        int(a)
        int(b)
        result = a / b
    except ZeroDivisionError:
        result = "Err : div by 0"
    return result

def subtract(a, b):
    try:
        int(a)
        int(b)
    except:
        print("The numbers must be integers.")
        return ValueError
    result = a - b
    return result

def exponent(a, b):
    try:
        int(a)
        int(b)
    except:
        print("The numbers must be integers.")
        return ValueError
    result = a ** b
    return result