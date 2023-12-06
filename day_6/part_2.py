def count_record_beats(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    times = "".join(lines[0].split()[1:])
    distances = "".join(lines[1].split()[1:])

    count = 0
    for j in range(int(times)):
        if (int(times) - j) * j > int(distances):
            count += 1


    return count

print(count_record_beats("data.txt"))
