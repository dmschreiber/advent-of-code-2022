import re
import scrib


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    stack = {}
    for i in range(9):
        stack[i] = []

    for row in range(8,-1,-1):
        for col in range(9):
            box = input_lines[row][col*4+1]
            if box != " ":
                stack[col].append(box)


    for item in range(10,len(input_lines)):
        # print(input_lines[item])
        (m,how_many,f,col1,t,col2) = input_lines[item].split()
        (how_many,col1,col2) = (int(how_many),int(col1),int(col2))
        for i in range(how_many):
            a = stack[col1-1].pop()
            stack[col2-1].append(a)

    result = ""
    for i in range(9):
        result = result + stack[i][len(stack[i])-1]

    print(result)

    # part 2
    stack = {}
    for i in range(9):
        stack[i] = []

    for row in range(7, -1, -1):
        for col in range(9):
            box = input_lines[row][col * 4 + 1]
            if box != " ":
                stack[col].append(box)

    for item in range(10, len(input_lines)):
        # print(input_lines[item])
        (m, how_many, f, col1, t, col2) = input_lines[item].split()
        (how_many, col1, col2) = (int(how_many), int(col1), int(col2))

        items = stack[col1-1][len(stack[col1-1])-how_many:]
        # print(how_many,items)

        stack[col1-1] = stack[col1-1][:len(stack[col1-1])-len(items)]

        stack[col2-1].extend(items)


    result = ""
    for i in range(9):
        result = result + stack[i][len(stack[i]) - 1]

    print(result)


if __name__ == '__main__':
    input_file = "./data/day5_input.txt"
    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))