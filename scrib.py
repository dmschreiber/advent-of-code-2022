import re
from collections import Counter
import os

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class ThreeD_Point:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z


def add_point(p1,p2):
    if type(p1) is Point:
        return Point(p1.x + p2.x, p1.y + p2.y)
    elif type(p1) is ThreeD_Point:
        return ThreeD_Point(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)

def mult_point(p1,d):
    if type(p1) is Point:
        return Point(p1.x * d, p1.y * d)
    elif type(p1) is ThreeD_Point:
        return Point(p1.x * d, p1.y * d, p1.z * d)

def manhattan_distance(p1:ThreeD_Point, p2:ThreeD_Point):
    if type(p1) is Point:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
    elif type(p1) is ThreeD_Point:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)

def find_filename(input_string):
    result = os.path.basename(input_string)
    return result

def find_int(input_string):
    result = re.search(r"(\d+)",input_string)
    if result is not None:
        return int(result.group(0))
    else:
        raise Exception("Number not found")

def find_most_frequent(lst):
    frequent = max(set(lst), key=lst.count)
    return frequent

def find_occurances(lst):
    occurences = Counter(lst)
    return occurences

def find_even(lst):
    even = []

    # List Comprehension method
    even = [e for e in lst if e % 2 == 0]
    return even

def capitalize_words(lst):
    return list(map(str.capitalize, lst))

def reverse_list(lst):
    return lst[::-1]


def a_star_algorithm(grid, start_node, stop_node, get_neighbors):
    # def get_neighbors(grid,p):


    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])

    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    g = {}

    g[start_node] = 0

    # parents contains an adjacency map of all nodes
    parents = {}
    parents[start_node] = start_node

    while len(open_list) > 0:
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_list:
            if n == None or g[v] < g[n]:
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start_node)

            reconst_path.reverse()

            return reconst_path

        # for all neighbors of the current node do
        for m in get_neighbors(grid,n):
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
