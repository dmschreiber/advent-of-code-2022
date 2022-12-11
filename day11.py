import re
import scrib
import os

class Num:
    def __init__(self,n1,n2,op):
        self.n1 = n1
        self.n2 = n2
        self.operator = op

    def print(self):
        print("(",end="")
        if type(self.n1) == int:
            print(self.n1,end="")
        else:
            self.n1.print()
        print(self.operator,end="")
        if type(self.n2) == int:
            print(self.n2,end="")
        else:
            self.n2.print()
        print(")",end="")


def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    monkeys = []

    rounds = 10000
    for i in range(int((len(input_lines)+1)/7)):
        index = i*7

        starting_items = input_lines[index+1].split(": ")[1].split(",")
        starting_items = [int(s) for s in starting_items]

        formula = input_lines[index+2].split(": ")[1].split("= ")[1]
        test_divisible_by = scrib.find_int(input_lines[index+3])
        if_true_throw_to = scrib.find_int(input_lines[index+4])
        if_false_throw_to = scrib.find_int(input_lines[index+5])
        monkeys.append((starting_items,formula,test_divisible_by,if_true_throw_to,if_false_throw_to))

    inspection = []
    for i in range(len(monkeys)):
        inspection.append(0)

    for round in range(rounds):
        print("round {}".format(round))
        for i in range(len(monkeys)):
            inspection[i] = inspection[i] + len(monkeys[i][0])
            for worry in monkeys[i][0]:
                if monkeys[i][1] == "old * old":
                    new_worry = Num(worry, worry, "*")
                elif "*" in monkeys[i][1]:
                    new_worry = Num(worry,scrib.find_int(monkeys[i][1]),"*")
                else:
                    new_worry = Num(worry,scrib.find_int(monkeys[i][1]),"+")
                # new_worry.print()
                # print()
                # new_worry = monkeys[i][1].replace("old",str(worry))
                # print(new_worry)

                if num_divisible_by(new_worry,monkeys[i][2]):
                    monkeys[monkeys[i][3]][0].append(new_worry)
                else:
                    monkeys[monkeys[i][4]][0].append(new_worry)
            monkeys[i] = ([],monkeys[i][1],monkeys[i][2],monkeys[i][3],monkeys[i][4])

    inspection.sort(reverse=True)
    print(inspection[0]*inspection[1])


def num_divisible_by(num,div):
    if num.operator == "*":
        if type(num.n1) == Num:
            t1 = num_divisible_by(num.n1,div)
        else:
            t1 = divisible_by(num.n1,div)
        if type(num.n2) == Num:
            t2 = num_divisible_by(num.n2,div)
        else:
            t2 = divisible_by(num.n2,div)
        return t1 or t2
    elif num.operator == "+":
        if (div-num.n2) == 0:
            return False

        if type(num.n1) == Num:
            t1 = num_divisible_by(num.n1,div-num.n2)
        else:
            t1 = divisible_by(num.n1,div-num.n2)
        if type(num.n2) == Num:
            raise Exception("RHS is a num")

        return t1

def array_divisible_by(nums,div):
    for n in nums:
        if divisible_by(int(n),div):
            return True
    return False


def divisible_by(num,div):
    if div == 0:
        print("is {} divisible by {}".format(num,div))
    if num / div == int(num / div):
        return True
    else:
        return False


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    monkeys = []
    div_by = 3
    rounds = 20
    for i in range(int((len(input_lines)+1)/7)):
        index = i*7

        starting_items = input_lines[index+1].split(": ")[1].split(",")
        starting_items = [int(s) for s in starting_items]
        formula = input_lines[index+2].split(": ")[1].split("= ")[1]
        test_divisible_by = scrib.find_int(input_lines[index+3])
        if_true_throw_to = scrib.find_int(input_lines[index+4])
        if_false_throw_to = scrib.find_int(input_lines[index+5])
        monkeys.append((starting_items,formula,test_divisible_by,if_true_throw_to,if_false_throw_to))

    inspection = []
    for i in range(len(monkeys)):
        inspection.append(0)

    for round in range(rounds):
        print("round {}".format(round))
        for i in range(len(monkeys)):
            inspection[i] = inspection[i] + len(monkeys[i][0])
            for worry in monkeys[i][0]:
                new_worry = eval(monkeys[i][1].replace("old",str(worry)))
                print(new_worry)
                if (div_by > 1):
                    new_worry = int(new_worry / div_by)

                if new_worry / monkeys[i][2] == int(new_worry / monkeys[i][2]):
                    monkeys[monkeys[i][3]][0].append(new_worry)
                else:
                    monkeys[monkeys[i][4]][0].append(new_worry)
            monkeys[i] = ([],monkeys[i][1],monkeys[i][2],monkeys[i][3],monkeys[i][4])

    inspection.sort(reverse=True)
    print(inspection[0]*inspection[1])

#    print(count)

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
