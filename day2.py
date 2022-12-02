import re
import scrib

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    list_input = []
    scores = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
    # 0, loss, 3, draw, 6, win
    # X lose, Y draw, Z win
    outcome = {"AX":"C", "AY":"A", "AZ":"B", "BX":"A", "BY":"B", "BZ":"C", "CX":"B", "CY":"C", "CZ":"A"}
    result = {"X":0, "Y":3, "Z":6}

    for l in input_lines:
        list_input.append(l.split())
    total_score = 0

    for d in list_input:
        (a,b) = d
        mine = scores[outcome[a+b]]
        score = result[b]

        total_score = total_score + score + mine
    print(total_score)


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    list_input = []
    scores = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
    outcome = {"AX":3, "AY":6, "AZ":0, "BX":0, "BY":3, "BZ":6, "CX":6, "CY":0, "CZ":3}
    # 0, loss, 3, draw, 6, win

    for l in input_lines:
        list_input.append(l.split())
    total_score = 0
    for d in list_input:
        (a,b) = d
        score = outcome[a+b]
        total_score = total_score + score + scores[b]

    print(total_score)

    # dirs = [d for (d,v) in list_input]
    # print(dirs)

if __name__ == '__main__':
    input = "./data/day2_input.txt"
    part1(input)
    part2(input)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))