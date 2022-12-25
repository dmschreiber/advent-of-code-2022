import re
import scrib
import os
from collections import namedtuple


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    num = 0

    Point = namedtuple("Point", "x y")
    for l in input_lines:
        num = num + convert_from_snafu(l)

    print(convert_to_snafu(num))

snafu_digits = ["=","-","0","1","2"]
snafu_digits_values = [-2,-1,0,1,2]

def convert_from_snafu(number):

    result = 0
    for index,d in enumerate(number[::-1]):
        result = result + 5 ** index * snafu_digits_values[snafu_digits.index(d)]

    return result
def convert_to_snafu(n):
    b = 5
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b

    num = ""
    carry = 0
    for d in digits:
        n = d + carry

        if n == 5:
            n = 0
            carry = 1
        else:
            carry = 0

        if n in [0,1,2]:
            num = str(n) + num
        elif n in [3,4]:
            carry = 1
            if n == 3:
                num = "=" + num
            else:
                num = "-" + num

    if carry > 0:
        num = "1" + num

    return num

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"

    if convert_from_snafu("1=11-2")==2022 and convert_to_snafu(2022)=="1=11-2":
        print("Success")
    else:
        exit(-1)

    part1(input_file)

