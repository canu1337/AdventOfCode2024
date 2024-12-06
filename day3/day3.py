import string
import os
import re

def part1(input: string) -> int:
    regex = re.compile('mul\((\d{1,3}),(\d{1,3})\)')
    matches = regex.findall(input)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result


def part2(input: string) -> int:
    regex_mul = re.compile('mul\((\d{1,3}),(\d{1,3})\)')
    regex_do = re.compile('do\(\)')
    regex_dont = re.compile('don\'t\(\)')
    indices_mul = re.finditer(regex_mul, input)
    indices_do = [(m.start(0), m.end(0)) for m in re.finditer(regex_do, input)]
    indices_dont = [(m.start(0), m.end(0)) for m in re.finditer(regex_dont, input)]

    result = 0
    for match in indices_mul:
        groups = match.groups()
        start = match.start()
        closest_do_index = max([start_do for i, (start_do, end_do) in enumerate(indices_do) if start_do < start], default=-1)
        closest_dont_index = max([start_dont for i, (start_dont, end_dont) in enumerate(indices_dont) if start_dont < start], default=-1)
        if closest_do_index > closest_dont_index:
            result += int(groups[0]) * int(groups[1])
    return result



if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/input.txt', 'r') as file:
        input = file.read()
        print(part1(input))
        print(part2(input))