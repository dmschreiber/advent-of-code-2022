import re
import scrib
import os
from collections import namedtuple
from time import time


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    Valve = namedtuple("Valve", "flow_rate to_valves")
    map = {}
    for l in input_lines:
        (a,b) = l.split("; ")
        valve_name = a[6:8]
        flow_rate = scrib.find_int(a)
        to_valves = [v[len(v)-2:] for v in b.split(", ")]
        # print(valve,flow_rate,to_valves)
        map[valve_name] = Valve(flow_rate,to_valves)
    start = "AA"

    total = 30
    # result = list(run_it(map,start,1,total,[]))
    seeking = [('AA', 0, 1), ('DD', 0, 2), ('DD', 20, 3), ('CC', 0, 4), ('BB', 0, 5), ('BB', 13, 6)]

    minute = 1
    states = []
    states.append([('AA', 0, 1)])
    keep_going = True
    max_states = 10000

    while keep_going:
        # print("Before open/close - {}".format(states))
        keep_going = False
        new_states = []
        for state in states:
            # open
            current = state[len(state)-1]
            current_valve = current[0]
            if current[2] <= total:
                # open if not previously open
                if map[current_valve].flow_rate > 0 and current_valve not in [i[0] for i in
                                                                  filter(lambda open: open[1] > 0, state)]:
                    new_state = state.copy()
                    new_state.append((current[0],map[current[0]].flow_rate,current[2]+1))
                    new_states.append(new_state)

                #not open
                new_states.append(state.copy())
                keep_going = True
            else:
                new_states.append(state)

        states = new_states

        # print("Before move - {}".format(states))
        new_states = []
        for state in states:
            current = state[len(state) - 1]
            if current[2] <= total:
                # move to a next valve
                for which in map[current[0]].to_valves:
                    new_state = state.copy()
                    new_state.append((which,0,current[2]+1))
                    new_states.append(new_state)
                keep_going = True

            else:
                new_states.append(state)
        states = new_states

        states.sort(key=lambda s: sum(item[1] * (total + 1 - item[2]) for item in s), reverse=True)
        if len(states) > max_states:
            states = states[:max_states]

    result = states

    total = 30

    result.sort(key=lambda s: sum(item[1] * (total + 1 - item[2]) for item in s), reverse=True)
    print("Got {} results".format(len(result)))
    for index,r in enumerate(result[:1]):
        print(index,sum(item[1] * (total + 1 - item[2]) for item in r), r)


def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    Valve = namedtuple("Valve", "flow_rate to_valves")
    map = {}
    for l in input_lines:
        (a,b) = l.split("; ")
        valve_name = a[6:8]
        flow_rate = scrib.find_int(a)
        to_valves = [v[len(v)-2:] for v in b.split(", ")]
        # print(valve,flow_rate,to_valves)
        map[valve_name] = Valve(flow_rate,to_valves)
    start = "AA"

    total = 26

    minute = 1
    states = []
    State = namedtuple("State","valve_name flow_rate minute actor")
    states.append([State(start, 0, 1, "me"),State(start, 0, 1, "el")])

    keep_going = True
    max_states = 10000

    while keep_going:
        # print("Before open/close - {}".format(states))
        keep_going = False
        new_states = []
        for state in states:
            # open
            for actor in ["me","el"]:
                actor_state = list(filter(lambda s: s.actor==actor,state))
                current = actor_state[len(actor_state)-1]
                current_valve = current.valve_name
                if current.minute <= total:
                    # open if not previously open
                    if map[current_valve].flow_rate > 0 and \
                            current_valve not in [i.valve_name for i in filter(lambda open: open.flow_rate > 0, state)]:
                        new_state = state.copy()
                        new_state.append(State(current.valve_name,map[current.valve_name].flow_rate,current.minute+1,actor))
                        new_states.append(new_state)

                    #not open
                    if state not in new_states:
                        new_states.append(state.copy())
                    keep_going = True
                else:
                    new_states.append(state)

        states = new_states

        # print("Before move - {}".format(states))
        new_states = []
        for state in states:
            for actor in ["me","el"]:
                actor_state = list(filter(lambda s: s.actor==actor,state))
                current = actor_state[len(actor_state) - 1]
                if current.minute <= total:
                    # print("Before move - {}".format(state))
                    # move to a next valve
                    for which in map[current.valve_name].to_valves:
                        new_state = state.copy()
                        new_state.append(State(which,0,current.minute+1,actor))
                        new_states.append(new_state)
                        # print("After move - {}".format(new_state))
                    keep_going = True

                elif len(list(filter(lambda s: s.minute==current.minute,state)))==2:
                    if state not in new_states:
                        new_states.append(state)

        states = new_states

        states.sort(key=lambda s: sum(item[1] * (total + 1 - item[2]) for item in s), reverse=True)
        if len(states) > max_states:
            states = states[:max_states]

        print("After round {}".format(len(states)))

    result = states

    total = 26

    result.sort(key=lambda s: sum(item[1] * (total + 1 - item[2]) for item in s), reverse=True)
    print("Got {} results".format(len(result)))
    for index,r in enumerate(result[:1]):
        print(index,sum(item[1] * (total + 1 - item[2]) for item in r))
        for min in range(1,30):
            print("Minute {}, {}".format(min,list(filter(lambda s: s.minute==min,r))))


if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # part1(input_file)

    start = time()
    input_file = "./data/" + d + "_test.txt"
    part2(input_file)
    print("elapsed {}".format(time()-start))

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
