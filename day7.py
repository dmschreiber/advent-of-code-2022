import re
import scrib

def get_size(dir,dirs, which):
    # print("get_size {}".format(which))
    total = 0
    if which in dir.keys():
        total = total + dir[which]
    if which in dirs.keys():
        for d in dirs[which]:
            total = total + get_size(dir,dirs,d)
    return total

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0
    path = "/"
    dir = {}
    dirs = {}
    read = False
    for l in input_lines:
        items = l.split()

        if items[0] == "$":
            read = False

        if read:
            if items[0] == "dir":
                if path in dirs.keys():
                    if path == "/":
                        dirs[path].append(path + items[1])
                    else:
                        dirs[path].append(path + "/" + items[1])
                else:
                    if path == "/":
                        dirs[path] = [path + items[1]]
                    else:
                        dirs[path] = [path + "/" + items[1]]

            elif path in dir.keys():
                dir[path] = dir[path] + int(items[0])
            else:
                dir[path] = int(items[0])

        elif items[0] == "$":
            if items[1] == "cd":
                if items[2] == "..":
                    path = path[:path.rindex("/")]

                elif items[2] == "/":
                    path = "/"
                elif path == "/":
                    path = "/" + items[2]
                else:
                    path = path + "/" + items[2]

            elif items[1] == "ls":
                read = True

    total = 0

    all_dirs = list(dir.keys())
    all_dirs.extend(list(dirs.keys()))
    all_dirs = set(all_dirs)
    all_dirs = list(all_dirs)

    for d in all_dirs:
        if get_size(dir, dirs, d) < 100000:
            total = total + get_size(dir, dirs, d)


    print(total)

    target = 30000000 - (70000000 - get_size(dir,dirs,"/"))
    options = []
    for d in all_dirs:
        if get_size(dir, dirs, d) > target:
            options.append(get_size(dir, dirs, d))
    options.sort()
    print(options[0])


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/day7_test.txt"
    part1(input_file)

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))

    # 1965010 wrong
    # 1911578 wrong
    # 1107954 wrong
    # 1419848 wrong
    # try 1348005
