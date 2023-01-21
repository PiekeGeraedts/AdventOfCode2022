from copy import deepcopy
import math

class Position():
    def __init__(self, x, y) -> None:
        self.x=x
        self.y=y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x==other.x and self.y==other.y


class PlanckGrid():
    def __init__(self, size:int) -> None:
        self.size = size
        self.nodes = [Position(0,0) for _ in range(size)]
        self.tail_positions = [Position(0,0)]
    
    def add_tail_pos(self):
        tail = deepcopy(self.nodes[-1])
        if tail not in self.tail_positions:
            self.tail_positions.append(tail)
    
    def diff(self, pos1:Position, pos2:Position):
        return pos1.x-pos2.x, pos1.y-pos2.y

    def move_node(self, head, tail):
        diff_x, diff_y = self.diff(head, tail)
        if abs(diff_x) <= 1 and abs(diff_y) <= 1:
            # do not take a step
            pass
        elif 2 >= abs(diff_x) >= 1 and diff_y == 0:
            # take step x-direction
            tail.x += int(math.copysign(1, diff_x))
        elif diff_x == 0 and 2 >= abs(diff_y) >= 1:
            # take step y-direction
            tail.y += int(math.copysign(1, diff_y))
        elif 2 >= abs(diff_x) >= 1 and 2 >= abs(diff_y) >= 1:
            # take diagonal step
            tail.x += int(math.copysign(1, diff_x))
            tail.y += int(math.copysign(1, diff_y))
        else:
            raise Exception(f'Something in the logic isn\'t right. Difference {diff_x} and {diff_y}')

    def move_head(self, direction:str):
        head = self.nodes[0]
        if direction == 'R':
            head.y+=1
        elif direction == 'L':
            head.y-=1
        elif direction == 'U':
            head.x-=1
        elif direction == 'D':
            head.x+=1

    def moves(self, instruction:str):
        direction, n_steps = instruction.split(' ')
        for _ in range(int(n_steps)):
            self.move_head(direction.strip())
            for i in range(self.size-1):
                head=self.nodes[i]
                tail=self.nodes[i+1]
                self.move_node(head, tail)
            self.add_tail_pos()
                


def main():
    with open("data/input_day9.txt", "r") as input:
        input = input.read().splitlines()
    # input = ['R 4','U 4','L 3','D 1','R 4','D 1','L 5','R 2','D 1', 'U 2']
    # input = ['R 5','U 8','L 8','D 3','R 17','D 10','L 25','U 20']
    pg = PlanckGrid(10)
    
    for idx, instruction in enumerate(input):
        pg.moves(instruction)
    print ('Number of unique positions visited:', len(pg.tail_positions))

if __name__ == '__main__':
    main()