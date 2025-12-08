# Invalid ID: ID which is made
# - only
# - sequence of digits repeated twice
#
# Answer is the SUM of invalid id's


def main():
    with open("2 - input.txt", encoding="utf-8") as f:
        inputs = f.read().strip().split(",")
    print(inputs)

    id_sum = 0

    for id_range in inputs:
        print(id_range)
        # range is inclusive
        range_start, range_end = [int(i) for i in id_range.split("-")]
        print(range_start, range_end)
        for id_ in range(range_start, range_end + 1):
            if not is_valid(id_):
                id_sum += id_
                print(f"{id_} is not a valid id")

    print(f"Sum of invalid id's: {id_sum}")


def is_valid(id_: int) -> bool:
    id_string = str(id_)

    # Can't be made of two sequences of digits if length is odd
    if len(id_string) % 2 == 1:
        return True

    half_len = len(id_string) // 2
    return not id_string[:half_len] == id_string[half_len:]


if __name__ == "__main__":
    main()
