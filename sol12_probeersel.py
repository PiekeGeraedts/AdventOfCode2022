import collections
import numpy as np

Point = collections.namedtuple('Point', 'x y')

def adjacent(coor):
    yield Point(coor.x - 1, coor.y)
    yield Point(coor.x, coor.y - 1)
    yield Point(coor.x, coor.y + 1)
    yield Point(coor.x + 1, coor.y)

def check_maze(maze):
    return 

def neighbors(maze, coor):
    for p in adjacent(coor):
        if 0 <= p.y < len(maze[0]) and 0 <= p.x < len(maze):
            if maze[p.x][p.y] <= maze[coor.x][coor.y] + 1 or maze[coor.x][coor.y] == 83:
                yield p

def solve(maze, pos, exit, current_path = None):
    if current_path is None:
        current_path = [pos]
    if pos == exit:
        # print (shortest_path_length)
        # if len(current_path) < shortest_path_length:
        #     shortest_path_length = len(current_path)
        yield current_path
    else:
        for node in neighbors(maze, pos):
            if node not in current_path:
                for result in solve(maze, node, exit, current_path + [node]):
                    yield result


def main():
    # this solution works for small mazes/graphs (test_input_day12.txt), not for the large graphs.
    with open("data/test_input_day12.txt", "r") as input:
        input = input.read()
    global shortest_path_length
    shortest_path_length = 999
    maze = input.splitlines()
    start_x = np.argmax([row.find('S') for row in maze])
    start_y = np.max([row.find('S') for row in maze])
    end_x = np.argmax([row.find('E') for row in maze])
    end_y = np.max([row.find('E') for row in maze])
    maze[end_x] = maze[end_x].replace('E', 'z')
    # print (maze)
    maze = [[ord(c) for c in row] for row in maze]
    # print (maze)
    paths = solve(maze, Point(start_x,start_y), Point(end_x,end_y), [Point(start_x,start_y)])
    print ('done generating')
    print (len([path for path in paths]))
    # shortest_path_length = len(maze)*len(maze[0])
    # print ('looping:')
    # shortest_path_length(min(len(path) for path in paths))
    # for path in paths:
    #     if len(path) < shortest_path_length:
    #         shortest_path_length = len(path)
    #         shortest_path = path

    # print (shortest_path)
    # print (shortest_path_length)

if __name__ == '__main__':
    main()