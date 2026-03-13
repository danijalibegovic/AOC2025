import numpy as np

def read_input_10(filename):
    with open(filename) as f:
        machines = []
        for l in f.readlines():
            m = l.strip("\n").split(" ")
            lights = m[0][1:-1].replace(".","0").replace("#","1")
            joltage = np.array([int(n) for n in m[-1][1:-1].split(",")])
            buttons = []
            for b in m[1:-1]:
                button = len(lights)*["0"]
                for i in [int(k) for k in b[1:-1].split(",")]:
                    button[i] = "1"
                buttons.append("".join(button))
            machine = (int(lights,base=2), [int(b,base=2) for b in buttons], joltage)
            machines.append(machine)
    return machines
from collections import deque

def min_xor_steps(target, masks):
    start = 0
    queue = deque([(start, 0)]) 
    visited = {start}

    while queue:
        value, steps = queue.popleft()
        if value == target:
            return steps

        for m in masks:
            new_val = value ^ m
            if new_val not in visited:
                visited.add(new_val)
                queue.append((new_val, steps + 1))
    
    return None
def part1(filename):
    machines = read_input_10(filename)
    presses = 0 
    for machine in machines:
        lights, buttons, _ = machine
        presses += min_xor_steps(lights, buttons)
    return presses
print("Part 1:", part1("factory.txt"))