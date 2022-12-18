import re
import scrib
import os
from collections import namedtuple


def add_point(grid,p,sides):

    add_sides = 6
    for current in grid:
        if current.x == p.x + 1 and current.y == p.y and current.z == p.z:
            add_sides = add_sides - 2
        if current.x == p.x - 1 and current.y == p.y and current.z == p.z:
            add_sides = add_sides - 2
        if current.x == p.x and current.y == p.y + 1 and current.z == p.z:
            add_sides = add_sides - 2
        if current.x == p.x and current.y == p.y - 1 and current.z == p.z:
            add_sides = add_sides - 2
        if current.x == p.x and current.y == p.y  and current.z == p.z + 1:
            add_sides = add_sides - 2
        if current.x == p.x and current.y == p.y and current.z == p.z - 1:
            add_sides = add_sides - 2

    grid.append(p)

    return sides + add_sides


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    grid = []
    Point = namedtuple("Point", "x y z")
    sides = 0

    for l in input_lines:
        (x,y,z) = l.split(",")
        p = Point(int(x),int(y),int(z))
        sides = add_point(grid,p,sides)

    print(sides)


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file)
    # too high 10768

