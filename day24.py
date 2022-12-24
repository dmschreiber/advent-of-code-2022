import re
import scrib
import os
from collections import namedtuple

Point = namedtuple("Point", "row col minute")
Blizzard = namedtuple("Blizzard", "row col direction")
directions = [">","<","^","v"]

def blizzard_positions(blizzards,height,width,minute):
    for b in blizzards:
        if b.direction == 0:
            yield Blizzard(b.row,(b.col + minute) % width,b.direction)
        elif b.direction == 1:
            yield Blizzard(b.row, (b.col - minute) % width, b.direction)
        elif b.direction == 2:
            yield Blizzard((b.row - minute) % height, b.col, b.direction)
        elif b.direction == 3:
            yield Blizzard((b.row + minute) % height, b.col, b.direction)
        else:
            Exception("Invalid direction")


def add_point(p1,p2):
    return Point(p1.row+p2.row,p1.col+p2.col,p1.minute+p2.minute)

def get_neighbors(blizzards,height, width,node):
    neighbors = [Point(-1,0,1),Point(1,0,1),Point(0,-1,1),Point(0,1,1),Point(0,0,1)]
    neighbors = [add_point(p,node) for p in neighbors]
    b_pos = list(blizzard_positions(blizzards, height, width,node.minute+1))
    neighbors = [n for n in neighbors if n not in [Point(b.row,b.col,node.minute+1) for b in b_pos]]
    neighbors = [n for n in neighbors if (0 <= n.row < height and 0 <= n.col < width) or (n in [Point(-1, 0, node.minute + 1), Point(height, width - 1, node.minute + 1)])]
    return neighbors


def a_star_algorithm(blizzards, height, width, start_node, stop_node):
    # def get_neighbors(grid,p):


    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])

    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    g = {start_node: 0}

    # parents contains an adjacency map of all nodes
    parents = {start_node: start_node}

    while len(open_list) > 0:
        # print("{} open in minute {}".format(len(open_list),max(p.minute for p in open_list)))
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_list:
            if n is None or g[v] < g[n]:
                n = v

        if n is None:
            print('Path does not exist!')
            return None
        # else:
        #     print("Minute {} Distance from target {}".format(max(p.minute for p in open_list),abs(stop_node.row-n.row) + abs(stop_node.col-n.col)))

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n.row == stop_node.row and n.col == stop_node.col:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start_node)

            reconst_path.reverse()

            return reconst_path

        # for all neighbors of the current node do
        for m in get_neighbors(blizzards,height,width,n):
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + 1

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and g data
            # and if the node was in the closed_list, move it to open_list
            else:
                if g[m] > g[n] + 1:
                    g[m] = g[n] + 1
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_list.remove(n)
        closed_list.add(n)

    # print('Path does not exist!')
    return None

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    grid = {}
    blizzards = []
    start_position = Point(-1,0,0)

    height = len(input_lines)-2
    width = len(input_lines[0])-2

    end_position = Point(height,width-1,-1)


    for row,row_value in enumerate(input_lines[1:len(input_lines)-1]):
        for col in range(width):
            grid[(row,col)] = row_value[col+1:col+2]
            if grid[(row,col)] in directions:
                blizzards.append(Blizzard(row,col,directions.index(grid[(row,col)])))


    # path = a_star_algorithm(blizzards,height,width,start_position,end_position)
    start_position = Point(height,width-1,286)
    end_position = Point(-1,0,-1)
    path = a_star_algorithm(blizzards,height,width,start_position,end_position)

    print("Path back home {}".format(path))
    back_home_minute = max(p.minute for p in path)
    print("Back home at minute {}".format(back_home_minute))

    back_home_minute = 541
    start_position = Point(-1,0,back_home_minute)
    end_position = Point(height,width-1,-1)
    path = a_star_algorithm(blizzards,height,width,start_position,end_position)

    print("Path out second time {}".format(path))
    print("Part 2 final answer {}".format(max(p.minute for p in path)))


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
