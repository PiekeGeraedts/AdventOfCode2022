def f1(asgnmt1, asgnmt2):
    n1, n2 = asgnmt1.split('-')
    set1 = set(range(int(n1), int(n2)+1))
    n1, n2 = asgnmt2.split('-')
    set2 = set(range(int(n1), int(n2)+1))

    if (set1 <= set2) or (set2 <= set1):
        return 1
    else:
        return 0

def f2(asgnmt1, asgnmt2):
    n1, n2 = asgnmt1.split('-')
    set1 = set(range(int(n1), int(n2)+1))
    n1, n2 = asgnmt2.split('-')
    set2 = set(range(int(n1), int(n2)+1))

    if len(set1.intersection(set2)) == 0:
        return 0
    else:
        return 1

### input ###
with open("input_day4.txt", "r") as input:
	input_lst = input.read().splitlines()

# input_lst = ['2-4,6-8' 
#                 ,'2-3,4-5'
#                 ,'5-7,7-9'
#                 ,'2-8,3-7'
#                 ,'6-6,4-6'
#                 ,'2-6,4-8'
#             ]

### puzzle 1 and 2 ###
cnt1 = 0
cnt2 = 0
for elf_pair in input_lst:
    asgnmt1, asgnmt2 = elf_pair.split(',')
    cnt1+= f1 (asgnmt1, asgnmt2)
    cnt2+= f2 (asgnmt1, asgnmt2)

print ('Assignment fully contained in elf pair:', cnt1)
print ('Assignment overlapping in elf pair:', cnt2)


