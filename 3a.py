# Max Joltage, selecting 2 cells
from dataclasses import dataclass


BatteryIndexes = dict[int, list[int]]


@dataclass
class Bank:
    batteries_int: int
    battery_indexes: BatteryIndexes
    length: int


def main():
    with open("3 - input.txt", encoding="utf-8") as f:
        inputs = [line.strip() for line in f]
    # inputs = inputs[:1]
    # print(inputs)
    total_joltage = 0

    for bank in inputs:
        batteries_int = int(bank)
        battery_indexes: BatteryIndexes = {}
        for index, battery in enumerate(bank):
            battery = int(battery)
            if not battery in battery_indexes:
                battery_indexes[battery] = [index]
            else:
                battery_indexes[battery].append(index)
        print(bank)
        print(battery_indexes)
        bank_processed = Bank(
            batteries_int=batteries_int,
            battery_indexes=battery_indexes,
            length=len(bank),
        )
        bank_joltage = biggest_jolts_in_bank(bank_processed)
        total_joltage += bank_joltage
    print(f"Total joltage is {total_joltage}")


def biggest_jolts_in_bank(bank: Bank) -> int:
    battery_values_sorted = sorted(bank.battery_indexes.keys(), reverse=True)
    first_number = None
    first_number_index = None
    for i in battery_values_sorted:
        if (
            len(bank.battery_indexes[i]) == 1
            and bank.battery_indexes[i][0] == bank.length - 1
        ):
            continue
        first_number = i
        first_number_index = sorted(bank.battery_indexes[i])[0]
        break
    # print(battery_values_sorted)
    # print(f"First number: {first_number} at index {first_number_index}")

    for i in battery_values_sorted:
        # All indexes are before the first number
        for index in bank.battery_indexes[i]:
            if index > first_number_index:
                second_number = i
                # print(f"Second number: {second_number} at index {index}")
                return first_number * 10 + second_number

    return 0


# def biggest_combination(start)


if __name__ == "__main__":
    main()
