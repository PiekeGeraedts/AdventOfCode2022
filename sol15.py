import re 
import time

class Piont():
    '''
    Point class to capture coordinate in 2d grid.
    '''
    def __init__(self, x, y) -> None:
        self.x=x
        self.y=y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x==other.x and self.y==other.y

    def distance(self, p) -> int:
        '''
        Calculate (walking) distance between two points in a grid. How many steps left and right are they apart?
        '''
        return abs(self.x-p.x) + abs(self.y-p.y)

class Sensor():
    '''
    Sensor class. Has information on x and y coordinates of sensor and closest beacon.
    '''
    def __init__(self, sensor_p: Piont, beacon_p: Piont):
        self.sensor_p = sensor_p
        self.coverage_x = abs(sensor_p.x - beacon_p.x)
        self.coverage_y = abs(sensor_p.y - beacon_p.y)
        self.dist = sensor_p.distance(beacon_p)

    def __repr__(self) -> str:
        return f"Sensor has coordinate {self.sensor_p} and nearest beacon at distance {self.dist}."

    def coverage(self, y):
        '''
        Method to determine coverage of sensor over row y.
        y - int, a row.
        '''
        y_distance = abs(self.sensor_p.y - y)
        if y_distance > self.dist:
            return 0
        else:
            return (self.dist-y_distance)

    def coverage_range(self, y):
        c = self.coverage(y)
        min_x = self.sensor_p.x-c
        max_x = self.sensor_p.x+c
        return set(range(min_x, max_x))

    def coverage_range_2(self, y):
        c = self.coverage(y)
        min_x = max(0, self.sensor_p.x-c)
        max_x = min(20, self.sensor_p.x+c)
        return set(range(min_x, max_x))

def tuning_frequency(p: Piont) -> int:
    return p.x*4000000 + p.y

def read_sensor_info(data):
    '''
    Find sensor and beacon location looking for x,y in string.
    data - list of lines with sensor and beacon coordinates
    '''
    sensors = []
    beacons = []
    # Use regex to find all integers (negative and positive)
    coordinates = map(lambda x: list(map(int, re.findall(r'-?\d+', x))), data)
    for c in coordinates:
        sensor, beacon = Piont(x=c[0], y=c[1]), Piont(x=c[2], y=c[3])
        sensors.append(Sensor(sensor, beacon))
    return sensors

def main():
    # Magic number
    y = 2000000
    t = time.time()

    # Read input
    with open("data/test_input_day15.txt", "r") as input:
        data = input.read().splitlines()
    sensors = read_sensor_info(data)
    print ('time spent reading info and creating classes:', time.time()-t)

    # Part 1 - Find coverage for row y
    # master_set = set()
    # sets = []
    # for sensor in sensors:
    #     sets.append(sensor.coverage_range(y))
    #     # master_set = master_set.union(sensor.coverage_range(y))

    # print (len(sets))
    # print (len(master_set))
    # print ('elapsed time:', time.time()-t)

    # Part 2 - Find beacon
    sets = []
    for sensor in sensors:
        sets.append(sensor.coverage_range_2(y))

if __name__ == '__main__':
    main()