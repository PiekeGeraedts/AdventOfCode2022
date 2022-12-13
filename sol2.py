from itertools import permutations
from copy import deepcopy

def single_round(p1, p2, strategy):
    rock, paper, scissors = strategy
    score = 0
    if p1 == 'A':
        if p2 == rock:
            score+=4
        elif p2 == paper:
            score+=8
        elif p2 == scissors:
            score+=3
    elif p1 == 'B':
        if p2 == rock:
            score+=1
        elif p2 == paper:
            score+=5
        elif p2 == scissors:
            score+=9
    elif p1 == 'C':
        if p2 == rock:
            score+=7
        elif p2 == paper:
            score+=2
        elif p2 == scissors:
            score+=6
    return score

def single_round2(p1, p2):
    score = 0
    if p1 == 'A':
        if p2 == 'Z':
            score+=8
        elif p2 == 'Y':
            score+=4
        elif p2 == 'X':
            score+=3
    if p1 == 'B':
        if p2 == 'Z':
            score+=9
        elif p2 == 'Y':
            score+=5
        elif p2 == 'X':
            score+=1
    if p1 == 'C':
        if p2 == 'Z':
            score+=7
        elif p2 == 'Y':
            score+=6
        elif p2 == 'X':
            score+=2
    return score
        
### input ###
with open("input_day2.txt", "r") as input:
	input_lst = input.read().splitlines()

# input_lst = ['A Y', 'B X', 'C Z']

### puzzle 1 ###
max_score = 0
for strategy in permutations(['X', 'Y', 'Z']):
    result = map(lambda x: single_round(x[0], x[-1], strategy=strategy), input_lst)
    total_score = sum(result)
    if total_score > max_score:
        max_score = total_score
        best_strategy = strategy
print (max_score)
print (best_strategy)

### puzzle 2 ###
result = map(lambda x: single_round2(x[0], x[-1]), input_lst)
print (sum(result))
