def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def track_signal_strength(input_list, cycle_check=[20, 60, 100, 140, 180, 220], line_split=[40, 80, 120, 160, 200]):
    n_cycles = 0
    X = 1
    cycle_tracker = {}
    pixel_list = ['' for _ in range(6)]
    pixel_row = 0
    for cmd in input_list:
        if cmd == 'noop':
            n_cycles_increment = 1
            x_iter = 0
        else:
            x_iter = int(cmd.split(' ')[1])
            n_cycles_increment = 2
        for inc in range(n_cycles_increment):
            if (n_cycles % 40) in [X-1, X, X+1]:
                pixel_list[pixel_row] += '#'
            else:
                pixel_list[pixel_row] += '.'
            n_cycles += 1
            if n_cycles in cycle_check:
                cycle_tracker[n_cycles] = n_cycles * X
            if n_cycles in line_split:
                pixel_row += 1
        X += x_iter
    total_sum = sum(cycle_tracker.values())
    return total_sum, cycle_tracker, pixel_list

def print_pixel_list(pixel_list):
    for row in pixel_list:
        print(row)

test = read_file("testD10Puzzle.txt")
test_sum, test_cycles, test_pixels = track_signal_strength(test)
print_pixel_list(test_pixels)

full = read_file("inputD10Puzzle.txt")
full_sum, full_cycles, full_pixels = track_signal_strength(full)
print_pixel_list(full_pixels)
