
import os
from pathlib import Path
from typing import List
import csv


def parse_list(input: str) -> (List[int]):
    with open(input) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        # convert each element to int
        res = []
        for line in reader:
            li = [int(i) for i in line]
            res.append(li)
        return res


def check_is_safe(l: List[int]) -> bool:
    current = None
    is_increasing = None
    for i in range(len(l)):
        if current is None:
            current = l[i]
            continue
        diff = l[i] - current
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff < 0:
            if is_increasing is None:
                is_increasing = False
            if is_increasing:
                return False
        elif diff > 0:
            if is_increasing is None:
                is_increasing = True
            if not is_increasing:
                return False
        current = l[i]
    return True

def check_is_safe_with_error(l: List[int]) -> bool:
    no_errors = check_is_safe(l)
    if no_errors:
        return True
    
    for i in range(len(l)):
        l_copy = l.copy()
        l_copy.pop(i)
        if check_is_safe(l_copy):
            return True
    return False


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    l = parse_list(dir_path + '\input.txt')
    is_safe_list = [check_is_safe(i) for i in l]
    is_safe_list_with_errors = [check_is_safe_with_error(i) for i in l]

    print(is_safe_list.count(True))
    print(is_safe_list_with_errors.count(True))

