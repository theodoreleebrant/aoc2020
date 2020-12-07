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

def q3_parser(parsed, line):
    parsed.append(line.strip())

def get_new_x(curr, step, wrap):
    return ((curr + step) % wrap)

def get_count(dx, dy, puzzle):
    x = 0
    y = 0
    wrap = len(puzzle[0])
    counter = 0

    length = len(puzzle)

    while (y < length - 1):
        y += dy
        x = get_new_x(x, dx, wrap)
        if puzzle[y][x] == "#":
            counter += 1
    
    return counter

if __name__ == "__main__":
    puzzle = get_from_stdin(q3_parser)
    print(get_count(3, 1, puzzle) * get_count(1, 1, puzzle) * get_count(5, 1, puzzle) * get_count(7, 1, puzzle) * get_count(1, 2, puzzle))
    

    
            
        
