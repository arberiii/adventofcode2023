import math
from collections import defaultdict
from functools import cmp_to_key


def part_2(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    instructions = lines[0]

    paths = []
    for line in lines[2:]:
        x = line.split("=")
        path = [None, None]
        path[0] = x[0].strip()
        y = x[1].strip().split(',')
        z = (y[0].strip('(').strip(), y[1].strip(')').strip())
        path[1] = z
        paths.append(path)

    starting_points = []
    for path in paths:
        if path[0][-1] == 'A':
            starting_points.append(path[0])

    d = {x[0]: x[1] for x in paths}

    steps = []
    for starting_point in starting_points:
        steps.append(get_ending_z(d, starting_point, instructions))
    
    return math.lcm(*steps)

def get_ending_z(d, start, instructions):
    count = 0
    current = start
    while True:
        instruction = instructions[count % len(instructions)]
        if instruction == "R":
            new_current = d[current][1]
        else:
            new_current = d[current][0]
        if new_current[-1] == 'Z':
            return count + 1

        current = new_current
        count += 1
    return 0

print(part_2("data.txt"))
