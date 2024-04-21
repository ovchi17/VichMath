import math
import os
import random
import re
import sys


def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return pow(args[0], 2) * pow(args[1], 2) - 3 * pow(args[0], 3) - 6 * pow(args[1], 3) + 8


def fourth_function(args: []) -> float:
    return pow(args[0], 4) - 9 * args[1] + 2


def fifth_function(args: []) -> float:
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1


def six_function(args: []) -> float:
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2


def seven_function(args: []) -> float:
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
def get_new(e, cur_values, n, func):
    result = []
    for x in range(n):
        diff_val = func[x](cur_values) * e
        result.append(cur_values[x] - diff_val)
    return result

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations, e=0.00001, mx=5000):
    func = get_functions(system_id)
    iteration_counter = 0
    cur_values = initial_approximations
    while iteration_counter < mx:
        updated_values = get_new(0.00005, cur_values, number_of_unknowns, func)
        checker = True
        for i in range(number_of_unknowns):
            if e < (abs(cur_values[i] - updated_values[i])):
                checker = False
        if checker == True:
            return updated_values
        else:
            cur_values = updated_values
            iteration_counter = iteration_counter + 1
    return updated_values


def tests():
    system_id1 = 1
    number_of_unknowns1 = 2
    initial_approximations1 = [0.5, 0.5]
    ms_test1 = solve_by_fixed_point_iterations(system_id1, number_of_unknowns1, initial_approximations1)
    rounded_ms_test1 = list(map(lambda x: round(x, 3), ms_test1))
    if (rounded_ms_test1 == [0.393, 0.473]):
        print("test1 passed(system_id 1)")
    system_id2 = 2
    number_of_unknowns2 = 2
    initial_approximations2 = [1.0, 1.0]
    ms_test2 = solve_by_fixed_point_iterations(system_id2, number_of_unknowns2, initial_approximations2)
    rounded_ms_test2 = list(map(lambda x: round(x, 3), ms_test2))
    if (rounded_ms_test2 == [1, 1.013]):
        print("test2 passed(system_id 2)")
    system_id3 = 3
    number_of_unknowns3 = 3
    initial_approximations3 = [0.0, 0.0, 0.0]
    ms_test3 = solve_by_fixed_point_iterations(system_id3, number_of_unknowns3, initial_approximations3)
    rounded_ms_test3 = list(map(lambda x: round(x, 3), ms_test3))
    if (rounded_ms_test3 == [0.022, -0.045, 0.066]):
        print("test3 passed(system_id 3)")
    system_id4 = 1
    number_of_unknowns4 = 2
    initial_approximations4 = [-0.5, 1.0]
    ms_test4 = solve_by_fixed_point_iterations(system_id4, number_of_unknowns4, initial_approximations4)
    rounded_ms_test4 = list(map(lambda x: round(x, 3), ms_test4))
    if (rounded_ms_test4 == [-0.5, 1]):
        print("test4 passed(1 negative in initial approximation)")
    system_id5 = 1
    number_of_unknowns5 = 2
    initial_approximations5 = [-0.5, -1.0]
    ms_test5 = solve_by_fixed_point_iterations(system_id5, number_of_unknowns5, initial_approximations5)
    rounded_ms_test5 = list(map(lambda x: round(x, 3), ms_test5))
    if (rounded_ms_test5 == [-0.5, -1]):
        print("test5 passed(2 negatives in initial approximation)")



if __name__ == '__main__':
    tests()