import re
import scrib
import os


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    head = scrib.Point()
    tail = scrib.Point()
    visited = []
    for l in input_lines:
        (a,b) = l.split()
        if a == "U":
            head.y = head.y + int(b)
        if a == "D":
            head.y = head.y - int(b)
        if a == "R":
            head.x = head.x + int(b)
        if a == "L":
            head.x = head.x - int(b)

        while abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
            # too far
            if head.x == tail.x:
                tail.y = tail.y + (head.y - tail.y) / abs(head.y - tail.y)
            elif head.y == tail.y:
                tail.x = tail.x + (head.x - tail.x) / abs(head.x - tail.x)
            else:
                tail.y = tail.y + (head.y - tail.y) / abs(head.y - tail.y)
                tail.x = tail.x + (head.x - tail.x) / abs(head.x - tail.x)

            visited.append((tail.x,tail.y))

    unique = set(visited)
    print(len(unique))

    # part 2
    head = scrib.Point()
    tails = [scrib.Point() for p in range(10)]

    visited = []
    for l in input_lines:
        (a,b) = l.split()
        how_many = int(b)
        while how_many > 0:
            how_many = how_many - 1
            if a == "U":
                tails[0].y = tails[0].y + 1
            if a == "D":
                tails[0].y = tails[0].y - 1
            if a == "R":
                tails[0].x = tails[0].x + 1
            if a == "L":
                tails[0].x = tails[0].x - 1

            # print(tails[0].x,tails[0].y)
            for i in range(1,10):
                head = tails[i-1]
                tail = tails[i]

                while abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
                    # too far
                    if head.x == tail.x:
                        tail.y = tail.y + (head.y - tail.y) / abs(head.y - tail.y)
                    elif head.y == tail.y:
                        tail.x = tail.x + (head.x - tail.x) / abs(head.x - tail.x)
                    else:
                        tail.y = tail.y + (head.y - tail.y) / abs(head.y - tail.y)
                        tail.x = tail.x + (head.x - tail.x) / abs(head.x - tail.x)

                    visited.append((tails[9].x,tails[9].y))

    unique = set(visited)
    print(len(unique))
    # not 2595

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
