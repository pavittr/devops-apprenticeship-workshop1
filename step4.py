from calculator import nextLine
import math

def step4(debug = False):
    complexHitLines = []
    cursor = 1

    with open("step4.txt", "r") as f:
        complexlines = [line for line in f.read().splitlines()]

    if debug:
        print(f"Line count: {len(complexlines)}")
    while cursor not in complexHitLines and cursor <= len(complexlines):
        if debug:
            print(f"loop {cursor}")
        complexHitLines.append(cursor)
        fullLine = complexlines[cursor - 1]
        if debug:
            print(fullLine)
        if fullLine.startswith("replace"):
            parts = fullLine.split(" ")
            src = int(parts[2])
            dst = int(parts[1])
            lineCount = len(complexlines)
            if src <= lineCount and dst <= lineCount:
                complexlines[dst - 1] = complexlines[src - 1]
            cursor = cursor + 1
        elif fullLine.startswith("remove"):
            parts = fullLine.split(" ")
            removableLine = int(parts[1])
            if removableLine <= len(complexlines):
                complexlines.pop(removableLine - 1)
                for hitLineIndex in range(0, len(complexHitLines)):
                    hitLine = complexHitLines[hitLineIndex]
                    if hitLine > removableLine:
                        complexHitLines[hitLineIndex] = complexHitLines[hitLineIndex] - 1

                if cursor < removableLine:
                    cursor = cursor + 1
            else:
                cursor = cursor + 1
        else:
            next = nextLine(fullLine)
            if debug:
                print(next)
            cursor = next
        if debug:
            print(f"loop done: {cursor}")

    print(f"Ending line was {cursor}")