import math

def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def is_in_kernel(T, H):
    kernel_list = []
    for i in range(H[0]-1, H[0]+2):
        for j in range(H[1]-1, H[1]+2):
            kernel_list.append([i, j])
    if T in kernel_list:
        return True
    return False

def simulate_rope_pull(move_list, snake_size=1):
    snake = {x: [0, 0] for x in range(snake_size+1)}
    H = [0, 0]
    T = [0, 0]
    T_spots = [tuple(snake[snake_size])]
    for move in move_list:
        move_dir, steps = move.split(' ')
        if move_dir == 'R':
            adj_idx, static_idx, iter = 0, 1, 1
        elif move_dir == 'L':
            adj_idx, static_idx, iter = 0, 1, -1
        elif move_dir == 'U':
            adj_idx, static_idx, iter = 1, 0, 1
        elif move_dir == 'D':
            adj_idx, static_idx, iter = 1, 0, -1
        else:
            print('Non-standard Move')
        for m in range(1, int(steps)+1):
            snake[0][adj_idx] += iter
            for snake_part in range(1, snake_size+1):
                if is_in_kernel(snake[snake_part], snake[snake_part-1]):
                    continue
                else:
                    diff_x = snake[snake_part-1][0] - snake[snake_part][0]
                    diff_y = snake[snake_part-1][1] - snake[snake_part][1]
                    if diff_x == 0:
                        change_idx = 1
                        change_val = int(math.copysign(iter, diff_y))
                        snake[snake_part][change_idx] += change_val
                    elif diff_y == 0:
                        change_idx = 0
                        change_val = int(math.copysign(iter, diff_x))
                        snake[snake_part][change_idx] += change_val
                    else:
                        x_change = int(math.copysign(iter, diff_x))
                        snake[snake_part][0] += x_change
                        y_change = int(math.copysign(iter, diff_y))
                        snake[snake_part][1] += y_change
                if snake_part == snake_size:
                    T_spots.append(tuple(snake[snake_size]))
    return len(set(T_spots)), T_spots


test = read_file("testD9Puzzle.txt")
test_nspots, test_spots = simulate_rope_pull(test, snake_size=9)

test_long = read_file("testD9Puzzle2.txt")
test_long_nspots, test_long_spots = simulate_rope_pull(test_long, snake_size=9)

full = read_file("inputD9Puzzle.txt")
full_nspots, full_spots = simulate_rope_pull(full, snake_size=9)
