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
    parsed.append(int(line.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2))

if __name__ == "__main__":
    puzzle = get_from_stdin(q4_parser)
    print("Minimum value: " + str(min(puzzle)))
    print("Maximum value: " + str(max(puzzle)))
    
    i = min(puzzle)
    j = max(puzzle)
    while (i < j):
        if i not in puzzle:
            print(i)
        i += 1