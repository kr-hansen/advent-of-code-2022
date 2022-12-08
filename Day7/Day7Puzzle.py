import re

def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def parse_cmd_output(file_list, start_dir='/'):
    file_output = {'/': {}}
    new_dir = None
    cwd = ''
    for line in file_list:
        if line.startswith('$ cd'):
            sel_dir = line.split(' ')[-1]
            if sel_dir == '/':
                file_output[sel_dir]['parent'] = ''
                file_output[sel_dir]['size'] = 0
                cwd = sel_dir
            elif sel_dir == '..':
                cwd = file_output[cwd]['parent']
            else:
                parent_dir = cwd
                cwd = f'{cwd}{sel_dir}/'
                file_output[cwd] = {}
                file_output[cwd]['parent'] = parent_dir
                file_output[cwd]['size'] = 0
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            continue
        elif re.match(r'^\d+', line):
            fsize, fn = line.split(' ')
            file_output[cwd]['size'] += int(fsize)
    return file_output

def calc_flat_sizes(sizes, max_size=100000):
    total_size = 0
    for path in sizes.keys():
        path_size = sizes[path]['size']
        for subpath in sizes.keys():
            if re.match(rf'^{path}\w+', subpath):
                path_size += sizes[subpath]['size']
        if path_size <= max_size:
            total_size += path_size
        sizes[path]['total_size'] = path_size
    return total_size, sizes

def calc_largest_file(file_list, max_size=100000):
    flat_parsed = parse_cmd_output(file_list)
    total_size, adjusted_sizes = calc_flat_sizes(flat_parsed)
    return flat_parsed, total_size

def select_dir_to_delete(sizes, total_size=70000000, free_space=30000000):
    sum_of_all, all_sizes = calc_flat_sizes(sizes, max_size=100000000)
    current_space = all_sizes['/']['total_size']
    total_sizes = [all_sizes[dir]['total_size'] for dir in all_sizes.keys()]
    sorted_sizes = sorted(total_sizes)
    space_to_empty = current_space - (total_size - free_space)
    big_enough_sizes = [sz for sz in sorted_sizes if sz > space_to_empty]
    final_size = min(big_enough_sizes)
    return final_size

test = read_file("testD7Puzzle.txt")
test_parse, test_size = calc_largest_file(test)
del_size = select_dir_to_delete(test_parse)

full = read_file("inputDay7Puzzle.txt")
full_parse, full_size = calc_largest_file(full)
full_del = select_dir_to_delete(full_parse)
