import re

def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def get_line_idxs(cur_line):
    return [idx for idx, col in enumerate(cur_line) if col not in [' ', '[', ']']]


def build_crate_inputs(input_list, split_line):
    line_idxs = get_line_idxs(input_list[split_line-1])
    crate_setup = {int(input_list[split_line-1][idx]): [] for idx in line_idxs}
    crate_conversion = {idx: int(input_list[split_line-1][idx]) for idx in line_idxs}
    for h in range(2, split_line+1):
        cur_line = input_list[split_line-h]
        new_idxs = get_line_idxs(cur_line)
        for idx in new_idxs:
            crate_setup[crate_conversion[idx]].append(cur_line[idx])
    return crate_setup

def parse_line(line_val):
    amount = int(re.findall("move \d+", line_val)[0].split(' ')[1])
    start = int(re.findall("from \d+", line_val)[0].split(' ')[1])
    finish = int(re.findall("to \d+", line_val)[0].split(' ')[1])
    return amount, start, finish

def find_top_crates(input_list, reverse=True):
    split_line = input_list.index('')
    crates = build_crate_inputs(input_list, split_line)
    for ln in range(split_line+1, len(input_list)):
        amount, start, finish = parse_line(input_list[ln])
        if reverse:
            crates[finish].extend(crates[start][-amount:][::-1])
        else:
            crates[finish].extend(crates[start][-amount:])
        crates[start] = crates[start][:-amount]
    output_list = []
    for k in crates.keys():
        if crates[k]:
            output_list.append(crates[k][-1])
        else:
            output_list.append(' ')
    return output_list, crates, ln


test = read_file("testD5Puzzle.txt")
test_name, test_crates, lnt = find_top_crates(test, reverse=True)
test_name1, test_crates1, lnt1 = find_top_crates(test, reverse=False)

test2 = read_file("test2D5Puzzle.txt")
test_name2, test_crates2, lnt2 = find_top_crates(test2, reverse=True)
test_name21, test_crates21, lnt21 = find_top_crates(test2, reverse=False)

full = read_file("inputD5Puzzle.txt")
full_name, full_crates, ln = find_top_crates(full, reverse=True)
full_name1, full_crates1, ln1 = find_top_crates(full, reverse=False)
