import re
import scrib

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    list_numbers = []
    elf = []
    total = 0
    for l in input_lines:
        if l == "":
            elf.append(total)
            total = 0
        else:
            total = total + scrib.find_int(l)

    elf.sort(reverse=True)
    print(elf[0])
    print(elf[0]+elf[1]+elf[2])

if __name__ == '__main__':
    input = "./data/day1_input.txt"
    part1(input)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))