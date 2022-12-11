import re
import scrib
import os
from functools import reduce
from sympy.ntheory import primefactors
from operator import mul
import time

def part1(input,div_by,rounds):
    with open(input) as f:
        input_lines = f.read().splitlines()

    monkeys = []

    for i in range(int((len(input_lines)+1)/7)):
        index = i*7

        starting_items = input_lines[index+1].split(": ")[1].split(",")
        starting_items = [int(s) for s in starting_items]
        formula = input_lines[index+2].split(": ")[1].split("= ")[1]
        test_divisible_by = scrib.find_int(input_lines[index+3])
        if_true_throw_to = scrib.find_int(input_lines[index+4])
        if_false_throw_to = scrib.find_int(input_lines[index+5])
        monkeys.append((starting_items,formula,test_divisible_by,if_true_throw_to,if_false_throw_to))

    mod_by = reduce(mul,[m[2] for m in monkeys],1)

    inspection = []
    for i in range(len(monkeys)):
        inspection.append(0)

    for round in range(rounds):
        # print("round {}".format(round))
        for i in range(len(monkeys)):
            inspection[i] = inspection[i] + len(monkeys[i][0])
            for worry in monkeys[i][0]:
                new_worry = eval(monkeys[i][1].replace("old",str(worry)))

                if (div_by > 1):
                    new_worry = int(new_worry / div_by)
                new_worry = new_worry % mod_by

                if new_worry % monkeys[i][2] == 0:
                    monkeys[monkeys[i][3]][0].append(new_worry)
                else:
                    monkeys[monkeys[i][4]][0].append(new_worry)
            monkeys[i] = ([],monkeys[i][1],monkeys[i][2],monkeys[i][3],monkeys[i][4])

    inspection.sort(reverse=True)
    print(inspection[0]*inspection[1])


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    part1(input_file,3,20)

    # input_file = "./data/" + d + "_test.txt"
    part1(input_file,1,10000)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
