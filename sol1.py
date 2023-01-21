'''
I used recursion (wanted to try it again) to solve the puzzle. I learnt how the next() method for iterators work.
The next function returns the next item in an iterator object, e.g., next(i for i in [1,2,3]) returns 1.
'''

def f1(lst, max_calories):
	# stop condition
	if len(lst) == 0:
		return [], max_calories
	# find elf's items
	print (lst)
	elf_items_idx = next((idx for idx, item in enumerate(lst) if item == ''), 1)
	elf_items = [int(i) for i in lst[:elf_items_idx]]
	print (elf_items)
	# remaining items
	lst = lst[elf_items_idx+1:]
	# update max
	if sum(elf_items) > max_calories:
		max_calories = sum(elf_items)
	return f1(lst, max_calories)


def f2(lst, sum_lst):
	if len(lst) == 0:
		return [], sorted(sum_lst)
	elf_items_idx = next((idx for idx, item in enumerate(lst) if item == ''), 1)
	elf_items = [int(i) for i in lst[:elf_items_idx]]
	lst = lst[elf_items_idx+1:]
	sum_lst.append(sum(elf_items))
	return f2(lst, sum_lst)


with open("data/input_day1.txt", "r") as input:
	input_lst = input.read().splitlines()

# Level 1 solution
_, max_calories = f1(input_lst, 0)
print (max_calories)	

# Level 2 solution
_, sum_lst = f2(input_lst, [])
print ('Most calories:', sum_lst[-1])
print ('Second most calories:', sum_lst[-2])
print ('Third most calories:', sum_lst[-3])

print ('Total Calories:', sum_lst[-1] + sum_lst[-2] + sum_lst[-3])

