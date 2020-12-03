

def main(is_part_one=False):
    count = 0
    with open('data.txt') as data:
        for line in data.read().splitlines():
            rules, key, password = line.split(' ')

            rules = rules.split('-')
            rule_1 = int(rules[0])
            rule_2 = int(rules[1])
            key = key[0]

            if is_part_one:
                count += part_one_validate(rule_1, rule_2, key, password)
            else:
                count += part_two_validate(rule_1, rule_2, key, password)

    print(f'{count} valid passwords')

def part_one_validate(at_least, at_most, key, password):
    char_count = 0
    for c in password:
        if c == key:
            char_count += 1

    return at_least <= char_count <= at_most

def part_two_validate(pos1, pos2, key, password):
    has_char1 = password[pos1-1] == key
    has_char2 = password[pos2-1] == key
    return has_char1 ^ has_char2

if __name__ == "__main__":
    main(is_part_one=True)
    main(is_part_one=False)
