import ast

class orderedList():
    def __init__(self, data: list, pointer: int):
        self.data = data
        self.pointer = pointer

    def move_min(self, min_pointer):
        assert min_pointer >= self.pointer, 'something went wrong'
        self.data.insert(self.pointer, self.data[min_pointer])
        self.data.pop(min_pointer+1)
        self.pointer +=1

def convert_to_list(s):
    return ast.literal_eval(s)

def check_items(l, r):
    if type(l) is int and type(r) is int:
        if l == r:
            return None
        return l < r 
    elif type(l) is list and type(r) is list:
        return compare(l,r)
    elif type(l) is list:
        return compare(l,[r])
    elif type(r) is list:
        return compare([l],r)
    else:
        assert False, "Shouldn't happen"

def compare(left, right):
    # if left and right empty stop return True
    if len(left) + len(right) == 0:
        return None
    elif len(left) == 0:
        return True
    elif len(right) == 0:
        return False
    # compare left and right items
    left_item = left.pop(0)
    right_item = right.pop(0)
    b = check_items(left_item, right_item)
    
    if b is not None:
        return b
    else:
        return compare(left, right)

def f1(data):
    correct_pairs = []
    for idx, pair in enumerate(data):
        left, right = pair.split('\n')
        left = convert_to_list(left)
        right = convert_to_list(right)
        result = compare(left, right)
        if result:
            correct_pairs.append(idx+1)
    print (correct_pairs)
    print (len(correct_pairs))
    print (sum(correct_pairs))

        
def find_minimum(ord_list: orderedList):
    min_pointer = ord_list.pointer
    for i in range(ord_list.pointer, len(ord_list.data)):
        left = convert_to_list(ord_list.data[min_pointer])
        right = convert_to_list(ord_list.data[i])
        if compare(left, right) == False:
            min_pointer = i
    return min_pointer

    # for i in range(len(ord_list.data)-1):
    #     left = convert_to_list(ord_list.data[i])
    #     right = convert_to_list(ord_list.data[i+1])
    #     result = compare(left, right)
    #     if 
    # return -1, i

def f2(data):
    ord_list = orderedList(data=data, pointer=0)
    ord_list.data.append('[[2]]')
    ord_list.data.append('[[6]]')
    for i in range(len(data)):
        ord_list.move_min(find_minimum(ord_list))
        # print ('==============')
        # print (ord_list.data)

    idx2 = ord_list.data.index('[[2]]') + 1
    idx6 = ord_list.data.index('[[6]]') + 1
    print (idx2, idx6, idx2*idx6)


def main():
    with open("input_day13.txt", "r") as input:
        data = input.read()
        
    # f1(data.split("\n\n"))
    f2(data.replace("\n\n", "\n").splitlines())

        

if __name__ == '__main__':
    main()