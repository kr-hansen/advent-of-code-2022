import csv

test_input = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

def find_elf_with_most_calories(carry_weights):
    sums = [sum(x) for x in carry_weights]
    max_weight = max(sums)
    return max_weight, sums.index(max_weight) + 1  # Account for 1 index in answer

def read_csv(file_path):
    elf_list = []
    with open(file_path, newline='') as csvfile:
        read_file = csv.reader(csvfile, delimiter=' ')
        weight_list = []
        for row in read_file:
            if not row:
                elf_list.append(weight_list)
                weight_list = []
            else:
                weight_list.extend([int(cal) for cal in row])
        elf_list.append(weight_list)  # Capture last one
    return elf_list

def find_top_n_calories(carry_weights, n=3):
    sums = [sum(x) for x in carry_weights]
    sorted_sums = sorted(sums, reverse=True)
    return sum(sorted_sums[:n])

full_input = read_csv("inputD1Puzzle1.csv")
weight, elf = find_elf_with_most_calories(full_input)
top3weight = find_top_n_calories(full_input, n=3)
