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

def q6_parser(parsed, line):
    parsed.append("".join(set(line.strip())))

if __name__ == "__main__":
    puzzle = get_from_stdin(q6_parser)
    
    length_counter = 0

    for questionnaire in puzzle:
        length_counter += len(questionnaire)

    print(length_counter)