import re
import scrib
import os

def part1(input,chars):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    l = input_lines[0]
    for i in range(chars,len(l)):
        m = list(l[i-chars:i])
        how_many = scrib.find_occurances(m)
        if max(how_many.values()) == 1:
            print(i)
            return


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    part1(input_file,4)
    part1(input_file,14)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
