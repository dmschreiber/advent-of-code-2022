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
    dirs = {"U":scrib.Point(0,1), "D":scrib.Point(0,-1), "L":scrib.Point(-1,0), "R":scrib.Point(1,0)}

    for l in input_lines:
        (a,b) = l.split()
        head = scrib.add_point(head, scrib.mult_point(dirs[a],int(b)))

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
    dirs = {"U":scrib.Point(0,1), "D":scrib.Point(0,-1), "L":scrib.Point(-1,0), "R":scrib.Point(1,0)}

    visited = []
    for l in input_lines:
        (a,b) = l.split()
        how_many = int(b)
        while how_many > 0:
            how_many = how_many - 1
            tails[0] = scrib.add_point(tails[0],dirs[a])

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


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"

    part1(input_file)