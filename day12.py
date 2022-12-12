import re
import scrib
import os


def get_neighbors(grid,p):
    row = p[0]
    col = p[1]
    n = []
    if row > 0 and ord(grid[row-1][col]) <= ord(grid[row][col]) + 1:
        n.append((row-1,col))
    if row < len(grid)-1 and ord(grid[row+1][col]) <= ord(grid[row][col]) + 1:
        n.append((row+1,col))
    if col < len(grid[row])-1 and ord(grid[row][col+1]) <= ord(grid[row][col]) + 1:
        n.append((row,col+1))
    if col > 0 and ord(grid[row][col - 1]) <= ord(grid[row][col]) + 1:
        n.append((row,col-1))

    return n


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    grid = {}
    rows = len(input_lines)
    for i in range(len(input_lines)):
        grid[i] = list(input_lines[i])
    start = (0,0)
    end = (0,0)

    for row in range(rows):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                start = (row,col)
                grid[row][col] = "a"
            elif grid[row][col] == "E":
                end = (row,col)
                grid[row][col] = "z"

    print(len(scrib.a_star_algorithm(grid, start, end, get_neighbors))-1)

    # part 2
    starts = []
    for row in range(rows):
        for col in range(len(grid[row])):
            if grid[row][col] == "a":
                starts.append((row,col))

    starts_len = []
    for s in starts:
        path = scrib.a_star_algorithm(grid,s,end, get_neighbors)
        if path != None:
            starts_len.append(len(path)-1)

    starts_len.sort()
    print(starts_len[0])


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    part1(input_file)
    # 438 not right

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
