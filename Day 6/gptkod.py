import re
import math

# read file
with open("trashCompactor.txt", "r", encoding="utf-8") as f:
    raw_lines = [line.rstrip("\n") for line in f]

# Expect 5 lines: 4 number rows and 1 operator row
if len(raw_lines) < 5:
    raise SystemExit("test.txt must contain 5 lines (4 number rows + 1 operator row)")

# pad all lines to the same width so indexing is safe
maxlen = max(len(raw_lines[i]) for i in range(5))
lines = [raw_lines[i].ljust(maxlen) for i in range(5)]

# -------- PART 1 (simple whitespace-split arithmetic) ----------
# Use findall to get integer tokens (avoids empty-string -> int('') error)
l0 = list(map(int, re.findall(r"\d+", lines[0])))
l1 = list(map(int, re.findall(r"\d+", lines[1])))
l2 = list(map(int, re.findall(r"\d+", lines[2])))
l3 = list(map(int, re.findall(r"\d+", lines[3])))
# operators for part1: split by whitespace but strip first to avoid empty tokens
ops_part1 = re.split(r"\s+", lines[4].strip())

answer1 = 0
for i in range(len(ops_part1)):
    op = ops_part1[i]
    if op == "+":
        answer1 += l0[i] + l1[i] + l2[i] + l3[i]
    else:
        answer1 += l0[i] * l1[i] * l2[i] * l3[i]

# -------- PART 2 (segment-based, handles mixed alignment) ----------
answer2 = 0

# find positions of non-space chars in operator row (these mark operation columns)
split_points = [m.start() for m in re.finditer(r"\S", lines[4])]
# if nothing found, nothing to do
if split_points:
    split_points.append(maxlen)  # add end-of-line as last boundary

    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i + 1]

        numbers = []
        # for each column in this segment, build the vertical number from the 4 rows
        for j in range(start, end):
            colchars = lines[0][j] + lines[1][j] + lines[2][j] + lines[3][j]
            colchars = colchars.strip()
            if colchars != "":
                numbers.append(int(colchars))

        op = lines[4][start]
        if op == "+":
            answer2 += sum(numbers)
        elif op == "*":
            # if numbers empty, math.prod([]) would raise; but empty means nothing to multiply
            answer2 += math.prod(numbers) if numbers else 0
        else:
            # if operator is something else (shouldn't happen) skip
            pass

print("Part 1:", answer1)
print("Part 2:", answer2)
