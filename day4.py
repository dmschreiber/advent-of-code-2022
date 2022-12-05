import re
import scrib


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    total_score = 0
    count = 0
    for l in input_lines:
        (a1,a2), (b1,b2) = [(int(n[0]), int(n[1])) for n in [z.split("-") for z in l.split(",")]]

        if a1 <= b1 and a2 >= b2:
            count = count + 1
        elif b1 <= a1 and b2 >= a2:
            count = count + 1

    print(count)

    count = 0
    for l in input_lines:
        (a1,a2), (b1,b2) = [(int(n[0]), int(n[1])) for n in [z.split("-") for z in l.split(",")]]

        if a1 <= b1 <= a2:
            count = count + 1
        elif b1 <= a1 <= b2:
            count = count + 1
    print(count)

if __name__ == '__main__':
    input_file = "./data/day4_input.txt"
    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))