import re
import scrib
import os
from collections import namedtuple
import time


def manhattan_distance(p1,p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def part1(input,row):
    with open(input) as f:
        input_lines = f.read().splitlines()


    Point = namedtuple("Point", "x y")

    items = []
    for l in input_lines:
        (a,b) = l.split(": ")
        (s_x,s_y) = (scrib.find_int(a.split(",")[0]),scrib.find_int(a.split(",")[1]))
        sensor = Point(s_x,s_y)
        (b_x,b_y) = (scrib.find_int(b.split(",")[0]),scrib.find_int(b.split(",")[1]))
        beacon = Point(b_x,b_y)
        items.append((sensor,beacon))

    start = time.time()
    row_points = []
    row_range = []
    for item in items:
        sensor = item[0]
        beacon = item[1]
        distance = manhattan_distance(sensor,beacon)
        if sensor.y + distance >= row >= sensor.y - distance:
            d_row = manhattan_distance(sensor,Point(sensor.x,row))
            row_range.append((Point(sensor.x-(distance-d_row),row),Point(sensor.x+(distance-d_row)+1,row)))

    row_points = list(set(row_points))

    count = 0
    points = {}
    for point in row_range:
        for x in range(point[0].x,point[1].x):
            points[x] = 1

    for item in items:
        if item[1].y == row:
            points[item[1].x] = 0
            # print("there is a beacon {}".format(item[1]))

    print(sum(points.values()))
    # part 1 38m - 5511201

    print("Elapsed {}".format(time.time() - start))


def get_item(items,k):
    for i in items:
        if i[0].x == k.x and i[0].y == k.y:
            return "S"
        elif i[1].x == k.x and i[1].y == k.y:
            return "B"

    return ""


def part2(input,size):
    with open(input) as f:
        input_lines = f.read().splitlines()


    Point = namedtuple("Point", "x y")

    items = []
    for l in input_lines:
        (a,b) = l.split(": ")
        (s_x,s_y) = (scrib.find_int(a.split(",")[0]),scrib.find_int(a.split(",")[1]))
        sensor = Point(s_x,s_y)
        (b_x,b_y) = (scrib.find_int(b.split(",")[0]),scrib.find_int(b.split(",")[1]))
        beacon = Point(b_x,b_y)
        items.append((sensor,beacon))

    start = time.time()

    rows_range = []
    points = {}

    print("Calculating items")
    for item in items:
        sensor = item[0]
        beacon = item[1]
        # print("Sensor {}, Beacon {}".format(sensor, beacon))
        print(".",end="")
        distance = manhattan_distance(sensor, beacon)

        for row_index in range(size+1):
            if len(rows_range)<=row_index:
                rows_range.append([])
            if sensor.y + distance >= row_index >= sensor.y - distance:
                d_row = distance - manhattan_distance(sensor,Point(sensor.x,row_index))
                rows_range[row_index].append((Point(sensor.x-d_row,row_index),Point(sensor.x+d_row+1,row_index)))

    print("Calculating coverage")

    uncovered = []
    for row,row_range in enumerate(rows_range):
        possible_x_values = [point[0].x - 1 for point in row_range]
        possible_x_values.extend([point[1].x for point in row_range])
        possible_x_values = list(filter(lambda x: 0 <= x <= size, possible_x_values))

        for possible_x in possible_x_values:
            covered = False
            for point1 in row_range:
                if point1[0].x <= possible_x < point1[1].x:
                    covered = True
            if not covered:
                uncovered.append(Point(possible_x, row))
    uncovered = list(set(uncovered))
    print(uncovered)
    print(uncovered[0].x*4000000+uncovered[0].y)

    # solution = set([k if not points[k] else (-1,-1) for k in points.keys()])
    # solution.remove((-1,-1))
    # print(solution)
    # part 1 38m - 5511201

    print("Elapsed {}".format(time.time() - start))



if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    row = 2000000
    size = 4000000

    # size = 20
    # row = 10
    # input_file = "./data/" + d + "_test.txt"

    part1(input_file,row)
    part2(input_file,size)
    # part two is search from 0 to 4 000 000

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
