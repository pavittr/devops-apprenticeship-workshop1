from calculator import nextLine
def step3(debug = False):
    hitlines = []
    currentline = 1

    with open("step3.txt", "r") as f:
        lines = [line for line in f.read().splitlines()]

    while currentline not in hitlines:
        if debug:
            print(f"loop {currentline}")
        hitlines.append(currentline)
        fullLine = lines[currentline - 1]
        if debug:
            print(fullLine)
        next = nextLine(fullLine)
        if debug:
            print(next)
        currentline = next
        if debug:
            print(f"loop done: {currentline}")

    print(f"Ending line was {currentline}")

