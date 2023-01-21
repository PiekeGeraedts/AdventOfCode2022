# class Item:
#     def __init__(self, items:list, operation:str, n_div:str, m_idx_true:int, m_idx_false:int):

class Monkey:
    def __init__(self, items:list, operation:str, n_div:str, m_idx_true:int, m_idx_false:int):
        self.items=items
        self.operation=operation
        self.n_div=n_div
        self.m_idx_true=m_idx_true
        self.m_idx_false=m_idx_false
        self.inspected_items=0

    def f_operation(self, val):
        op = self.operation.split('new =')[-1].strip().replace('old', str(val))
        return eval(op)

    def f_test(self, val):
        # print (val)
        # print (val % self.n_div)
        # if (val / self.n_div).is_integer():
        if val % self.n_div == 0:
            return self.m_idx_true
        else:
            return self.m_idx_false

    def __repr__(self) -> str:
        return f'items: {self.items}, inspected items: {self.inspected_items}'


def get_monkeys_state(input):
    n_monkeys = int((len(input)+1)/7)
    monkey_lst = []
    for i in range(n_monkeys):
        starting_items = [item.strip() for item in input[i*7+1].split(':')[-1].split(',')]
        operation = input[i*7+2].split('new =')[-1].strip()
        n_div = int(input[i*7+3].split('divisible by')[-1].strip())
        m_idx_true = int(input[i*7+4].split('throw to monkey')[-1].strip())
        m_idx_false = int(input[i*7+5].split('throw to monkey')[-1].strip())
        m = Monkey(starting_items, operation, n_div, m_idx_true, m_idx_false)
        monkey_lst.append(m)
    return monkey_lst

def one_round(j, monkey_lst):
    monkey = monkey_lst[j]
    while len(monkey.items) > 0:
        item = monkey.items.pop(0)
        monkey.inspected_items+=1
        # print ('monkey has item with worry level:', item)
        item = monkey.f_operation(item) # monkey has item, worry level increases
        item = int(item/3) # monkey gets bored, worry level decreases
        # print ('new worry level:', item)
        next_mnky_idx = monkey.f_test(item) # check next monkey
        # print ('Next monkey:', next_mnky_idx)
        # print (monkey_lst[next_mnky_idx])
        monkey_lst[next_mnky_idx].items.append(item)
        # print (monkey_lst[next_mnky_idx])
    return monkey_lst

def f1(input):
    # 31578 is too low
    monkey_lst = get_monkeys_state(input)
    for i in range(200):
        for j in range(len(monkey_lst)):
            monkey_lst = one_round(j, monkey_lst)
        print (i)
    lst_interests = [monkey.inspected_items for monkey in monkey_lst]
    max_interest = max(lst_interests)
    lst_interests.pop(lst_interests.index(max_interest))
    second_max_interest = max(lst_interests)
    print ('================ Puzzle 1 ================ ')
    print (monkey_lst)
    print (max_interest * second_max_interest)


def f2(input):
    pass


def main():
    with open("test_input_day11.txt", "r") as input:
        input = input.read().splitlines()

    f1(input)
    f2(input)

if __name__ == '__main__':
    main()