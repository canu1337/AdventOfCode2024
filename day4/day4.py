from enum import Enum
import os
from typing import List

Direction = Enum('Direction', 'up down left right upleft upright downleft downright')
next_letter_dict = {'X': 'M', 'M': 'A', 'A': 'S', 'S': 'W'}

array: List[str] = []  # Initialize the array variable

def parse(input: str) -> list:
    rows = input.strip().split('\n')
    array = [list(row) for row in rows]
    return array


def get_from_array(i :int, j: int) -> chr:
    try:
        if i < 0 or j < 0:
            return 'E'
        return array[i][j]
    except IndexError as e:
        return 'E'        

def check_for_next_letter(i: int, j: int, char_to_search: chr, direction: Direction) -> int:
    
    actual_char = get_from_array(i, j) 
    if  actual_char != char_to_search:
        return 0
    if j < 0:
        a = 'aa'
    # we reached end of word
    if char_to_search == 'S':
        print('i ' + str(i) + 'j ' + str(j))
        return 1


    next_i = i
    next_j = j
    if direction == Direction.left:
        next_i = i - 1
    elif direction == Direction.right:
        next_i = i + 1
    elif direction == Direction.up:
        next_j = j - 1
    elif direction == Direction.down:
        next_j = j + 1
    elif direction == Direction.upleft:
        next_i = i - 1
        next_j = j - 1
    elif direction == Direction.upright:
        next_i = i + 1
        next_j = j - 1
    elif direction == Direction.downleft:
        next_i = i - 1
        next_j = j + 1
    elif direction == Direction.downright:
        next_i = i + 1
        next_j = j + 1
    
    return check_for_next_letter(next_i, next_j, next_letter_dict[char_to_search], direction)


def check_for_xmas(i: chr, j: chr) -> int:
    res = 0
    res += check_for_next_letter(i - 1, j, 'M', Direction.left)
    res += check_for_next_letter(i + 1, j, 'M', Direction.right)
    res += check_for_next_letter(i, j - 1, 'M', Direction.up)
    res += check_for_next_letter(i, j + 1, 'M', Direction.down)
    res += check_for_next_letter(i - 1, j - 1, 'M', Direction.upleft)
    res += check_for_next_letter(i + 1, j - 1, 'M', Direction.upright)
    res += check_for_next_letter(i - 1, j + 1, 'M', Direction.downleft)
    res += check_for_next_letter(i + 1, j + 1, 'M', Direction.downright)

    return res

def part1(input: str) -> int:
    global array
    array = parse(input)
    res = 0
    for j, row in enumerate(array):
        for i, char in enumerate(row):
            if char == 'X':
                res += check_for_xmas(j, i)
    return res

def check_for_xmas_2(i: chr, j: chr) -> int:
    res = 0
    upleft = get_from_array(i -1, j - 1)
    downright = get_from_array(i + 1, j + 1)
    upright = get_from_array(i + 1, j - 1)
    downleft = get_from_array(i - 1, j + 1)

    if (upleft == 'M' and downright == 'S') or (upleft == 'S' and downright == 'M'):
        res += 1

    if (upright == 'M' and downleft == 'S') or (upright == 'S' and downleft == 'M'):
        res += 1
    return 1 if res == 2 else 0

def part2(input: str) -> int:
    global array
    array = parse(input)
    res = 0
    for j, row in enumerate(array):
        for i, char in enumerate(row):
            if char == 'A':
                res += check_for_xmas_2(j, i)
    return res


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/input.txt', 'r') as file:
        input = file.read()
        # print(part1(input))
        print(part2(input))