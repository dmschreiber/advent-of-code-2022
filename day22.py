import re
import scrib
import os
from collections import namedtuple

directions = [(0,1), (1,0), (0,-1), (-1,0)] # right, down, left, up
def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    grid = {}
    Point = namedtuple("Point", "x y")
    start_position = None
    for row in range(len(input_lines)-2):
        for col in range(len(input_lines[row])):
            if row == 0 and input_lines[row][col] != ' 'and start_position is None:
                start_position = (row,col)

            grid[(row,col)] = input_lines[row][col:col+1]
    print(grid)
    print(start_position)
    line = input_lines[len(input_lines)-1]

    num = ""
    instructions = []
    for index in range(len(line)):
        char = line[index:index+1]
        if char in ["R","L"]:
            instructions.append(int(num))
            num = ""
            instructions.append(char)
        else:
            num = num + line[index:index+1]
    if len(num) > 0:
        instructions.append(int(num))

    print(instructions)

    rotation = 0
    position = start_position
    for i in instructions:
        if i == "R":
            rotation = (rotation + 1) % 4
        elif i == "L":
            rotation = (rotation - 1) % 4
        else:
            for step in range(i):
                if (position[0] + directions[rotation][0],position[1] + directions[rotation][1]) in grid.keys() and grid[(position[0] + directions[rotation][0],position[1] + directions[rotation][1])] == ".":
                    position = (position[0] + directions[rotation][0],position[1] + directions[rotation][1])
                elif  (position[0] + directions[rotation][0],position[1] + directions[rotation][1]) not in grid.keys() or grid[(position[0] + directions[rotation][0],position[1] + directions[rotation][1])] == " ": # wrap
                    (row,column) = (position[0],position[1])
                    print("Wrapping at {} with rotation {}".format(position,rotation))
                    if rotation == 0:
                        column = min(k[1] for k in filter(lambda k: k[0] == position[0] and grid[k] in [".","#"], grid.keys()))
                    elif rotation == 2:
                        column = max(k[1] for k in filter(lambda k: k[0] == position[0] and grid[k] in [".","#"], grid.keys()))
                    elif rotation == 1:
                        row = min(k[0] for k in filter(lambda k: k[1] == position[1] and grid[k] in [".","#"], grid.keys()))
                    elif rotation == 3:
                        row = max(k[0] for k in filter(lambda k: k[1] == position[1] and grid[k] in [".","#"], grid.keys()))

                    if (row,column) in grid.keys() and grid[(row,column)] == ".":
                        position = (row,column)
                        print("Becomes at {}".format(position))

        print("Ending position {}, rotation {}".format(position,rotation))

    print(1000*(position[0]+1) + 4*(position[1]+1) + rotation)


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
