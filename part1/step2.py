from calculator import parse
import math

def step2():
    print(parse("calc + 1 2"))
    with open("step2.txt", "r") as f:
        outputs = [parse(line) for line in f.read().splitlines()]
    print(math.fsum(outputs))
