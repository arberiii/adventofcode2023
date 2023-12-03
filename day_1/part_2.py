numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_calibration_value(file_path: str) -> int:
    total = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        line = line.lower()
        first_digit_index = None
        first_digit = None
        last_digit_index = None
        last_digit = None
        for i in range(len(line)):
            if line[i].isdigit():
                if first_digit_index is None:
                    first_digit_index = i
                    first_digit = int(line[i])
                last_digit_index = i
                last_digit = int(line[i])

            for number in numbers:
                if line[i:].startswith(number):
                    if first_digit_index is None or first_digit_index > i:
                        first_digit_index = i
                        first_digit = numbers[number]
                    if last_digit_index is None or last_digit_index < i:
                        last_digit_index = i
                        last_digit = numbers[number]

        total += (first_digit or 0) * 10 + (last_digit or 0)
    return total


print(get_calibration_value("data.txt"))
