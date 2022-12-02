import csv

my_score_dict = {'X': 1, 'Y': 2, 'Z': 3}
opp_score_dict = {'A': 1, 'B': 2, 'C': 3}

def read_csv(file_path):
    round_list = []
    with open(file_path, newline='') as csvfile:
        read_file = csv.reader(csvfile, delimiter=' ')
        weight_list = []
        for row in read_file:
            round_list.append(row)  # Capture last one
    return round_list

def score_matches(round_list):
    match_scores = []
    round_score = 0
    for round in round_list:
        opp_choice = opp_score_dict[round[0]]
        my_choice = my_score_dict[round[1]]
        round_score += my_choice
        if my_choice == opp_choice:
            round_score += 3
        if opp_choice == 3:
            opp_choice = 0  # Handle case if they pick scissors
        if my_choice == (opp_choice + 1):
            round_score += 6
        match_scores.append(round_score)
        round_score = 0
    return match_scores, sum(match_scores)

def guess_what_to_choose(round_list):
    match_scores = []
    round_score = 0
    for round in round_list:
        opp_choice = opp_score_dict[round[0]]
        if round[1] == 'X':
            if opp_choice == 1:
                opp_choice = 4
            round_score += opp_choice - 1
        elif round[1] == 'Y':
            round_score += 3
            round_score += opp_choice
        elif round[1] == 'Z':
            round_score += 6
            if opp_choice == 3:
                opp_choice = 0
            round_score += opp_choice + 1
        match_scores.append(round_score)
        round_score = 0
    return match_scores, sum(match_scores)

# Part 1
test_input = read_csv('testD2Puzzle.csv')
all_scores, test_score = score_matches(test_input)

full_input = read_csv('inputD2Puzzle.csv')
full_scores, final_score = score_matches(full_input)

# Part 2
all_guesses, test_guess_total = guess_what_to_choose(test_input)

full_guesses, final_guess_total = guess_what_to_choose(full_input)
