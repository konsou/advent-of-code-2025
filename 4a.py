PAPER = "@"
FREE = "."


def main():
    with open("4 - input.txt", encoding="utf-8") as f:
        rows = [line.strip() for line in f]

    accessible_papers = 0
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            # print("--")
            # print(row)
            # print(y, x, char)
            if char == PAPER:
                adjacent = get_adjacent(x, y, rows)
                if adjacent.count(PAPER) < 4:
                    accessible_papers += 1
    print(f"{accessible_papers} paper rolls accessible")


def get_adjacent(x: int, y: int, grid: list[str]) -> list[str]:
    # fmt: off
    offsets = ((-1, -1), (0, -1), (1, -1),
               (-1, 0),           (1, 0),
               (-1, 1),  (0, 1),  (1, 1))
    return_values = []
    for (x_offset, y_offset) in offsets:
        current_x = x + x_offset
        current_y = y + y_offset
        coordinate_negative = current_x < 0 or current_y < 0
        y_overflow = current_y > len(grid) -1
        x_overflow = current_x > len(grid[0]) -1
        if coordinate_negative or y_overflow or x_overflow:
            return_values.append(FREE)
            continue

        value_at_coordinates = grid[current_y][current_x]
        return_values.append(value_at_coordinates)
    return return_values


if __name__ == "__main__":
    main()
