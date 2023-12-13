from utils import lines_of_file
import re
from time import perf_counter
from copy import deepcopy

prev_arrays = {}

def combinationsx(array, count, prev_array=None):
    if prev_array is None:
        prev_array = array
    else:
        if len(prev_array[0]) == count:
            return prev_array
    if len(prev_array[0]) + 1 in prev_arrays:
        return combinationsx(array, count, prev_arrays[len(prev_array[0])+1])
    print(prev_arrays.keys())
    new_array = []
    for a in prev_array:
        for b in array:
            new_array.append(a+b)
    prev_arrays[len(new_array[0])] = new_array
    print(new_array)
    return combinationsx(array, count, new_array)


def part_one(file):
    res = 0
    combination_dict = {}
    i = 0
    for line in lines_of_file(file):
        print(i)
        springs, number_string = line.split(' ')
        numbers = number_string.split(',')
        numbers = [int(n)for n in numbers]
        unknown_count = springs.count('?')
        if unknown_count in combination_dict:
            char_combinations = combination_dict[unknown_count]
        else:
            char_combinations = combinationsx('.#', unknown_count)
            combination_dict[unknown_count] = char_combinations

        regex_pattern = '^\.*' + ''.join([f'#{{{n}}}\.+' for n in numbers])[:-1] + '*$'
        prog = re.compile(regex_pattern, flags=re.MULTILINE)
        combination_string = ''
        for char_combination in char_combinations:
            temp_springs = springs
            for char in char_combination:
                temp_springs = temp_springs.replace('?', char, 1)
            combination_string += temp_springs + '\n'
        regex_result = prog.findall(combination_string)
        res += len(regex_result)
        i += 1
    return res

def ranger(value, counter):
    for i in range(value):
        if i.bit_count() == counter:
            yield i
def part_two(file):
    res = 0
    i = 0
    combination_dict = {}
    lines = [l for l in lines_of_file(file)]
    for line in lines:
        print(i)
        r = 0
        springs, number_string = line.split(' ')
        numbers = number_string.split(',')
        # numbers = [int(n)for n in numbers]
        numbers = [int(n)for n in numbers]*5
        springs = '?'.join([springs]*5)
        sum_numbers = sum(numbers)
        orig_counter = springs.count('#')

        unknown_count = springs.count('?')

        regex_pattern = '^\.*' + ''.join([f'#{{{n}}}\.+' for n in numbers])[:-1] + '*$'
        prog = re.compile(regex_pattern, flags=re.MULTILINE)
        counter = 2**unknown_count
        bit_check = sum_numbers - orig_counter
        for k in ranger(counter, bit_check):
            # if k % 10_000_000 == 0:
            #     print(round(100*k/counter, 2))
        # for k in range(10):
            char_combination = str(bin(k))[2:].zfill(unknown_count)
            temp_springs = springs
            for char in char_combination:
                if char == '0':
                    temp_springs = temp_springs.replace('?', '.', 1)
                else:
                    temp_springs = temp_springs.replace('?', '#', 1)
            if temp_springs.count('#') == sum_numbers:
                regex_result = prog.match(temp_springs)
                if regex_result is not None:
                    r += 1
        print(i, r)
        i += 1
        res += r
    return res



if __name__ == '__main__':
    s = perf_counter()
    # res = part_one('day_12_input_ex.txt')
    # print(f"Beispiel 1: {res}")
    # res = part_one('day_12_input.txt')
    # print(f"Ergebnis 1: {res}")
    res = part_two('day_12_input_ex.txt')
    print(f"Beispiel 2: {res}")
    # res = part_two('day_12_input.txt')
    # print(f"Ergebnis 2: {res}")
    print(perf_counter() - s)
