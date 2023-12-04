import re
from utils import lines_of_file

def part_one(file):
    res = 0
    for line in lines_of_file(file):
        line_result = 0
        card, numbers = line.split(':')
        winning_numbers_string, check_numbers_string = numbers.split('|')
        winning_numbers = re.findall('[0-9]+', winning_numbers_string)
        check_numbers = re.findall('[0-9]+', check_numbers_string)
        for check_number in check_numbers:
            if check_number in winning_numbers:
                if line_result == 0:
                    line_result = 1
                else:
                    line_result *= 2
        res += line_result
    return res


def part_two(file):
    res = 0
    for line in lines_of_file(file):
        ...
    return res


if __name__ == '__main__':
    res = part_one('day_4_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_4_input.txt')
    print(f"Ergebnis 1: {res}")
    # res = part_two('day_4_input_ex.txt')
    # print(f"Beispiel 2: {res}")
    # res = part_two('day_4_input.txt')
    # print(f"Ergebnis 2: {res}")
