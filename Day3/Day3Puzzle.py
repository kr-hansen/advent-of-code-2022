import csv
from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

lower_scores = {letter: val for letter, val in zip(alc, range(1, 27))}
upper_scores = {letter: val for letter, val in zip(auc, range(27, 53))}
score_dict = lower_scores | upper_scores

def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

def count_rucksack(item_list):
    scores = []
    for sack in item_list:
        n_items = len(sack)
        div_idx = int(n_items/2)
        item_type = list(set(sack[:div_idx]).intersection(sack[div_idx:]))[0]
        scores.append(score_dict[item_type])
    return sum(scores), scores

def find_elf_groups(item_list, n_elves=3):
    scores = []
    for idx in range(0, len(item_list), n_elves):
        item_type = list(set(item_list[idx]).intersection(item_list[idx+1]).intersection(item_list[idx+2]))[0]
        scores.append(score_dict[item_type])
    return sum(scores), scores

test = read_file("testD3Puzzle.txt")
test_score, test_list = count_rucksack(test)
test_group_score, test_group_list = find_elf_groups(test)

question1 = read_file("inputD3Puzzle.txt")
q1_score, q1_list = count_rucksack(question1)
group_score, group_list = find_elf_groups(question1)
