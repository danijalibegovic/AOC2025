FILENAME = "factory.txt"
from collections import defaultdict
from z3 import Int, Optimize

part2 = 0

with open(FILENAME) as file:
    for line in file.readlines():
        line = line.strip()
        parts = line.split(' ')
        buttons = [[int(x) for x in part[1:-1].split(',')] for part in parts[1:-1]]
        target = [int(x) for x in parts[-1][1:-1].split(',')]

        presses = Int('presses')
        counters = [Int(f"count{i}") for i in range(len(target))]
        button_vars = [Int(f"button{i}") for i in range(len(buttons))]

        counters_button_lookup = defaultdict(list)
        for i, button in enumerate(buttons):
            for index in button:
                counters_button_lookup[index].append(i)

        equations = []

        for counter, counter_buttons in counters_button_lookup.items():
            equations.append(target[counter] == sum([button_vars[i] for i in counter_buttons]))

        for button_var in button_vars:
            equations.append(button_var >= 0)

        equations.append(presses == sum(button_vars))

        opt = Optimize()
        opt.add(equations)
        opt.minimize(presses)
        opt.check()

        output = opt.model()[presses]

        part2 += int(str(output))

print(part2)