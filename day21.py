import re
import scrib
import os
from collections import namedtuple

from sympy.solvers import solve
from sympy import Symbol


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    monkeys = {}


    for l in input_lines:
        (a,b) = l.split(": ")

        monkeys[a] = b

    result = monkeys["root"]

    while re.search("[a-z]",result) is not None:
        for key in monkeys.keys():
            result = result.replace(key,"(" + monkeys[key] + ")")

    print(int(eval(result)))

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    monkeys = {}


    for l in input_lines:
        (a,b) = l.split(": ")

        monkeys[a] = b

    result1 = monkeys["root"].split(" + ")[0]
    result2 = monkeys["root"].split(" + ")[1]
    last_result1 = ""
    last_result2 = ""

    monkeys.pop("humn")
    while last_result2 != result2 or last_result1 != result1:
        last_result1 = result1
        for key in monkeys.keys():
            result1 = result1.replace(key,"(" + monkeys[key] + ")")

        last_result2 = result2
        for key in monkeys.keys():
            result2 = result2.replace(key,"(" + monkeys[key] + ")")


    humn = Symbol('humn')
    print(result1, " = ", str(int(eval(result2))))
    result = result1 + " - " + str(int(eval(result2)))
    solutions = solve(eval(result))
    for s in solutions:
        print(int(s))


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    part1(input_file)
    part2(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
