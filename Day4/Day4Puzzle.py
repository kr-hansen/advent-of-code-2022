def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def find_full_containment(pairs):
    n_contained = 0
    for pair in pairs:
        elf_ranges = pair.split(',')
        elf1 = elf_ranges[0].split('-')
        elf2 = elf_ranges[1].split('-')
        if (int(elf1[0]) <= int(elf2[0])) & (int(elf1[1]) >= int(elf2[1])):
            n_contained += 1
        elif (int(elf2[0]) <= int(elf1[0])) & (int(elf2[1]) >= int(elf1[1])):
            n_contained += 1
    return n_contained

def find_overlap(pairs):
    n_overlap = 0
    for pair in pairs:
        elf_ranges = pair.split(',')
        elf1 = [int(x) for x in elf_ranges[0].split('-')]
        elf2 = [int(x) for x in elf_ranges[1].split('-')]
        if (elf1[0] <= elf2[0]) and not (elf1[1] < elf2[0]):
            n_overlap += 1
        elif (elf2[0] <= elf1[0]) and not (elf2[1] < elf1[0]):
            n_overlap += 1
    return n_overlap

test = read_file("testD4Puzzle.txt")
test_contained = find_full_containment(test)
test_overlap = find_overlap(test)

full = read_file("inputD4Puzzle.txt")
full_contained = find_full_containment(full)
full_overlap = find_overlap(full)
