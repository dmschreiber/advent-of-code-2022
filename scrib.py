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
