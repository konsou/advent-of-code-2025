PAPER = "@"
FREE = "."


def main():
    with open("4 - input.txt", encoding="utf-8") as f:
        rows: list[list[str]] = [[c for c in line.strip()] for line in f]

    total_removed = 0

    while True:
        # 1: scan accessible
        num_accessible_papers = 0
        accessible_paper_coords: list[tuple[int, int]] = []
        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                # print("--")
                # print(row)
                # print(y, x, char)
                if char == PAPER:
                    adjacent = get_adjacent(x, y, rows)
                    if adjacent.count(PAPER) < 4:
                        num_accessible_papers += 1
                        accessible_paper_coords.append((x, y))
        print(f"{num_accessible_papers} paper rolls accessible")

        if num_accessible_papers == 0:
            print(f"No more paper rolls to remove.")
            print(f"Removed a total of {total_removed} rolls.")
            return

        # 2: remove
        for x, y in accessible_paper_coords:
            rows[y][x] = FREE
        total_removed += num_accessible_papers

        # for line in rows:
        #    print("".join(line))

        print(f"Accessible paper rolls removed")
        # input(f"Press ENTER to continue...")


def get_adjacent(x: int, y: int, grid: list[list[str]]) -> list[str]:
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
