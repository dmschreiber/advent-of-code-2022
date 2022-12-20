import re
import scrib
import os
from collections import namedtuple


class Item:
    def __init__(self,next,previous,num):
        self.next = next
        self.previous = previous
        self.num = num


def move_item(list_items,which):
    if which >= len(list_items):
        print("trying to index {}".format(which))
        exit(-1)

    item = list_items[which]
    prev_item = item.previous
    next_item = item.next

    # account for item.num < 0
    if item.num > 0:

        # remove item from list
        list_items[prev_item].next = next_item
        list_items[next_item].previous = prev_item

        # find new place and add it
        curr = item
        curr_index = 0
        loop_range = ((item.num -1) % (len(list_items)-1)) + 1
        # print(loop_range,item.num)
        for i in range(loop_range):
            curr_index = curr.next
            curr = list_items[curr.next]


        item.previous = curr_index
        item.next = curr.next
        my_next = curr.next
        curr.next = which
        list_items[my_next].previous = which

    elif item.num < 0:
        # remove item from list
        list_items[prev_item].next = next_item
        list_items[next_item].previous = prev_item

        # find new place and add it
        curr = item
        loop_range = ((abs(item.num) -1) % (len(list_items)-1)) + 1
        for i in range(loop_range):
            curr_index = curr.previous
            curr = list_items[curr.previous]

        item.next = curr_index

        my_prev = curr.previous
        item.previous = my_prev
        curr.previous = which
        list_items[my_prev].next = which

    return list_items


def part1(input, decryption, mixing_times):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    items = []

    # Item = namedtuple("Item", "next previous num")
    for index,l in enumerate(input_lines):
        prev_item = (index - 1) % len(input_lines)
        next_item = (index + 1) % len(input_lines)
        i = Item(next_item,prev_item,decryption * scrib.find_int(l))
        items.append(i)

    for j in range(mixing_times):
        for move_index in range(len(items)):
            items = move_item(items,move_index)

    curr = items[0]
    start_index = 0
    for index in range(len(items)):
        if curr.num == 0:
            start_index = items.index(curr)
            break
        else:
            curr = items[curr.next]

    curr = items[start_index]
    total = 0

    for i in range(3):
        for j in range(1000):
            curr = items[curr.next]
        total = total + curr.num

    print(total)

    # 4045 too high
    # 2827 right

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file,1,1)
    part1(input_file,811589153,10)
