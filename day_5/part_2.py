def lowest_range_location_number(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    seeds_ = lines[0].split()
    positions = [int(x) for x in seeds_[1:]]

    line_position = 1
    new_positions = []

    while line_position < len(lines):
        if lines[line_position] == "":
            if new_positions:
                positions.extend([x for x in new_positions])
                new_positions = []
            line_position += 2

            continue

        map_details = [int(x) for x in lines[line_position].split()]
        destination_range, source_range, range_length = map_details[0], map_details[1], map_details[2]
        temp_positions = []
        for i in range(len(positions)//2):
            if max(source_range, positions[2*i]) < min(source_range + range_length - 1, positions[2*i] + positions[2*i+1] - 1):
                start = max(source_range, positions[2*i])
                end = min(source_range + range_length - 1, positions[2*i] + positions[2*i+1] - 1)
                if start > positions[2*i]:
                    temp_positions.append(positions[2*i])
                    temp_positions.append(start - positions[2*i])
                if end < positions[2*i] + positions[2*i+1] - 1:
                    temp_positions.append(end + 1)
                    temp_positions.append(positions[2*i] + positions[2*i+1] - 1 - end)
                new_positions.append(destination_range + (start - source_range))
                new_positions.append(end - start + 1)
            else:
                temp_positions.append(positions[2*i])
                temp_positions.append(positions[2*i+1])

        positions = [x for x in temp_positions]
        line_position += 1
    minimum = None
    positions.extend([x for x in new_positions])
    for i in range(len(positions)//2):
        if minimum is None or positions[2*i] < minimum:
            minimum = positions[2*i]

    return minimum

print(lowest_range_location_number("data.txt"))
