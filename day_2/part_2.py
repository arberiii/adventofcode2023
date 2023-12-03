def count_power_of_games(file_path: str) -> int:
    total = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        x = line.split(":")
        game, cube_rounds = x[0], x[1]
        is_valid = True
        counts = {}
        for cube_round in cube_rounds.split(";"):
            cube_round = cube_round.strip()
            for cube_count in cube_round.split(","):
                cube_count = cube_count.strip()
                y = cube_count.split(" ")
                count, cube = y[0], y[1]
                if cube not in counts:
                    counts[cube] = 0
                if counts[cube] < int(count):
                    counts[cube] = int(count)
        game_power = 1
        for cube in counts:
            game_power *= counts[cube] if counts[cube] > 0 else 1
        total += game_power
    return total


print(count_power_of_games("../data.txt"))
