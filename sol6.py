from copy import deepcopy

### input ###
with open("data/input_day6.txt", "r") as input:
	input = input.read()

# input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
# input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
# input = 'nppdvjthqldpwncqszvftbrmjlhg'
# input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

### puzzle 1 ###
idx = 0
input1 = deepcopy(input)
while len(input1) > 0:
    s = set(input1[:4])
    if len(s) == 4:
        print ('found unique set of 4 letters:', s)
        break
    idx+=1
    input1 = input1[1:]

print ('First start-of-packer marker ends at index:', idx+4)

### puzzle 2 ###
idx = 0
input2 = deepcopy(input)
while len(input2) > 0:
    s = set(input2[:14])
    if len(s) == 14:
        print ('found unique set of 14 letters:', s)
        break
    idx+=1
    input2 = input2[1:]

print ('First start-of-message marker ends at index:', idx+14)
