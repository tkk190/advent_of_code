import re
from utils import lines_of_file

def run(file):
    res_a = 0
    copies = {}

    for line in lines_of_file(file):
        line_result_a = 0
        line_result_b = 0
        card, numbers = line.split(':')
        card_id = re.findall('[0-9]+', card)[0]
        if card_id not in copies:
            copies[card_id] = 1
        winning_numbers_string, check_numbers_string = numbers.split('|')
        winning_numbers = re.findall('[0-9]+', winning_numbers_string)
        check_numbers = re.findall('[0-9]+', check_numbers_string)
        for check_number in check_numbers:
            if check_number in winning_numbers:
                if line_result_a == 0:
                    line_result_a = 1
                else:
                    line_result_a *= 2
                line_result_b += 1
        for i in range(line_result_b):
            new_key = str(int(card_id) + i + 1)
            if new_key in copies:
                copies[new_key] += copies[card_id]
            else:
                copies[new_key] = 1  + copies[card_id]
        res_a += line_result_a
    return res_a, sum(copies.values())


if __name__ == '__main__':
    res_1, res_2 = run('day_4_input_ex.txt')
    print(f"Beispiel 1: {res_1}")
    print(f"Beispiel 2: {res_2}")
    res_1, res_2 = run('day_4_input.txt')
    print(f"Ergebnis 1: {res_1}")
    print(f"Ergebnis 2: {res_2}")