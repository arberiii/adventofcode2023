def gear_ratio(file_path: str) -> int:
    total = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    matrix = [[char for char in line] for line in lines]
    d = {}
    for row in range(len(matrix)):
        current_number = 0
        current_stars = set()
        for column in range(len(matrix[row])):
            if matrix[row][column].isdigit():
                current_number = current_number * 10 + int(matrix[row][column])
                for star in get_star_adjacent_symbols(matrix, row, column):
                    current_stars.add(star)
            else:
                if current_number > 0:
                    for star in current_stars:
                        if star not in d:
                            d[star] = set()
                        d[star].add(current_number)
                current_number = 0
                current_stars = set()
        if current_number > 0:
            for star in current_stars:
                if star not in d:
                    d[star] = set()
                d[star].add(current_number)

    for key, value in d.items():
        if len(value) == 2:
            v_1 = value.pop()
            v_2 = value.pop()
            total += v_1 * v_2
    return total

def get_star_adjacent_symbols(matrix: list[list[str]], row: int, col: int) -> set[tuple[int, int]]:
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1,-1], [1, 0], [1, 1]]
    ret = set()
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
            if value == "*":
                ret.add((new_row, new_col))
        except IndexError:
            continue
    return ret

print(gear_ratio("../data.txt"))
