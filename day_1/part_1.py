def get_calibration_value(file_path: str) -> int:
    total = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = int(char)
                last_digit = int(char)
        total += first_digit * 10 + last_digit
    return total


print(get_calibration_value("data.txt"))
