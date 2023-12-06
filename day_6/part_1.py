def count_record_beats(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    wins_to_win = []
    for i in range(len(times)):
        count = 0
        for j in range(times[i]):
            if (times[i] - j)*j > distances[i]:
                count += 1
        wins_to_win.append(count)
    result = 1
    for i in wins_to_win:
        result *= i
    return result

print(count_record_beats("data.txt"))
