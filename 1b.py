# dial: 0-99
# starts at 50
# pw: number of times ends up pointing at 0 OR passes 0
# left: lower
# right: higher


def main():
    with open("1 - input.txt", encoding="utf-8") as f:
        inputs = [i.strip() for i in f.readlines()]
    print(inputs)
    dial = 50
    zeroes = 0

    for i in inputs:
        direction = i[0]
        amount = int(i[1:])
        print(direction, amount)

        # Fuck it we ball
        while amount:
            if direction.lower() == "l":
                dial -= 1
            else:
                dial += 1
            amount -= 1

            dial %= 100

            if dial == 0:
                zeroes += 1

    print(f"Zeroes: {zeroes}")

if __name__ == '__main__':
    main()