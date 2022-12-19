import re
import scrib
import os
from collections import namedtuple
from time import time

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

Point = namedtuple("Point", "x y z")
def get_neighbors(grid,p):
    n = []
    n.append(Point(p.x,p.y,p.z+1))
    n.append(Point(p.x, p.y, p.z - 1))
    n.append(Point(p.x, p.y+1, p.z))
    n.append(Point(p.x, p.y-1, p.z))
    n.append(Point(p.x+1, p.y, p.z))
    n.append(Point(p.x-1, p.y, p.z))
    n_list = n.copy()

    for p in n_list:
        if p in grid:
            n.remove(p)

    return n

def find_closest_outside(outside,p):
    current_min = None
    current_outside = None
    for o in outside:
        if current_min is None or abs(o.x - p.x) + abs(o.y - p.y) + abs(o.z - p.z) < current_min:
            current_min = abs(o.x - p.x) + abs(o.y - p.y) + abs(o.z - p.z)
            current_outside = Point(o.x,o.y,o.z)

    return current_outside


def find_all_neighbors(grid,p):
    neighbors = list(get_neighbors(grid,p))
    last_size = 0

    while len(neighbors) != last_size:
        new_n = neighbors.copy()
        for n in neighbors:
            new_n.extend(list(get_neighbors(grid,n)))

        new_n = list(set(new_n))
        last_size = len(neighbors)
        neighbors = new_n

    return neighbors


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    grid = []
    # Point = namedtuple("Point", "x y z")
    sides = 0

    for l in input_lines:
        (x,y,z) = l.split(",")
        p = Point(int(x),int(y),int(z))
        sides = add_point(grid,p,sides)

    print(sides)
    print(min([p.x for p in grid]),max([p.x for p in grid]))
    print(min([p.y for p in grid]),max([p.y for p in grid]))
    print(min([p.z for p in grid]),max([p.z for p in grid]))

    outside=[]
    min_x = min([p.x for p in grid])
    max_x = max([p.x for p in grid])
    min_y = min([p.y for p in grid])
    max_y = max([p.y for p in grid])
    min_z = min([p.z for p in grid])
    max_z = max([p.z for p in grid])

    for x in [min_x,max_x+1]:
        for y in [min_y,max_y+1]:
            for z in [min_z,max_z+1]:
                outside.append(Point(x,y,z))

    for x in range(min_x,max_x+1):
        start = time()
        print("{}".format(x),end="")
        for y in range(min_y,max_y+1):
            for z in range(min_z,max_z+1):
                my_point = Point(x,y,z)
                outside.extend([Point(x,y,min_z-1),Point(x,y,max_z+1),Point(x,min_y-1,z),Point(x,max_y+1,z),Point(min_x-1,y,z),Point(max_x+1,y,z)])
                my_outside = find_closest_outside(outside,my_point)
                if Point(x,y,z) not in grid and scrib.a_star_algorithm(grid,my_point,my_outside,get_neighbors) is None:
                    sides = add_point(grid,Point(x,y,z),sides)

                    neighbors = find_all_neighbors(grid,Point(x,y,z))
                    for n in neighbors:
                        sides = add_point(grid,n,sides)
                # elif Point(z,y,z) not in grid:
                #     neighbors = find_all_neighbors(grid,Point(x,y,z))
                #     outside.extend(neighbors)


        print("({:2.2f}s-{}),".format(time() - start,len(grid)),end="")

    print()
    print(sides)

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file)
    # too high 10768

