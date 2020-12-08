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

def day8parser(parsed, line):
    op, num = re.split(' ', line)
    num = int(num)
    op = op.strip()
    to_be_inserted = [op, num]
    parsed.append(to_be_inserted)

def run(rom, init_acc, init_pointer):
    def do_op(op, num, acc, pointer):
        if op == 'nop':
            pointer += 1
        elif op == 'jmp':
            pointer += num
        elif op == 'acc':
            pointer += 1
            acc += num
        return [acc, pointer]
    
    visited_pointer = set()
    pointer = init_pointer
    acc = init_acc
    while True:
        visited_pointer.add(pointer)
        op, num = rom[pointer]
        acc, pointer = do_op(op, num, acc, pointer)
        if pointer in visited_pointer:
            break
    return [pointer, acc]

if __name__ == "__main__":
    parsed = get_from_stdin(day8parser)
    pointer, acc = run(parsed, 0, 0)
    print(acc)

    

