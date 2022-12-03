import re
import scrib


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    list_input = []

    total_score = 0
    for l in input_lines:
        item = ""
        a = l[:int(len(l)/2)]
        b = l[int(len(l)/2):]
        for c in list(a):
            for d in list(b):
                if c == d:
                    item = c

        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            score = int(ord(item) - ord('A')) + 27
        else:
            score = int(ord(item) - ord('a')) + 1
        total_score = total_score + score

    print(total_score)

    total_score = 0
    for index in range(int(len(input_lines)/3)):
        first = input_lines[index*3]
        second = input_lines[index*3+1]
        third = input_lines[index*3+2]

        item = ""
        for c in list(first):
            for d in list(second):
                for e in list(third):
                    if c == d == e:
                        item = c

        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            score = int(ord(item) - ord('A')) + 27
        else:
            score = int(ord(item) - ord('a')) + 1
        total_score = total_score + score
    print(total_score)


    # dirs = [d for (d,v) in list_input]


if __name__ == '__main__':
    input_file = "./data/day3_input.txt"
    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
