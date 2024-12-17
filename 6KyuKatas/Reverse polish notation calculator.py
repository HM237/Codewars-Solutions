def calc(expr):
    stack = []
    expression = expr.split(" ")
    if expression[0] == '': return 0
    elif len(expression) == 1: return float(expression[0])
    for character in expression:
        if character not in list('+-*/'): stack.append(float(character))
        else:
            print(stack)
            numbers = stack[-2:]
            new_number = eval(f'{numbers[0]} {character} {numbers[1]}')
            stack.pop(stack.index(numbers[0]))
            stack.pop(stack.index(numbers[1]))
            stack.append(new_number)
    return stack[0]
