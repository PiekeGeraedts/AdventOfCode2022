'''
Used sets to solve this puzzle.
New functions used: ord, 
ord - returns an integer representing the unicode character, it is the inverse of chr
'''

def f1(rucksack):
    middle = int(len(rucksack)/2)
    compartment1 = set(rucksack[:middle])
    compartment2 = set(rucksack[middle:])
    shared_item = compartment1.intersection(compartment2).pop()

    if shared_item.islower():
        priority = ord(shared_item) - ord('a') + 1
    else:
        priority = ord(shared_item) - ord('A') + 27

    return priority

def f2(lst, sum_priorities):
    if len(lst) == 0:
        return 0, sum_priorities
    elf1_rk = set(lst[0])
    elf2_rk = set(lst[1])
    elf3_rk = set(lst[2])
    lst = lst[3:]
    shared_item = elf1_rk.intersection(elf2_rk).intersection(elf3_rk).pop()

    if shared_item.islower():
        sum_priorities += ord(shared_item) - ord('a') + 1
    else:
        sum_priorities += ord(shared_item) - ord('A') + 27

    return f2(lst, sum_priorities)

### input ###
with open("data/input_day3.txt", "r") as input:
	input_lst = input.read().splitlines()

# input_lst = ['vJrwpWtwJgWrhcsFMMfFFhFp'
#                 ,'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
#                 ,'PmmdzqPrVvPwwTWBwg'
#                 ,'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
#                 ,'ttgJtRGJQctTZtZT'
#                 ,'CrZsJsPPZsGzwwsLwLmpwMDw'
#             ]

### puzzle 1 ###
sum_priorities = 0
for rucksack in input_lst:
    sum_priorities += f1(rucksack=rucksack)
print ('Incorrect item sum of the priorities:', sum_priorities)

### puzzle 2 ### 
_, sum_priorities = f2(input_lst, 0)
print ("Three-Elf group sum of priorities:", sum_priorities)