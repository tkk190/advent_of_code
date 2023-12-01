import re
from utils import lines_of_file

translation = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven':'7',
    'eight': '8',
    'nine': '9'
}

def part_one(file):
    res = 0
    for line in lines_of_file(file):
        number_string = re.sub('[A-Za-z]', '', line)
        res += int(number_string[0] + number_string[-1])
    return res

def part_two(file):
    res = 0
    for line in lines_of_file(file):
        regex_res = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        string_number = [b if b not in translation else translation[b] for b in regex_res]
        res += int(string_number[0] + string_number[-1])
    return res

if __name__ == '__main__':
    res = part_one('day_1_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_1_input.txt')
    print(f"Ergebnis 1: {res}")
    res = part_two('day_1_input_ex2.txt')
    print(f"Beispiel 2: {res}")
    res = part_two('day_1_input.txt')
    print(f"Ergebnis 2: {res}")

