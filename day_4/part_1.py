def points_total(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    total = 0
    for line in lines:
        game = line.split(":")
        numbers = game[1].split("|")
        lucky_numbers_, my_numbers_ = numbers[0].strip().split(" "), numbers[1].strip().split(" ")
        lucky_numbers = [int(number.strip()) for number in lucky_numbers_ if number]
        my_numbers = [int(number.strip()) for number in my_numbers_ if number]
        count = 0
        for number in my_numbers:
            if number in lucky_numbers:
                count += 1
        if count > 0:
            total += 2 ** (count - 1)
    return total

print(points_total("../data.txt"))
