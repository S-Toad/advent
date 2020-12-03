

def main(is_part_one=False):
    with open('data.txt') as data:
        trees = data.read().splitlines()

    if is_part_one:
        count_num_trees(3, 1, trees)
    else:
        value = 1
        value *= count_num_trees(1, 1, trees)
        value *= count_num_trees(3, 1, trees)
        value *= count_num_trees(5, 1, trees)
        value *= count_num_trees(7, 1, trees)
        value *= count_num_trees(1, 2, trees)

        print(f'The product of trees is: {value}')

def count_num_trees(num_right, num_down, trees):
    i = 0
    tree_count = 0
    N = len(trees[0])

    for j in range(num_down, len(trees), num_down):
        i += num_right
        if trees[j][i % N] == '#':
            tree_count += 1

    print(f'Right {num_right}, down {num_down} -- Encountered {tree_count} trees')

    return tree_count

if __name__ == "__main__":
    main(is_part_one=True)
    print('-' * 50)
    main(is_part_one=False)
