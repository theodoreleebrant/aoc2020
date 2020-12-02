import re
import functools as ft

def get_from_stdin(parser):
    parsed = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "end":
            break
        parser(parsed, line)
    return parsed


def get_from_file(parser, filename):
    parsed = []
    challengeinput = open(filename)
    lines = challengeinput.readlines()
    for line in lines:
        parser(parsed, line)
    return parsed

def day2parser(parsed, line):
    # sample content """1-7 j: vrfjljjwbsv"""
    parsed_line = re.split('-|:\s|\s', line)
    parsed_line[0] = int(parsed_line[0])
    parsed_line[1] = int(parsed_line[1])
    parsed.append(parsed_line)

def validate_part1(parsed_line):
    min_val = parsed_line[0]
    max_val = parsed_line[1]
    letter = parsed_line[2]
    string = parsed_line[3]

    return bool((string.count(letter) >= min_val) and (string.count(letter) <= max_val))

def validate_part2(parsed_line):
    fst_val = parsed_line[0]
    snd_val = parsed_line[1]
    letter = parsed_line[2]
    string = parsed_line[3]

    fst_cond = bool(string[fst_val - 1] == letter)
    snd_cond = bool(string[snd_val - 1] == letter)

    return fst_cond ^ snd_cond

if __name__ == "__main__":
    parsed = get_from_stdin(day2parser)
    print(ft.reduce(lambda x, y: x + int(validate_part1(y)), parsed, 0))
    print(ft.reduce(lambda x, y: x + int(validate_part2(y)), parsed, 0))


