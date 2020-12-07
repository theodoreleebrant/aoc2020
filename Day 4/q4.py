import re

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

def q4_parser(parsed, line):
    temp = {}
    temp_arr = re.split(',', line.strip())
    for kv in temp_arr:
        key, value = re.split(':', kv)
        key = key.strip()
        value = value.strip()
        temp.update({key: value})
    parsed.append(temp)

if __name__ == "__main__":
    puzzle = get_from_stdin(q4_parser)
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0
    for entry in puzzle:
        temp = 1
        for key in required_keys:
            if key not in entry:
                temp = 0
                break
        if temp == 1:
            if int(entry["byr"]) < 1920 or int(entry["byr"]) > 2002:
                temp = 0
            if int(entry["iyr"]) < 2010 or int(entry["iyr"]) > 2020:
                temp = 0
            if int(entry["eyr"]) < 2020 or int(entry["eyr"]) > 2030:
                temp = 0
            if re.match('\d+cm$', entry["hgt"]):
                print(entry["hgt"][:-2])
                if int(entry["hgt"][:-2]) < 150 or int(entry["hgt"][:-2]) > 193:
                    temp = 0
            elif re.match('\d+in$', entry["hgt"]):
                if int(entry["hgt"][:-2]) < 59 or int(entry["hgt"][:-2]) > 76:
                    temp = 0
            else:
                temp = 0
            if not re.match("^#([a-f0-9]{6})$", entry["hcl"]):
                temp = 0
            if not re.match("amb|blu|brn|gry|grn|hzl|oth", entry["ecl"]):
                temp = 0
            if not re.match("^[0-9]{9}$", entry["pid"]):
                temp = 0
        res += temp
    print(res)
