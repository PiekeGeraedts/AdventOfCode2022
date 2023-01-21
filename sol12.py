import numpy as np
import collections

Point = collections.namedtuple('Point', 'x y')

class Graph():
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def minDistance(self, dist, sptSet):
        # Initialize minimum distance for next node
        min = 1e12
 
        # Search not nearest vertex not in the shortest path tree
        try:
            for v in range(self.V):
                if dist[v] < min and sptSet[v] == False:
                    min = dist[v]
                    min_index = v
            return min_index
        except:
            for v in range(self.V):
                if dist[v] < min and sptSet[v] == False:
                    min = dist[v]
                    min_index = v
            assert False, f"{min}"

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

def adjacent(coor):
    yield Point(coor.x - 1, coor.y)
    yield Point(coor.x, coor.y - 1)
    yield Point(coor.x, coor.y + 1)
    yield Point(coor.x + 1, coor.y)

def create_weighted_graph(data):
    shape = (len(data), len(data[0]))
    G = Graph(shape[0]*shape[1]) 
    for x in range(shape[0]):
        for y in range(shape[1]):
            for p in adjacent(Point(x,y)):
                if 0 <= p.x < shape[0] and 0 <= p.y < shape[1]:
                    if data[p.x][p.y] <= data[x][y] + 1 or data[x][y] == 83:
                        G.graph[x*shape[1] + y][p.x*shape[1]+p.y] = 1
                    else:
                        G.graph[x*shape[1] + y][p.x*shape[1]+p.y] = 0 
    return G


def f1(data, src, target):
    data = [[ord(c) for c in row] for row in data]
    G = create_weighted_graph(data)
    sol = G.dijkstra(src)
    print (sol[target])

def f2(data, src, target):
    data = [[ord(c) for c in row] for row in data]
    G = create_weighted_graph(data)
    min_path = 10e7
    for src in range(G.V):
        print (src, '/', G.V)
        x = int(src / len(data[0]))
        y = src % len(data[0])
        if data[x][y] == ord('a'):
            if min_path > G.dijkstra(src)[target]:
                min_path = G.dijkstra(src)[target]
    print (min_path)


def main():
    with open("data/input_day12.txt", "r") as input:
        data = input.read().splitlines()
        
        # find source and target node
        src_x = np.argmax([row.find('S') for row in data])
        src_y = np.max([row.find('S') for row in data])
        target_x = np.argmax([row.find('E') for row in data])
        target_y = np.max([row.find('E') for row in data])
        data[target_x] = data[target_x].replace('E', 'z')
        src = src_x*len(data[0]) + src_y
        target = target_x*len(data[0]) + target_y
        f1(data, src, target) 
        f2(data, src, target) # solution is 386, but this took way too long.


if __name__ == '__main__':
    main()