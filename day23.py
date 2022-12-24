import re
import scrib
import os
from collections import namedtuple
from time import time

Point = namedtuple("Point", "row column")

steps = [[Point(-1,0),Point(-1,-1),Point(-1,1)],    #North
         [Point(1,0),Point(1,1),Point(1,-1)],       #South
         [Point(0,-1),Point(-1,-1),Point(1,-1)],    #West
         [Point(0,1),Point(1,1),Point(-1,1)]        #East
         ]

neighbors = []
movements = [Point(-1,0), Point(1,0), Point(0,-1), Point(0,1)]

def add_point(p1, p2):
    return Point(p1.row+p2.row,p1.column+p2.column)


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    for row in [-1,0,1]:
        for col in [-1,0,1]:
            if row != 0 or col != 0:
                neighbors.append(Point(row,col))

    grid = {}

    for row,l in enumerate(input_lines):
        for col in range(len(l)):
            p = Point(row,col)
            grid[p] = 1 if l[col:col+1] == "#" else 0

    elves = list(filter(lambda k: grid[k] == 1,grid.keys()))

    direction_start_state = 0
    keep_going = True
    round = 1
    while keep_going:
        how_many_move = 0
        new_positions = []
        proposed_moves = []
        print("Round {} direction start state is {}".format(round, direction_start_state))
        round = round + 1
        keep_going = False
        for elf in elves:

            if len(set([add_point(elf,n) for n in neighbors]).intersection(elves)) != 0:
                proposed_move = None
                direction_state = direction_start_state

                for i in range(len(movements)):
                    movement = movements[direction_state]
                    step = steps[direction_state]

                    if len(set([add_point(elf,s) for s in step]).intersection(elves)) == 0 and proposed_move is None:
                        proposed_move = add_point(elf,movement)
                        break

                    direction_state = (direction_state + 1) % len(movements)

                if proposed_move is not None:
                    # print("{},{} proposes to move to {},{}".format(elf.row,elf.column,proposed_move.row,proposed_move.column))
                    proposed_moves.append((elf,proposed_move))
                else:
                    new_positions.append(elf)

            else:
                new_positions.append(elf)

        check_moves = scrib.find_occurances([pm[1] for pm in proposed_moves])
        check_moves = list(filter(lambda k: check_moves[k] > 1, check_moves.keys()))

        # new_positions.extend([pm[0] for pm in proposed_moves if pm[1] in check_moves])
        # new_positions.extend([pm[1] for pm in proposed_moves if pm[1] not in check_moves])
        # how_many_move = len([pm[1] for pm in proposed_moves if pm[1] not in check_moves])
        # keep_going = how_many_move > 0
        for pm in proposed_moves:
            if pm[1] in check_moves:
                new_positions.append(pm[0])
            else:
                keep_going = True
                how_many_move = how_many_move + 1
                new_positions.append(pm[1])

        print("Elves moved {}".format(how_many_move))

        elves = new_positions
        direction_start_state = (direction_start_state + 1) % len(movements)


    min_row = min(k.row for k in elves)
    max_row = max(k.row for k in elves)
    min_col = min(k.column for k in elves)
    max_col = max(k.column for k in elves)

        # for row in range(min_row,max_row+1):
        #     for col in range(min_col,max_col+1):
        #         if (row,col) in elves:
        #             print("#",end="")
        #         else:
        #             print(".",end="")
        #     print()

    print((max_row-min_row+1) * (max_col-min_col+1) - len(elves))
    print("Round {}".format(round-1))

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    start = time()
    part1(input_file)
    print("Elapsed {}".format(time()-start))
    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
