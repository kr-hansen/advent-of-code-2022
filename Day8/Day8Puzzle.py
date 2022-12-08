import numpy as np

def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def make_array(list_rows):
    convert_list = []
    for row in list_rows:
        convert_list.append([int(x) for x in row])
    return np.array(convert_list)

def check_vis(tree_height, sub_arr, iter_list):
    for walk in iter_list:
        if sub_arr[walk] >= tree_height:
            return 0
    return 1

def count_visible_trees(row_list):
    arr = make_array(row_list)
    nrow, ncol = arr.shape
    n_visible = 2 * (nrow - 2) + (2 * ncol)
    for i in range(1, nrow-1):
        for j in range(1, ncol-1):
            tree = arr[i, j]
            vis_left = check_vis(tree, arr[i, :], range(j-1, -1, -1))
            vis_right = check_vis(tree, arr[i, :], range(j+1, ncol, 1))
            vis_up = check_vis(tree, arr[:, j], range(i-1, -1, -1))
            vis_down = check_vis(tree, arr[:, j], range(i+1, nrow, 1))
            if vis_left | vis_right | vis_up | vis_down:
                n_visible += 1
    return n_visible

def scenic_score(tree_height, sub_arr, iter_list):
    tree_count = 0
    for walk in iter_list:
        tree_count += 1
        if sub_arr[walk] >= tree_height:
            return tree_count
    return tree_count

def find_best_scenic_score(row_list):
    arr = make_array(row_list)
    nrow, ncol = arr.shape
    best_score = 0
    for i in range(1, nrow-1):
        for j in range(1, ncol-1):
            tree = arr[i, j]
            left = scenic_score(tree, arr[i, :], range(j-1, -1, -1))
            right = scenic_score(tree, arr[i, :], range(j+1, ncol, 1))
            up = scenic_score(tree, arr[:, j], range(i-1, -1, -1))
            down = scenic_score(tree, arr[:, j], range(i+1, nrow, 1))
            current_score = left * right * up * down
            if current_score > best_score:
                best_score = current_score
    return best_score

test = read_file("testD8Puzzle.txt")
test_count = count_visible_trees(test)
test_scenic = find_best_scenic_score(test)

full = read_file("inputDay8Puzzle.txt")
full_count = count_visible_trees(full)
full_scenic = find_best_scenic_score(full)
