import re
from utils import lines_of_file
from math import lcm
def part_one(file):
    res = 0
    lines = [l for l in lines_of_file(file)]
    instructions = lines[0]
    map = {}
    for line in lines[2:]:
        values = re.findall('[A-Z]{3}', line)
        map[values[0]] = (values[1], values[2])
    current_key = 'AAA'
    while True:
        for direction in instructions:
            if current_key == 'ZZZ':
                break
            res += 1
            if direction == 'L':
                current_key = map[current_key][0]
            elif direction == 'R':
                current_key = map[current_key][1]
            else:
                raise Exception('no direction')
        if current_key == 'ZZZ':
            break
    return res

def part_two2(file):
    results = []
    lines = [l for l in lines_of_file(file)]
    instructions = lines[0]
    map = {}
    for line in lines[2:]:
        m = re.match(r'([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)', line)
        map[m.group(1)] = (m.group(2), m.group(3))
    current_keys = [k for k in map.keys() if k.endswith('A')]
    for current_key in current_keys:
        result = 0
        while True:
            for direction in instructions:
                if current_key.endswith('Z'):
                    break
                result += 1
                if direction == 'L':
                    current_key = map[current_key][0]
                elif direction == 'R':
                    current_key = map[current_key][1]
                else:
                    raise Exception('no direction')
            if current_key.endswith('Z'):
                break
        results.append(result)
    return lcm(*results)

if __name__ == '__main__':
    res = part_one('day_8_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_8_input_ex2.txt')
    print(f"Beispiel 1b: {res}")
    res = part_one('day_8_input.txt')
    print(f"Ergebnis 1: {res}")
    res = part_two2('day_8_input_ex3.txt')
    print(f"Beispiel 2: {res}")
    res = part_two2('day_8_input.txt')
    print(f"Ergebnis 2: {res}")
