import re
import scrib
import os
from collections import namedtuple


State = namedtuple("State", "ore_robot clay_robot obs_robot geode_robot ore clay obs geode")


def run_simulation(bp,minutes):

    minute = 1
    initial_state = State(1, 0, 0, 0, 0, 0, 0, 0)
    states = [initial_state]
    max_states = 500000

    while minute <= minutes:
        new_states = []
        for state in states:
            state2 = run_robots(state)
            # check can build ore robot
            if state.ore >= bp.ore_cost_ore:
                new_state = State(state.ore_robot+1,state.clay_robot, state.obs_robot, state.geode_robot, state2.ore - bp.ore_cost_ore, state2.clay, state2.obs, state2.geode)
                new_states.append(new_state)

            # check can build clay robot
            if state.ore >= bp.clay_cost_ore:
                new_state = State(state.ore_robot,state.clay_robot+1, state.obs_robot, state.geode_robot, state2.ore - bp.clay_cost_ore, state2.clay, state2.obs, state2.geode)
                new_states.append(new_state)

            # check can build obs robot
            if state.clay >= bp.obs_cost_clay and state.ore >= bp.obs_cost_ore:
                new_state = State(state.ore_robot,state.clay_robot, state.obs_robot+1, state.geode_robot, state2.ore - bp.obs_cost_ore, state2.clay - bp.obs_cost_clay, state2.obs, state2.geode)
                new_states.append(new_state)

            # check can build geode robot
            if state.obs >= bp.geode_cost_obs and state.ore >= bp.geode_cost_ore:
                new_state = State(state.ore_robot,state.clay_robot, state.obs_robot, state.geode_robot + 1, state2.ore - bp.geode_cost_ore, state2.clay, state2.obs - bp.geode_cost_obs, state2.geode)
                new_states.append(new_state)

            state = run_robots(state)
            new_states.append(state)

        states = new_states
        states.sort(key=lambda s: state_score(bp,s), reverse=True)
        if len(states) > max_states:
            states = states[:max_states]

        # print("Minute {} states {} score {} max geode {}".format(minute,len(states),max([state_score(bp,state) for state in states]),max([state.geode for state in states])))
        # for s in states[:1]:
        #     print(s)
        minute = minute + 1


    return max([state.geode for state in states])


def state_score(bp,s):
    return s.ore_robot + s.obs_robot * 100 + s.clay_robot * 10 + 1000 * s.geode_robot + 10000 * s.geode

    # return s.ore_robot/(bp.ore_cost_ore+bp.clay_cost_ore+bp.obs_cost_ore+bp.geode_cost_ore) + \
    #     s.clay_robot/(bp.obs_cost_clay)  + s.clay_robot/(bp.obs_cost_clay) * s.obs_robot/(bp.geode_cost_obs) + s.geode_robot


def run_robots(state):
    state = State(state.ore_robot, state.clay_robot, state.obs_robot, state.geode_robot, state.ore + state.ore_robot,
                  state.clay + state.clay_robot, state.obs + state.obs_robot, state.geode + state.geode_robot)
    return state


def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    count = 0

    blueprints = []
    Blueprint = namedtuple("Blueprint", "ore_cost_ore clay_cost_ore obs_cost_ore obs_cost_clay geode_cost_ore geode_cost_obs")
    for l in input_lines:
        result = re.findall(r"(\d+)+", l)
        if result is not None:
            params = [int(p) for p in result]
            b = Blueprint(params[1],params[2],params[3],params[4],params[5],params[6])
            blueprints.append(b)
            print(b)
        else:
            raise Exception("Number not found")

    total_mins = 24
    total = 0
    for index,blueprint in enumerate(blueprints):
        result = run_simulation(blueprint,total_mins)
        total = total + result * (index+1)
        print("{} - {}".format(index+1,result))
    print(total)

if __name__ == '__main__':
    d = scrib.find_filename(__file__)
    d = d[:len(d)-3]

    input_file = "./data/" + d + "_input.txt"
    # input_file = "./data/" + d + "_test.txt"
    part1(input_file)
    # 1336 too low
    # 1358 too low
    # 1365 right

    # lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
    # print(scrib.find_most_frequent(lst))
    # print(scrib.find_occurances(lst)[4])
    # print(scrib.find_even(lst))
    # print(scrib.capitalize_words(["python", "javaScript", "c++"]))
    # print(scrib.reverse_list(lst))
