import re
import scrib
import os

def print_state(x,cycle,output):
    print("during cycle {}".format(cycle))
    if cycle <= 22:
        print(output[:20])
        print("".join((["."]*(x-2))),end="")
        print("###",end="")
        print("".join((["."]*(20-x))),end="")
        print()
        print("".join((["."] * (cycle - 1))), end="")
        print("#", end="")
        print("".join((["."] * (20 - cycle ))), end="")
        print()


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    x = 1
    cycle = 0
    total_ss = 0
    which = [20,60,100,140,180,220]

    output = ""
    for l in input_lines:
        cycle = cycle + 1
        if cycle in which:
            total_ss = total_ss + cycle * x

        output = create_output(cycle, output, x)

        if l != "noop":
            (a,b) = l.split()
            (a,b) = (a,int(b))
            cycle = cycle + 1

            if cycle in which:
                total_ss = total_ss + cycle * x

            output = create_output(cycle, output, x)

            x = x + b

    ##..##..##..##..##..##..##..##..##..##..
    ##..##..##..##..##.##..##..##..##..##...
    print(total_ss)
    print(output[:40])
    print(output[40:80])
    print(output[80:120])
    print(output[120:160])
    print(output[160:200])
    print(output[200:240])
    #10160 wrong 10:30
    #14780 wrong 12:20
    # right part 1 in 29:36
    # right part 2 in 1:33:00


def create_output(cycle, output, x):
    if x - 1 <= (cycle - 1) % 40 <= x + 1:
        output = output + "#"
    else:
        output = output + " "
    return output


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/day10_test.txt"

    part1(input_file)
