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

def do_op(op, num, acc, pointer):
        if op == 'nop':
            pointer += 1
        elif op == 'jmp':
            pointer += num
        elif op == 'acc':
            pointer += 1
            acc += num
        return [acc, pointer]

def find_loop(rom, init_acc, init_pointer):
    visited_pointer = set()
    see_loop = set()
    pointer = init_pointer
    acc = init_acc
    last_instr_ptr = len(rom) - 1
    while pointer <= last_instr_ptr:
        visited_pointer.add(pointer)
        op, num = rom[pointer]
        acc, pointer = do_op(op, num, acc, pointer)
        if pointer in visited_pointer:
            if pointer in see_loop:
                break
            else:
                see_loop.add(pointer)
    return see_loop

def run(rom, init_acc, init_pointer):
    visited_pointer = set()
    pointer = init_pointer
    acc = init_acc
    last_instr_ptr = len(rom) - 1
    while pointer <= last_instr_ptr:
        visited_pointer.add(pointer)
        op, num = rom[pointer]
        acc, pointer = do_op(op, num, acc, pointer)
        if pointer in visited_pointer:
            break
    return [pointer, acc]

def search_with_replacement(curr_op, new_op, looping_pointers, rom, init_acc, init_pointer):
    for ptr in looping_pointers:
        if parsed[ptr][0] == curr_op:
            parsed[ptr][0] = new_op
            pointer, acc = run(rom, init_acc, init_pointer)
            if pointer >= rom_length:
                print(pointer, acc)
                parsed[ptr][0] = curr_op
                break
            else:
                parsed[ptr][0] = curr_op
        

if __name__ == "__main__":
    parsed = get_from_stdin(day8parser)
    rom_length = len(parsed)
    loop = find_loop(parsed, 0, 0)
    search_with_replacement("jmp", "nop", loop, parsed, 0, 0)
    search_with_replacement("nop", "jmp", loop, parsed, 0, 0)
            



    

