def sum_of_parts(file_path: str) -> int:
    total = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    matrix = [[char for char in line] for line in lines]
    for row in range(len(matrix)):
        current_number = 0
        has_adjacent = False
        for column in range(len(matrix[row])):
            if matrix[row][column].isdigit():
                current_number = current_number * 10 + int(matrix[row][column])
                if has_adjacent_symbols(matrix, row, column):
                    has_adjacent = True
            else:
                if has_adjacent:
                    total += current_number
                current_number = 0
                has_adjacent = False
        if has_adjacent:
            total += current_number
    return total

def has_adjacent_symbols(matrix: list[list[str]], row: int, col: int) -> bool:
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1,-1], [1, 0], [1, 1]]
    for direction in directions:
        try:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row < 0 or new_col < 0:
                continue
            if new_row >= len(matrix) or new_col >= len(matrix[row]):
                continue
            value = matrix[row + direction[0]][col + direction[1]]
            if value.isdigit():
                continue
            if value == ".":
                continue
            return True
        except IndexError:
            continue
    return False

print(sum_of_parts("../data.txt"))
