import re
import scrib
import os
from collections import namedtuple


def get_grid_p2(grid,k,max_row):
    if k[0] > max_row + 1:
        return "#"

    if grid.get(k) is None:
        return "."

    return grid.get(k)


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    grid = make_grid(input_lines)

    start = (0,500)

    count = 0
    while True:
        max_row = print_grid(grid,False)
        count = count + 1
        # print("sands {}".format(count))
        sand = start
        last_sand = (-1, -1)
        while sand != last_sand and sand[0] <= max_row:
            # print("Current sand {} (last {})".format(sand,last_sand))
            grid[sand] = "."
            last_sand = sand
            if grid.get((sand[0]+1,sand[1])) is None or grid.get((sand[0]+1,sand[1])) == ".":
                # print("straight down")
                sand = (sand[0]+1,sand[1])
            elif grid.get((sand[0]+1,sand[1]-1)) is None or grid.get((sand[0]+1,sand[1]-1)) == ".":
                # print("down left")
                sand = (sand[0]+1,sand[1]-1)
            elif grid.get((sand[0]+1,sand[1]+1)) is None or grid.get((sand[0]+1,sand[1]+1)) == ".":
                # print("down right")
                sand = (sand[0]+1,sand[1]+1)
            grid[sand] = "o"

        # print("sand made row {}".format(last_sand[0]))
        if last_sand[0] >= max_row or (sand == start):
            break

    count = 0
    for k in grid.keys():
        if grid[k] == "o":
            count = count + 1

    print(count-1)


def part2(input):
    Point = namedtuple('Point', 'row col')
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    grid = make_grid(input_lines)

    start = Point(0,500)

    count = 0
    max_row = print_grid(grid, False)
    moved = True
    while moved:
        # print_grid(grid, True)
        count = count + 1
        # print("sands {}".format(count))
        sand = start
        last_sand = Point(-1, -1)
        while sand != last_sand and sand.row <= max_row:
            # print("Current sand {} (last {})".format(sand,last_sand))
            grid[sand] = "."
            last_sand = sand
            if get_grid_p2(grid,Point(sand.row+1,sand.col),max_row) == ".":
                # print("straight down")
                sand = Point(sand[0]+1,sand[1])
            elif get_grid_p2(grid,Point(sand.row+1,sand.col-1),max_row) == ".":
                # print("down left")
                sand = Point(sand.row+1,sand.col-1)
            elif get_grid_p2(grid,(sand.row+1,sand.col+1),max_row)  == ".":
                # print("down right")
                sand = Point(sand.row+1,sand.col+1)
            grid[sand] = "o"

        # print("sand made row {}".format(last_sand[0]))
        if sand == start:
            moved = False

    count = 0
    for k in grid.keys():
        if grid[k] == "o":
            count = count + 1

    print(count)


def make_grid(input_lines):
    grid = {}
    rows = []
    Point = namedtuple('Point', 'row col')

    for l in input_lines:
        points = l.split(" -> ")
        input_line = []
        for p in points:
            (col, row) = (int(p.split(",")[0]), int(p.split(",")[1]))
            item = Point(row,col)
            # print(row,col)
            input_line.append(item)
        rows.append(input_line)

    for l in rows:
        for p in range(len(l) - 1):
            first = l[p]
            second = l[p+1]
            if first.row == second.row:
                step = 1 if second.col > first.col else -1
                for c in range(first.col, second.col + step, step):
                    grid[(first.row, c)] = "#"

            if first.col == second.col:
                step = 1 if second.row > first.row else -1
                for r in range(first.row, second.row + step, step):
                    grid[(r, first.col)] = "#"
    return grid


def print_grid(grid,print_it):
    max_row = max([k[0] for k in grid.keys()])
    min_col = min([k[1] for k in grid.keys()])
    max_col = max([k[1] for k in grid.keys()])
    if print_it:
        for r in range(max_row + 1):
            for c in range(min_col, max_col + 1):
                if grid.get((r, c)) is None:
                    print(".", end="")
                else:
                    print(grid.get((r, c)), end="")
            print()
    return max_row

    # part 1 59:00
    # part 2 1:09:00

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"

    part1(input_file)
    part2(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
