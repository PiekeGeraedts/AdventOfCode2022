import numpy as np


def is_visible(x, y, tree_map):
    tree_size = tree_map[x,y]
    # check left
    left = tree_map[x,:y]
    # check right
    right = tree_map[x,y+1:]
    # check up
    up = np.transpose(tree_map)[y,:x]    
    # check down
    down = np.transpose(tree_map)[y,x+1:]
    if min([max(down), max(up), max(left), max(right)]) < tree_size:
        return 1
    return 0


def count_visible(tree_map):
    cnt = 0
    for i in range(len(tree_map)):
        if i == 0 or i == len(tree_map)-1:
            continue
        for j in range(len(tree_map)):
            if j == 0 or j == len(tree_map)-1:
                continue
            cnt += is_visible(i,j, tree_map)
    return cnt


def check_direction(tree_size, trees, reverse):
    if len(trees) == 0:
        return 0
    if reverse:
        n_trees = next((idx for idx, item in enumerate(reversed(trees)) if int(item) >= int(tree_size)), -1)
    else:
        n_trees = next((idx for idx, item in enumerate(trees) if int(item) >= int(tree_size)), -1)
    if n_trees == -1:
        return len(trees)
    if n_trees < len(trees):
        return n_trees+1
    return n_trees     


def calc_visibility(x,y,tree_map):
    tree_size = tree_map[x,y]
    # check left
    left = tree_map[x,:y]
    n_left = check_direction(tree_size, left, True)
    # check right
    right = tree_map[x,y+1:]
    n_right = check_direction(tree_size, right, False)
    # check up
    up = np.transpose(tree_map)[y,:x]
    n_up = check_direction(tree_size, up, True)
    # check down
    down = np.transpose(tree_map)[y,x+1:]
    n_down = check_direction(tree_size, down, False)
    return n_left*n_right*n_up*n_down


def max_visibility(tree_map):
    max_mult = 0
    for i in range(len(tree_map)):
        for j in range(len(tree_map)):
            mult = calc_visibility(i,j, tree_map)
            if mult > max_mult:
                max_mult = mult
            # break
        # break
    return max_mult


def main():
    with open("input_day8.txt", "r") as input:
        input = input.read().splitlines()
    input = [[c for c in input[i]] for i in range(len(input))]
    in_arr = np.array(input)
    
    print ('Visible inner:', count_visible(in_arr))
    print ('Edge trees:', len(in_arr)*4 - 4)

    print ('Maximum visibility:', max_visibility(in_arr))


if __name__ == '__main__':
    main()