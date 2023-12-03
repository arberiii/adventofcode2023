def count_possible_games(file_path: str) -> int:
    total = 0

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        x = line.split(":")
        game, cube_rounds = x[0], x[1]
        is_valid = True
        for cube_round in cube_rounds.split(";"):
            counts = {}
            cube_round = cube_round.strip()
            for cube_count in cube_round.split(","):
                cube_count = cube_count.strip()
                y = cube_count.split(" ")
                count, cube = y[0], y[1]
                if cube not in counts:
                    counts[cube] = 0
                counts[cube] += int(count)
            if counts.get("red", 0) > 12 or counts.get("green", 0) > 13 or counts.get("blue", 0) > 14:
                is_valid = False
                break
        if is_valid:
            z = game.split(" ")
            game_id = z[1]
            total += int(game_id)
    return total


print(count_possible_games("../data.txt"))
