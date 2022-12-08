import re
import scrib
import os


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    row = 0
    grid = []
    for l in input_lines:
        grid.append([int(c) for c in list(l)])
        row = row + 1

    rows = row
    width = rows
    count = 0

    for row in range(rows):
        for col in range(width):
            # print(grid[row][col])
            if 0 < row < rows - 1 and 0 < col < width - 1:
                left_max = max([grid[row][i] for i in range(col)])
                right_max = max([grid[row][i] for i in range(col+1,width)])
                top_max = max([grid[i][col] for i in range(row)])
                bottom_max = max([grid[i][col] for i in range(row+1,rows)])
                visible = left_max < grid[row][col] or right_max < grid[row][col] or top_max < grid[row][col] or bottom_max < grid[row][col]

            else:
                visible = True

            if visible:
                count = count + 1
    print(count)

    max_view_total = 0
    for row in range(1,rows-1):
        for col in range(1,width-1):

            view_total = 1
            view = 0
            for i in range(col-1,-1,-1):
                view = view + 1
                if grid[row][col] <= grid[row][i]:
                    break

            view_total = view_total * view

            view = 0
            for i in range(col + 1,width):
                view = view + 1
                if grid[row][col] <= grid[row][i]:
                    break

            view_total = view_total * view

            view = 0
            for i in range(row-1,-1,-1):
                view = view + 1
                if grid[row][col] <= grid[i][col]:
                    break

            view_total = view_total * view

            view = 0

            for i in range(row+1,rows):
                view = view + 1
                if grid[row][col] <= grid[i][col]:
                    break

            view_total = view_total * view

            if view_total > max_view_total:
                max_view_total = view_total

    print(max_view_total)


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/day8_test.txt"

    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
