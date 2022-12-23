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


    print(1000*(position[0]+1) + 4*(position[1]+1) + rotation)

faces = {"D": (100,0), "A": (0,50), "B": (0,100), "C": (50,50), "E": (100,50), "F": (150,0)}
R_RIGHT = 0
R_DOWN = 1
R_LEFT = 2
R_UP = 3


def part2(input):
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

    print(start_position)
    line = input_lines[len(input_lines)-1]
    direction_character = [">","v","<","^"]
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

    rotation = 0
    position = start_position
    positions = {}
    for i in instructions:
        if i == "R":
            rotation = (rotation + 1) % 4
        elif i == "L":
            rotation = (rotation - 1) % 4
        else:
            print("Step {} steps".format(i))
            for step in range(i):
                positions[position] = rotation
                if (position[0] + directions[rotation][0],position[1] + directions[rotation][1]) in grid.keys() and grid[(position[0] + directions[rotation][0],position[1] + directions[rotation][1])] in ["."]:
                    position = (position[0] + directions[rotation][0],position[1] + directions[rotation][1])
                elif  (position[0] + directions[rotation][0],position[1] + directions[rotation][1]) not in grid.keys() or grid[(position[0] + directions[rotation][0],position[1] + directions[rotation][1])] == " ": # wrap
                    (row,column) = (position[0],position[1])

                    my_face = ""
                    for k in faces.keys():
                        face = faces[k]
                        if face[0] <= position[0] < face[0]+50 and face[1] <= position[1] < face[1]+50:
                            my_face = k
                            print("My face {}".format(my_face))



                    print("Wrapping at {} with rotation {}".format(position,rotation))

                    row = row - faces[my_face][0]
                    column = column - faces[my_face][1]
                    next_rotation = rotation
                    if rotation == R_LEFT and my_face == "A":  # Left A -> Right D (rows - row,0) CHECKED
                        next_rotation = R_RIGHT
                        row = faces["D"][0] + 49 - row
                        column = faces["D"][1]

                    elif rotation == R_UP and my_face == "A": # Up A -> Right F (col,0) CHECKED
                        next_rotation = R_RIGHT
                        row = faces["F"][0] + column
                        column = faces["F"][1]

                    elif rotation == R_UP and my_face == "B": # Up B -> Up F (rows, col) CHECKED
                        next_rotation = R_UP
                        row = faces["F"][0] + 49
                        column = faces["F"][1] + column

                    elif rotation == R_DOWN and my_face == "B": # Down B -> Left C (col,cols) CHECKED
                        next_rotation = R_LEFT
                        row = faces["C"][0] + column
                        column = faces["C"][1] + 49

                    elif rotation == R_RIGHT and my_face == "B": # Right B -> Left E (rows-row,cols) CHECKED
                        next_rotation = R_LEFT
                        row = faces["E"][0] + 49 - row
                        column = faces["E"][1] + 49

                    elif rotation == R_RIGHT and my_face == "C": # Right C -> Up B (col,rows) CHECKED
                        next_rotation = R_UP
                        column = faces["B"][1] + row
                        row = faces["B"][0] + 49

                    elif rotation == R_LEFT and my_face == "C": # Left C -> Down D (0,row) CHECKED
                        next_rotation = R_DOWN
                        column = faces["D"][1] + row
                        row = faces["D"][0]

                    elif rotation == R_RIGHT and my_face == "E": # Right E -> Left B (rows-row,cols) CHECKED
                        next_rotation = R_LEFT
                        row = faces["B"][0] + 49 - row
                        column = faces["B"][1] + 49

                    elif rotation == R_DOWN  and my_face == "E": # Down E -> Left F (cols,col) CHECKED
                        next_rotation = R_LEFT
                        row = faces["F"][0] + column
                        column = faces["F"][1] + 49

                    elif rotation == R_UP and my_face == "D": # Up D -> Right C (col,0) CHECKED
                        print("D up to C right {},{}".format(row,column),end="")
                        next_rotation = R_RIGHT
                        row = faces["C"][0] + column
                        column = faces["C"][1]
                        print("to {},{}".format(row,column))

                    elif rotation == R_LEFT and my_face == "D": # Left D -> Right A (rows-row,0) CHECKED
                        next_rotation = R_RIGHT
                        row = faces["A"][0] + 49 - row
                        column = faces["A"][1]

                    elif rotation == R_RIGHT and my_face == "F": # Right F -> Up E (rows,row) CHECKED
                        next_rotation = R_UP
                        column = faces["E"][1] + row
                        row = faces["E"][0] + 49

                    elif rotation == R_LEFT and my_face == "F": # Left F -> Down A (0,row) CHECKED
                        next_rotation = R_DOWN
                        column = faces["A"][1] + row
                        row = faces["A"][0]

                    elif rotation == R_DOWN and my_face == "F": # Down F -> Down B (0,col) CHECKED
                        next_rotation = R_DOWN
                        row = faces["B"][0]
                        column = faces["B"][1] + column
                    else:
                        Exception("Off the map without one of the conditions")

                    if (row,column) in grid.keys() and grid[(row,column)] in ["."]:
                        rotation = next_rotation
                        position = (row,column)
                        print("Becomes at {}".format(position))
                    else:
                        print("off the map but cannot become {}".format((row,column)))
                        break

        # print("Ending position {}, rotation {}".format(position,rotation))

    max_row = max(k[0] for k in grid.keys())
    max_col = max(k[1] for k in grid.keys())

    for row in range(max_row):
        for col in range(max_col):
            if (row,col) in positions.keys():
                print(direction_character[positions[(row,col)]],end="")
            else:
                print(grid.get((row,col)," "),end="")
        print()

    print(1000*(position[0]+1) + 4*(position[1]+1) + rotation)

    # 147173 is too high
    # now 150262 (still too high)
    # 17393 is too low
    # 24566 is too low

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file)
    part2(input_file)

