def calc(operation, op1, op2):
    if operation == "x":
        return op1 * op2
    elif operation == "/":
        return op1 / op2
    elif operation == "-":
        return op1 - op2
    elif operation == "+":
        return op1 + op2
    
    
    raise Exception(f"Unknown operation '{operation}'")
    


def parse(command):
    parts = command.split(" ")
    if parts[0] == "calc":
        return calc(parts[1], int(parts[2]), int(parts[3]))

def nextLine(command):
    parts = command.split(" ")
    if parts[1] == "calc":
        return int(parse(command[5:]))
    else:
        return int(parts[1])