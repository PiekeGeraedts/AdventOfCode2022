'''
I use deepcopy because dict is a mutable object.
Notable functions: reversed, pop
reversed - an iterable object that 'traverse' a list in the reverse direction
pop - a function returns and removes item at position -1 of the list, can also give it an index.
'''


from copy import deepcopy

def parse_starting_stacks(lst):
    n_rows = int(max(lst[-1]))
    d = {new_list: [] for new_list in range(n_rows)}
    
    for row in reversed(lst[:-1]):
        for i in range(n_rows):
            stack = row [i*4:(i+1)*4]
            if stack.strip() != '':
                d[i].append(stack.strip())
    return d


def parse_instruction(instruction):
    sub_s1 = 'move '
    sub_s2 = ' from '
    sub_s3 = ' to '
    idx1 = instruction.find(sub_s1) 
    idx2 = instruction.find(sub_s2) 
    idx3 = instruction.find(sub_s3) 
    n_move = int(instruction[idx1+len(sub_s1):idx2])
    from_stack = int(instruction[idx2+len(sub_s2):idx3]) - 1
    to_stack = int(instruction[idx3+len(sub_s3):]) - 1
    return n_move, from_stack, to_stack


def f1(instruction, d):
    n_move, from_stack, to_stack = parse_instruction(instruction)
    for _ in range(n_move):
        moving_item = d[from_stack].pop()
        d[to_stack].append(moving_item)
    return d


def f2(instruction, d):
    n_move, from_stack, to_stack = parse_instruction(instruction)
    for item in d[from_stack][-n_move:]:
        d[from_stack].pop(len(d[from_stack]) - 1 - d[from_stack][::-1].index(item))
        d[to_stack].append(item)
    return d


### input ###
with open("data/input_day5.txt", "r") as input:
	input_lst = input.read().splitlines()

idx = next((idx for idx, item in enumerate(input_lst) if item == ''))
starting_stacks = input_lst[:idx]
instructions = input_lst[idx+1:]
d = parse_starting_stacks(starting_stacks)
d2 = deepcopy(d)

### puzzle 1 ###
for instruction in instructions:
    d = f1(instruction, d)

s = ''.join(stack.pop() for stack in d.values())
print ('puzzle 1:', s.replace('[','').replace(']',''))

### puzzle 2 ###
for i, instruction in enumerate(instructions):
    d2 = f2(instruction, d2)

s = ''.join(stack.pop() for stack in d2.values())
print ('puzzle 2:', s.replace('[','').replace(']',''))