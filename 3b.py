# Max Joltage, selecting 12 cells
from dataclasses import dataclass


BatteryIndexes = dict[int, list[int]]


@dataclass
class Bank:
    # batteries_int: int
    battery_values: list[int]
    battery_indexes: BatteryIndexes
    length: int


def main():
    with open("3 - input.txt", encoding="utf-8") as f:
        inputs = [line.strip() for line in f]
    # inputs = inputs[:1]
    # print(inputs)
    total_joltage = 0

    for bank in inputs:
        # batteries_int = int(bank)
        battery_values = [int(b) for b in bank]
        battery_indexes: BatteryIndexes = {}
        for index, battery in enumerate(bank):
            battery = int(battery)
            if not battery in battery_indexes:
                battery_indexes[battery] = [index]
            else:
                battery_indexes[battery].append(index)
        # print(bank)
        # print(battery_indexes)
        bank_processed = Bank(
            # batteries_int=batteries_int,
            battery_values=battery_values,
            battery_indexes=battery_indexes,
            length=len(bank),
        )
        bank_joltage = biggest_jolts_in_bank(bank_processed)
        print(bank_joltage)
        total_joltage += bank_joltage
    print(f"Total joltage is {total_joltage}")


def biggest_jolts_in_bank(bank: Bank) -> int:
    battery_values_sorted = sorted(bank.battery_indexes.keys(), reverse=True)
    digits: list[int] = []
    num_digits = 12
    first_valid_index = 0
    len_digits = len(digits)
    last_valid_index = bank.length - num_digits
    while len(digits) < num_digits:
        valid_slice = bank.battery_values[first_valid_index : last_valid_index + 1]
        max_val = max(valid_slice)
        digits.append(max_val)
        len_digits = len(digits)
        first_valid_index = valid_slice.index(max_val) + first_valid_index + 1
        last_valid_index += 1
    ret_val = list_of_ints_to_int(digits)
    # if not ret_val == max(bank.battery_values):
    #    raise ValueError("Algo is fucked")
    return ret_val
    # raise ValueError("Unexpected error")


def list_of_ints_to_int(data: list[int]) -> int:
    result = 0
    for index, value in enumerate(data[::-1]):
        result = result + 10**index * value
    return result


if __name__ == "__main__":
    main()
