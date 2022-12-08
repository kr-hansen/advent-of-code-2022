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

def calc_nested_sizes(sizes, save_dict=None, save_key='/', sum_val=0, iter=0):
    if save_dict == None:
        save_dict = {}
    for sel_key in sizes.keys():
        if isinstance(sizes[sel_key], dict):
            if sel_key in save_dict.keys():
                new_key = f'{sel_key}_{iter}'
                iter += 1
            else:
                new_key = sel_key
            save_dict = calc_nested_sizes(sizes[sel_key], save_dict, save_key=new_key, iter=iter)
        elif isinstance(sizes[sel_key], int):
            sum_val += sizes[sel_key]
            save_dict[save_key] = sum_val
        else:
            dtype = type(sizes[sel_key])
            print(f'Other type: {dtype}')
    return save_dict

def calc_flat_sizes(sizes, max_size=100000):
    total_size = 0
    for path in sizes.keys():
        path_size = sizes[path]['size']
        for subpath in sizes.keys():
            if re.match(rf'^{path}\w+', subpath):
                path_size += sizes[subpath]['size']
        if path_size <= max_size:
            total_size += path_size
    return total_size


def calc_largest_file(file_list, max_size=100000):
    cmd_struct = parse_cmd_output(file_list)
    flat_sizes = calc_nested_sizes(cmd_struct)
    total_size = 0
    for sel_dir in flat_sizes.keys():
        if flat_sizes[sel_dir] <= max_size:
            total_size += flat_sizes[sel_dir]
    return cmd_struct, flat_sizes, total_size

test = read_file("testD7Puzzle.txt")
test_parse, test_flat, test_total = calc_largest_file(test)

full = read_file("inputDay7Puzzle.txt")
full_parse, full_flat, full_total = calc_largest_file(full)
