import re
import scrib
import os
import functools


def compare_lists(l, r):
    left = l
    right = r
    item_count = min(len(left), len(right))

    for i in range(item_count):
        l_i = left[i]
        r_i = right[i]
        if type(l_i) is int and type(r_i) is int:
            if l_i < r_i:
                return 1
            elif l_i > r_i:
                return -1

        else:
            if type(l_i) is int:
                l_i = [l_i]
            elif type(r_i) is int:
                r_i = [r_i]

            res = compare_lists(l_i, r_i)
            if res != 0:
                return res

    if len(left) < len(right):
        return 1

    elif len(right) < len(left):
        return -1

    else:
        return 0


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    total = 0
    for index in range(int((len(input_lines) + 1) / 3)):
        left = eval(input_lines[index * 3])
        right = eval(input_lines[index * 3 + 1])

        if compare_lists(left, right) > 0:
            total = total + index + 1

    print(total)
    # right 29:15


def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    items = []
    a = [[2]]
    b = [[6]]

    for l in input_lines:
        if l != "":
            items.append(eval(l))
    items.append(a)
    items.append(b)

    sorted_l = sorted(items, key=functools.cmp_to_key(compare_lists), reverse=True)

    print((sorted_l.index(a) + 1) * (sorted_l.index(b) + 1))

    # right 38:26


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d) - 3]

    input_file = "./data/" + d + "_input.txt"
    part1(input_file)
    part2(input_file)
