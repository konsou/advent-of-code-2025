# Invalid ID: ID which is made
# - only
# - sequence of digits repeated AT LEAST twice
#
# Answer is the SUM of invalid id's


def main():
    with open("2 - input.txt", encoding="utf-8") as f:
        inputs = f.read().strip().split(",")
    print(inputs)

    id_sum = 0

    for id_range in inputs:
        # print(id_range)
        # range is inclusive
        range_start, range_end = [int(i) for i in id_range.split("-")]
        # print(range_start, range_end)
        for id_ in range(range_start, range_end + 1):
            if not is_valid(id_):
                id_sum += id_
                print(f"{id_} is not a valid id")

    print(f"Sum of invalid id's: {id_sum}")


def is_valid(id_: int) -> bool:
    id_string = str(id_)
    id_len = len(id_string)

    # Can't repeat more times than length of the number
    for repeats in range(2, id_len + 1):
        # Can't have n repeats if not divisible by n
        if id_len % repeats > 0:
            continue

        parts = split_n_ways(id_string, repeats)
        # All elements are same -> only repeats
        if len(set(parts)) == 1:
            return False

    return True


def split_n_ways(input_string: str, parts: int) -> list[str]:
    parts_list = []
    characters_per_part = len(input_string) // parts
    for i in range(parts):
        parts_list.append(input_string[:characters_per_part])
        input_string = input_string[characters_per_part:]
    return parts_list


if __name__ == "__main__":
    # split_n_ways("123123123", 4)
    main()
