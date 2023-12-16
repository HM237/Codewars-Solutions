def calculate(num1, operation, num2):
    if num2 == 0 and operation == "/":
        return None
    elif operation == "+":
        return ( num1 + num2)
    elif operation == "-":
        return (num1 - num2)
    elif operation == "*":
        return ( num1 * num2)
    elif operation == "/":
        return (num1 / num2)
    else:
        return None
