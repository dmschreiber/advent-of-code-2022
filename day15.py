import re
import scrib
import os
from collections import namedtuple

def manhattan_distance(p1,p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def part1(input,row):
    with open(input) as f:
        input_lines = f.read().splitlines()


    count = 0
    items = []
    Point = namedtuple("Point", "x y")
    for l in input_lines:
        (a,b) = l.split(": ")
        (s_x,s_y) = (scrib.find_int(a.split(",")[0]),scrib.find_int(a.split(",")[1]))
        sensor = Point(s_x,s_y)
        (b_x,b_y) = (scrib.find_int(b.split(",")[0]),scrib.find_int(b.split(",")[1]))
        beacon = Point(b_x,b_y)
        items.append((sensor,beacon))
        count = count + 1

    row_points = []
    row_range = []
    for item in items:
        sensor = item[0]
        beacon = item[1]
        distance = manhattan_distance(sensor,beacon)
        if sensor.y + distance >= row >= sensor.y - distance:
            # within range
            # print("pair within range {} - {}".format(sensor,beacon))

            d_row = manhattan_distance(sensor,Point(sensor.x,row))
            # print((Point(sensor.x-(distance-d_row),row),Point(sensor.x+(distance-d_row+1),row)))
            row_range.append((Point(sensor.x-(distance-d_row),row),Point(sensor.x+(distance-d_row+1),row)))
            # for row_x in range(sensor.x-(distance-d_row),sensor.x+(distance-d_row+1)):
            #     row_points.append(Point(row_x,row))

    row_points = list(set(row_points))

    count = 0
    points = {}
    for point in row_range:
        match = False
        for x in range(point[0].x,point[1].x):
            points[x] = 1

    for item in items:
        if item[1].y == row:
            points[item[1].x] = 0
            # print("there is a beacon {}".format(item[1]))

    print(sum(points.values()))
    # part 1 38m - 5511201


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    row = 2000000

    # input_file = "./data/" + d + "_test.txt"
    # row = 10
    part1(input_file,row)
    # part two is search from 0 to 4 000 000

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
