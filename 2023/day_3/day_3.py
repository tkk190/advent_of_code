from utils import lines_of_file
import re

def check_special_character(gear, line_part, idx, check_range):
    special_character = re.findall('[^0-9.]', line_part)
    if len(special_character) > 0:
        gear['line'] = idx - 1
        gear['position'] = line_part.index(special_character[0]) + check_range.start
        if special_character[0] == '*':
            gear['is_gear'] = True
    return gear

def run(file):
    res_1 = 0
    res_2 = 0
    lines = [l for l in lines_of_file(file)]
    gears = {}
    for idx, line in enumerate(lines):
        numbers = re.findall('[0-9]+', line)
        for number in numbers:
            gear = {'is_gear': False, 'line': -1, 'position': -1}
            start_index = line.index(number)
            stop_index = start_index + len(number)
            check_range = range(start_index - 1, stop_index + 1)
            if check_range.start < 0:
                check_range = range(0 , check_range.stop)
            if check_range.stop > len(line) - 1:
                check_range = range(check_range.start, len(line))

            if idx > 0:
                check_before = lines[idx - 1][check_range.start:check_range.stop]
                gear = check_special_character(gear, check_before, idx - 1, check_range)

            check_current = line[check_range.start:check_range.stop]
            gear = check_special_character(gear, check_current, idx, check_range)

            if idx + 1 < len(lines):
                check_after = lines[idx + 1][check_range.start:check_range.stop]
                gear = check_special_character(gear, check_after, idx + 1, check_range)

            if gear['line'] >= 0 and gear['position'] >= 0:
                res_1 += int(number)
                if gear['is_gear'] is True:
                    gear_name = f"{gear['line']}-{gear['position']}"
                    if gear_name in gears:
                        res_2 += gears[gear_name] * int(number)
                    else:
                        gears[gear_name] = int(number)

            # handle double numbers
            line = line.replace(number, '0' * len(number), 1)

    return res_1, res_2


if __name__ == '__main__':
    res_1, res_2 = run('day_3_input_ex.txt')
    print(f"Beispiel 1: {res_1}")
    print(f"Beispiel 2: {res_2}")
    res_1, res_2 = run('day_3_input.txt')
    print(f"Ergebnis 1: {res_1}")
    print(f"Ergebnis 2: {res_2}")

