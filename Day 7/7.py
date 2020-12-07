import re
import functools as ft

def get_from_stdin(parser):
    parsed = {}
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "end":
            break
        parser(parsed, line)
    return parsed

def day7parser(parsed, line):
    inside_dict = {}
    outside_bag, inside_list = re.split(',', line, 1)
    outside_bag = outside_bag[1:] # remove the bracket
    inside_list = inside_list.strip()[1:-2]
    inside_bags = re.split(',', inside_list)
    length = len(inside_bags)
    i = 0
    while (i < length):
        if inside_bags[0].strip() == "no other":
            parsed.update({outside_bag: {}})
            break
        key = inside_bags[i + 1].strip()
        value = int(inside_bags[i])
        inside_dict.update({key: value})
        i += 2
    tuple_to_be_put = {outside_bag : inside_dict}
    parsed.update(tuple_to_be_put)

# def find(color, result_set, parsed):
#     for (outside, inside) in parsed:
#         if outside in result_set:
#             continue
#         elif color in inside:
#             result_set.add(outside)
#             find(outside, result_set, parsed)

def find_in(color, parsed, multiplicity):
    count = 0
    x = parsed.get(color)
    for key, val in x.items():
        count += val * find_in(key, parsed, val)
    return 1 + count

if __name__ == "__main__":
    parsed = get_from_stdin(day7parser)
    # result_set = set()
    # find("shiny gold", result_set, parsed)
    # print(len(result_set))
    x = find_in("shiny gold", parsed, 1) - 1
    print(x)

