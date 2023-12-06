def lowest_location_number(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    seeds_ = lines[0].split()

    positions = [int(x) for x in seeds_[1:]]
    line_position = 1
    new_positions = [x for x in positions]
    while line_position < len(lines):
        if lines[line_position] == "":
            positions = [x for x in new_positions]
            line_position += 2
            continue

        map_details = [int(x) for x in lines[line_position].split()]
        destination_range, source_range, range_length = map_details[0], map_details[1], map_details[2]
        for i in range(len(positions)):
            if source_range <= positions[i] < source_range + range_length:
                new_positions[i] = destination_range + (positions[i] - source_range)
        line_position += 1

    return min(new_positions)

print(lowest_location_number("data.txt"))
