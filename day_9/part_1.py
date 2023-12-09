def part_1(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    total = 0
    for line in lines:
        total += get_next_value([int(num.strip()) for num in line.split(" ")])

    return total

def get_next_value(l):
    temp_l = [i for i in l]
    temp_pyramid = [temp_l]
    while all([i == 0 for i in temp_pyramid[-1]]) == False:
        new_l = []
        temp_l = [i for i in temp_pyramid[-1]]
        for i in range(len(temp_l) - 1):
            new_l.append(temp_l[i+1] - temp_l[i])
        temp_pyramid.append(new_l)

    n = 0
    for i in range(len(temp_pyramid)):
        n += temp_pyramid[i][-1]

    return n

print(part_1("data.txt"))
