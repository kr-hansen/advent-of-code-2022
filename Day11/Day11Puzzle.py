from typing import Callable, List, Optional
import math
import operator

def read_file(file_path):
    round_list = []
    with open(file_path, "r", newline='\n') as fn:
        return fn.read().splitlines()

class monkey:
    def __init__(self,
        start_items: List = None,
        operation: Callable = None,
        test: Callable = None,
        true_throw: "monkey" = None,
        false_throw: "monkey" = None
    ):
        if start_items is None:
            start_items = []
        self.items = start_items
        self.operation = operation
        self.test = test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.nitems = 0
        self.test_val = None
    def take_turn(self):
        for item in self.items:
            inspected = self.operation(item)
            new_item = inspected // 3
            if self.test(new_item):
                true_throw.add_item(new_item)
            else:
                false_throw.add_item(new_item)
        items = []
    def add_item(self, item):
        self.items.append(item)
    def sum_items(self):
        self.nitems += len(self.items)


def initialize_monkeys(input_list):
    init_monkeys = {}
    for r in input_list:
        r_vals = r.split(' ')
        if r_vals[0] == 'Monkey':
            mnky = int(r_vals[1].strip(':'))
            init_monkeys[mnky] = monkey()
    mnky = None
    for row in input_list:
        row_vals = row.split(' ')
        if row_vals[0] == 'Monkey':
            mnky = int(row_vals[1].strip(':'))
        elif 'Starting items' in row:
            list_start = row_vals.index('items:')
            for idx in range(list_start+1, len(row_vals)):
                itm = int(row_vals[idx].strip(','))
                init_monkeys[mnky].add_item(itm)
        elif 'Operation' in row:
            fn_start = row_vals.index('=')
            func_string = ''
            for idx in range(fn_start+1, len(row_vals)):
                func_string += row_vals[idx]
            init_monkeys[mnky].operation = eval(f"lambda old: {func_string}")
        elif 'Test' in row:
            div_by = int(row_vals[-1])
            init_monkeys[mnky].test = eval(f"lambda x: not bool(x % {div_by})")
            init_monkeys[mnky].test_val = div_by
        elif 'true:' in row:
            init_monkeys[mnky].true_throw = init_monkeys[int(row_vals[-1])]
        elif 'false:' in row:
            init_monkeys[mnky].false_throw = init_monkeys[int(row_vals[-1])]
        else:
            continue
    return init_monkeys

def monkey_rounds(monkey_dict, nrounds=20, worry_div=3, big_numbers=None):
    if worry_div is None:
        test_list = [x.test_val for x in monkey_dict.values()]
        big_div = math.prod(test_list)
    for turn in range(nrounds):
        if turn % 100 == 0:
            print(f"Current turn is: {turn}")
        for mnky in monkey_dict.keys():
            monkey_dict[mnky].sum_items()
            for item in monkey_dict[mnky].items:
                post_inspection = monkey_dict[mnky].operation(item)
                if not big_numbers:
                    decrease_worry = post_inspection // worry_div
                elif big_numbers:
                    decrease_worry = post_inspection % big_div
                if monkey_dict[mnky].test(decrease_worry):
                    monkey_dict[mnky].true_throw.add_item(decrease_worry)
                else:
                    monkey_dict[mnky].false_throw.add_item(decrease_worry)
            monkey_dict[mnky].items = []
    return monkey_dict

def calc_monkey_business(monkey_dict):
    monkey_vals = []
    for mnky in monkey_dict.keys():
        monkey_vals.append(monkey_dict[mnky].nitems)
    sort_idx = [i[0] for i in sorted(enumerate(monkey_vals), reverse=True, key=lambda x:x[1])]
    business = 1
    for big_monkey in sort_idx[:2]:
        business *= monkey_dict[big_monkey].nitems
    return business

test = read_file("testD11Puzzle.txt")
test_initialized_monkeys = initialize_monkeys(test)
test_monkeys = monkey_rounds(test_initialized_monkeys, nrounds=20)
test_monkey_business = calc_monkey_business(test_monkeys)
test_worry_monkeys = monkey_rounds(test_initialized_monkeys, nrounds=10000, worry_div=None, big_numbers=True)
test_worry_business = calc_monkey_business(test_worry_monkeys)


full = read_file("inputD11Puzzle.txt")
full_initialized_monkeys = initialize_monkeys(full)
full_monkeys = monkey_rounds(full_initialized_monkeys, nrounds=20)
full_monkey_business = calc_monkey_business(full_monkeys)
full_worry_monkeys = monkey_rounds(full_initialized_monkeys, nrounds=10000, worry_div=None, big_numbers=True)
full_worry_business = calc_monkey_business(full_worry_monkeys)
