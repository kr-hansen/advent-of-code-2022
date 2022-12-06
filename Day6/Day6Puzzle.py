def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def find_start_of_buffer(message: str, start_idx):
    charset = set()
    idx = start_idx
    while len(charset) < start_idx+1:
        charset = set([message[i] for i in range(idx-start_idx, idx+1)])
        idx += 1
    return idx, charset


test = read_file('testD6Puzzle.txt')
test_idx, test_charset = find_start_of_buffer(test[0], start_idx=3)
test_idx_message, test_charset_message = find_start_of_buffer(test[0], start_idx=13)

full = read_file('inputDay6Puzzle.txt')
full_idx, full_charset = find_start_of_buffer(full[0], start_idx=3)
full_idx_message, full_charset_message = find_start_of_buffer(full[0], start_idx=13)
