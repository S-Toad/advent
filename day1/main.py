

def main():
    SUM_COUNT = 2020
    value_set = set()
    with open('data.txt') as data:
        for line in data.read().splitlines():
            # Check if the value needed was found already
            val = int(line)
            val_needed = SUM_COUNT - val
            # If so, print solution
            if val_needed in value_set:
                print('Solution:', val_needed * val)
                return
            # Otherwise add the value seen to our set
            else:
                value_set.add(val)


if __name__ == "__main__":
    main()
