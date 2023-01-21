import numpy as np

class Position():
    def __init__(self, x, y) -> None:
        self.x=x
        self.y=y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x==other.x and self.y==other.y

class State():
    def __init__(self):
        self.n_cycle = 0
        self.x_register = 1
        self.crt_loc = Position(0,0)
        self.crt_image = np.empty((6,40), 'str')
        self.signal_strengths = []
        self.check_points = [20+40*i for i in range(6)]
    
    def check_state(self):
        if self.n_cycle in self.check_points:
            self.signal_strengths.append(self.n_cycle*self.x_register)

    def crt_draw(self):
        # print (self.x_register)
        if self.crt_loc.y in [self.x_register-1, self.x_register, self.x_register+1]:
            self.crt_image[self.crt_loc.x,self.crt_loc.y] = '#'
        else:
            self.crt_image[self.crt_loc.x,self.crt_loc.y] = '.'
        # print (self.crt_image[self.crt_loc.x,self.crt_loc.y])
        if self.crt_loc.y == 39:
            self.crt_loc.x+=1
            self.crt_loc.y=0
        else:
            self.crt_loc.y+=1
        # print (self.crt_loc)
        # print ('-----')



def f1(input):
    S = State()
    for signal in input:
        if signal.strip() == 'noop':
            S.n_cycle+=1
            S.check_state()
        else:
            v = int(signal.split(' ')[-1])
            S.n_cycle+=1
            S.check_state()
            S.n_cycle+=1
            S.check_state()
            S.x_register+=v
    print ('================ Puzzle 1 ================ ')
    print ('Signal strength checking points:', S.check_points)
    print ('Signal strengths:', S.signal_strengths)
    print ('Sum of signal strengths:', sum(S.signal_strengths))

def f2(input):
    S = State()
    for idx, signal in enumerate(input):
        if signal.strip() == 'noop':
            S.n_cycle+=1
            S.crt_draw()
        else:
            v = int(signal.split(' ')[-1])
            S.n_cycle+=1
            S.crt_draw()
            S.n_cycle+=1
            S.crt_draw()
            S.x_register+=v

    print ('================ Puzzle 2 ================ ')
    for i in range(6):
        print (''.join(S.crt_image[i,:]))

def main():
    with open("data/input_day10.txt", "r") as input:
        input = input.read().splitlines()

    f1(input)
    f2(input)
    
    
if __name__ == '__main__':
    main()