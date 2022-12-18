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
history = {}

grid2 = {}

shape_index = 0
jetIndex = 0


def collision(grid, shape):
    shape_grid = shapes_source[shape.which]
    if shape.row < 0:
        return True

    if shape.col < 0:
        return True

    if shape.col + shapes_width[shape.which] > max_col:
        return True

    for row in range(len(shape_grid)):
        n1 = shapes_numbers[shape.which][row] * 2 ** (7 - shape.col - shapes_width[shape.which])
        n2 = grid2.get(shape.row - row,0)

        if n1&n2 > 0:
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


def place_shape(shape):
    shape_grid = shapes_source[shape.which]

    check_rows = []
    for row in range(len(shape_grid)):
        number = shapes_numbers[shape.which][row] * 2 ** (7 - shape.col - shapes_width[shape.which])
        grid2[shape.row - row] = grid2.get(shape.row - row,0) | number
        check_rows.append(shape.row - row)

    if shape_index == (793+297):
        print(grid2.get(max(grid2.keys())))
        print("Shape index {} height {}".format(shape_index-793,max(grid2.keys())-1275))

    check_rows = list(set(check_rows))
    new_bottom = min(check_rows)
    check_band = 1

    for col in range(7):
        if sum([grid2.get(row,0) & 2**(6-col) for row in range(new_bottom,new_bottom+check_band)]) == 0:
            return

    check_sum = 0
    for row in range(check_band):
        check_sum = check_sum * 2**7 + grid2.get(shape.row - row,0)

    if check_sum in history.keys() and history[check_sum][1] == shape.which and history[check_sum][2] == jetIndex and jetIndex == 4565:
        print("found previous pattern {} at {} (current {}) - jetIndex {}, shapeIndex {}".format(check_sum,history[check_sum],new_bottom,jetIndex,shape_index))

    else:
        history[check_sum] = (new_bottom,shape.which,jetIndex,shape_index)

    min_row = min(list(grid2.keys()))
    to_remove = list(range(min_row,new_bottom))
    for k in to_remove:
        if k in grid2.keys():
            grid2.pop(k)

    return



def print_grid():
    max_row = max(k for k in grid2.keys())
    for row in range(max_row,-1,-1):
        print("{:4d} {:07b}".format(row,grid2.get(row,0)))


def part1(input, total):
    global jetIndex, shape_index
    make_shape_numbers()

    start = time.time()
    jet_moves = {">": +1, "<": -1}

    with open(input) as f:
        input_lines = f.read().splitlines()

    start_col = 2
    start_row = 3


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
            place_shape(shape)
            if shape_index + 1 >= total:
                break
            top_row = max(k for k in grid2.keys()) + 3 + shapes_height[(shape.which + 1) % len(shapes_source)]

            if (shape_index+1) % 1000000 == 0:
                elapsed = time.time()-start
                print("Percent done {:.4f} at {} seconds".format(100*shape_index/total,time.time()-start))
                if shape_index > 0:
                    print("Estimated complete in {} hours".format(elapsed*(total/shape_index)/3600))
                print("size grid2 {}".format(len(grid2)))

            shape = Shape((shape.which + 1) % len(shapes_source),top_row,start_col)
            shape_index = shape_index + 1

    # print_grid()
    # print(max(k[0] for k in grid.keys())+1)
    print(max(grid2.keys())+1)

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    total = 2022
    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file, total)

    total = 1000000000000

    # first_row + int(total/shape_periodicity)*row_periodicity + height(total % shape_periodicity + first_shape) - height(first_shape)
    # first_row is when pattern starts
    # first_shape is first shape_index when pattern starts
    # shape_periodicity is difference in shape_index between repeating patterns
    # row_periodicity is difference in row between repeating patterns

    total = 10000
    part1(input_file, total)
    # part 2
    # 1532163742773 too high
    # 1532163742772 too high
    # 1532163742771 too high
    # 1532163742770 too high
    # 1532163742769 too high
    # 1532163742768 too high
    # 1532163742758 RIGHT - Math

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
