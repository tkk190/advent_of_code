import re
from utils import lines_of_file

def part_one(file):
    res = 0
    colors = {'red': 12, 'green': 13, 'blue': 14}
    for line in lines_of_file(file):
        game, game_results = line.split(':')
        game_id = int(game.replace('Game ', ''))
        game_result = game_results.split(';')
        for result in game_result:
            for color, maximum in colors.items():
                color_results = re.findall(f'[0-9]* {color}', result)
                color_sum = sum([int(res.replace(f' {color}', '')) for res  in color_results])
                if color_sum > maximum:
                    break
            else:
                continue
            break
        else:
            res += game_id
            continue
    return res


def part_two(file):
    res = 0
    colors = {'red': 12, 'green': 13, 'blue': 14}
    for line in lines_of_file(file):
        game, game_results = line.split(':')
        game_result = game_results.split(';')
        product = 1
        minimal_cubes = {'red': 1, 'green': 1, 'blue': 1}
        for result in game_result:
            for color, maximum in colors.items():
                color_results = re.findall(f'[0-9]* {color}', result)
                color_sum = sum([int(res.replace(f' {color}', '')) for res in color_results])
                if color_sum > minimal_cubes[color]:
                    minimal_cubes[color] = color_sum
        for value in minimal_cubes.values():
            product *= value
        res += product
    return res


if __name__ == '__main__':
    res = part_one('day_2_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_2_input.txt')
    print(f"Ergebnis 1: {res}")
    res = part_two('day_2_input_ex.txt')
    print(f"Beispiel 2: {res}")
    res = part_two('day_2_input.txt')
    print(f"Ergebnis 2: {res}")
