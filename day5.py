import re
import scrib


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    total = 0

    for l in input_lines:
        (a,b) = l.split(",")

    print(total)


if __name__ == '__main__':
    input_file = "./data/day5_input.txt"
    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))