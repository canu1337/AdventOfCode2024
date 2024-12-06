
import os
from pathlib import Path
from typing import List


class Rule:
    def __init__(self, page1: int, page2: int):
        self.page1 = page1
        self.page2 = page2


def parse_list(input: str) -> tuple[List[Rule], List[List[int]]]:
    rules = []
    updates = []
    with open(input) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if '|' in line:
                parts = line.split('|')
                rules.append(Rule(parts[0], parts[1]))
            elif ',' in line:
                parts = line.split(',')
                updates.append(parts)
        return (rules, updates)


def check_rule(rule: Rule, update: List[int]) -> bool:
    if rule.page1 not in update or rule.page2 not in update:
        return True

    page_1_index = update.index(rule.page1)
    page_2_index = update.index(rule.page2)

    return True if page_1_index < page_2_index else False


def get_middle(update: List[int], rules: List[Rule]) -> int:
    for page in update:
        nb_before = 0
        nb_after = 0
        for rule in rules:
            if rule.page1 == page and rule.page2 in update:
                nb_after += 1
            if rule.page2 == page and rule.page1 in update:
                nb_before += 1
        if nb_before == nb_after:
            return int(page)
    raise Exception


def part1(rules: List[Rule], updates: List[List[int]]) -> int:
    res = 0
    for update in updates:
        is_update_ok = True
        for rule in rules:
            is_ok = check_rule(rule, update)
            if not is_ok:
                is_update_ok = False
                break
        if is_update_ok:
            res += int(update[int(len(update) / 2)])
    return res


def part2(rules: List[Rule], updates: List[List[int]]) -> int:
    res = 0
    for update in updates:
        is_update_ok = True
        for rule in rules:
            is_update_ok = is_update_ok and check_rule(rule, update)
        if is_update_ok:
            continue
        middle = get_middle(update, rules)
        res += middle
    return res


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    rules, updates = parse_list(dir_path + '/input.txt')

    # print(part1(rules, updates))
    print(part2(rules, updates))