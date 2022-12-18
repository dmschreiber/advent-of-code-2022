import re
import scrib
import os
from collections import namedtuple
import time


shapes_source = [["####"], [".#.", "###", ".#."], ["..#", "..#", "###"], ["#", "#", "#", "#"], ["##", "##"]]
shapes_numbers = []
max_col = 7
shapes_width = [len(s[0]) for s in shapes_source]
shapes_height = [len(s) for s in shapes_source]


def collision(grid, shape):
    shape_grid = shapes_source[shape.which]
    if shape.row < 0:
        return True

    if shape.col < 0:
        return True

    if shape.col + shapes_width[shape.which] > max_col:
        return True

    for row in range(len(shape_grid)):
        n1 = shapes_numbers[shape.which][row]

        n2 = "".join(list(["1" if grid.get((shape.row - 0,shape.col + col)) == "#" else "0" for col in range(len(shape_grid[0]))]))
        n2 = int(n2,2)
        if n1&n2 > 0:
            return True

        for col in range(len(shape_grid[0])):
            if shape_grid[row][col] == "#" and grid.get((shape.row - row,shape.col + col)) == "#":
                return True

    return False


def make_shape_numbers():
    for s in shapes_source:
        shape_number = []
        for shape_row in s:
            n1 = shape_row
            n1 = n1.replace("#", "1")
            n1 = n1.replace(".", "0")
            n1 = int(n1, 2)
            shape_number.append(n1)

        shapes_numbers.append(shape_number)


def place_shape(grid,shape):
    shape_grid = shapes_source[shape.which]

    check_rows = []
    for col in range(len(shape_grid[0])):
        for row in range(len(shape_grid)):
            if shape_grid[row][col] == "#":
                grid[(shape.row - row,shape.col + col)] = "#"
                check_rows.append(shape.row - row)

    check_rows = list(set(check_rows))
    new_bottom = min(check_rows)
    check_band = 5

    for col in range(7):
        # print("Sum of col {} is {}".format(col,sum([1 if grid.get((row, col)) == "#" else 0 for row in range(new_bottom,new_bottom+check_band)])))
        if sum([1 if grid.get((row, col)) == "#" else 0 for row in range(new_bottom,new_bottom+check_band)]) == 0:
            return grid

    to_remove = list(filter(lambda k : k[0] < new_bottom, list(grid.keys())))
    for k in to_remove:
        grid.pop(k)
    return grid


def print_grid(grid):
    max_row = max(k[0] for k in grid.keys())
    for row in range(max_row,-1,-1):
        for col in range(max_col):
            if grid.get((row,col)) is None:
                print(".",end="")
            else:
                print(grid.get((row, col)),end="")
        print()


def part1(input, total):
    make_shape_numbers()

    start = time.time()
    jet_moves = {">": +1, "<": -1}

    with open(input) as f:
        input_lines = f.read().splitlines()

    start_col = 2
    start_row = 3
    shape_index = 0
    jetIndex = 0


    Shape = namedtuple("Shape", "which row col")
    jets = list(input_lines[0])

    shape = Shape(0,start_row,start_col)
    grid = {}

    while True:
        # jet
        jet_move = jet_moves[jets[jetIndex]]
        jetIndex = (jetIndex + 1) % len(jets)

        if not collision(grid, Shape(shape.which, shape.row, shape.col + jet_move)):
            shape = Shape(shape.which, shape.row,shape.col+jet_move)

        # fall
        if not collision(grid, Shape(shape.which,shape.row-1,shape.col)):
            shape = Shape(shape.which,shape.row-1,shape.col)

        else:
            # new shape
            grid = place_shape(grid,shape)
            if shape_index + 1 >= total:
                break
            top_row = max(k[0] for k in grid.keys()) + 3 + shapes_height[(shape.which + 1) % len(shapes_source)]

            if shape_index % 100000 == 0:
                print("Percent done {:.4f} at {} seconds".format(100*shape_index/total,time.time()-start))
                print("size {}".format(len(grid)))

            shape = Shape((shape.which + 1) % len(shapes_source),top_row,start_col)
            shape_index = shape_index + 1

    # print_grid(grid)
    print(max(k[0] for k in grid.keys())+1)
    # 3146 too low


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    total = 2022
    input_file = "./data/" + d + "_input.txt"
    input_file = "./data/" + d + "_test.txt"
    part1(input_file, total)

    total = 1000000000000
    part1(input_file, total)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
