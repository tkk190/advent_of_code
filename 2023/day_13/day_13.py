from utils import lines_of_file
from itertools import zip_longest
def check_next_row(part, value):
    # print('check_next_row', value)
    if value[0] - 1 >= 0 and value[1] + 1 < len(part):
        # print('if 1')
        if part[value[0] - 1] == part[value[1] + 1]:
            # print('if 2')
            return check_next_row(part, [value[0] - 1, value[1] + 1])
        else:
            # print('el 2', value[1] - value[0])
            return 0
            # return value[1] - value[0]
    else:
        # print('el 1', value[1] - value[0])
        if value[0] - 1 >= 0 or value[1] + 1 < len(part):
            return check_next_row(part, [value[0] - 1, value[1] + 1])
        else:
            return value[1] - value[0]

def part_one(file):
    res = 0
    parts = []
    part = []
    for line in lines_of_file(file):
        if line == '':
            parts.append(part)
            part = []
        else:
            part.append(line)
    parts.append(part)
    for part in parts:
        r = 0
        [print(p) for p in part]
        print()
        horizontal = None
        for idx, line in enumerate(part):
            # print(idx, line)
            if idx+1 < len(part):
                if line == part[idx + 1]:
                    horizontal_counter = check_next_row(part, [idx, idx+1])
                    if horizontal is not None and horizontal[1] < horizontal_counter:
                        horizontal = (idx + 1, horizontal_counter)
                    if horizontal is None:
                        horizontal = (idx + 1, horizontal_counter)


                    print(f"{horizontal=}")
        vertical = None
        # print('------')
        # [print(p) for p in part]
        part = [''.join(p) for p in zip_longest(*part)]
        # print('------')
        # [print(p) for p in part]
        # print('------')
        for idx, line in enumerate(part):
            # print(idx, line)
            if idx+1 < len(part):
                if line == part[idx + 1]:
                    vertical_counter = check_next_row(part, [idx, idx+1])
                    if vertical is not None and vertical[1] < vertical_counter:
                        vertical = (idx + 1, vertical_counter)
                    if vertical is None:
                        vertical = (idx + 1, vertical_counter)

                    print(f"{vertical=}")
        # if horizontal is None:
        #     r = vertical[0]
        # elif vertical is None:
        #     r = horizontal[0] * 100
        # else:
        #     if horizontal[1] > vertical[1]:
        #         r = horizontal[0] * 100
        #     else:
        #         r = vertical[0]
        if horizontal is not None and horizontal[1] >= len(part[0]) / 2:
                r = horizontal[0] * 100
        if vertical is not None and vertical[1] >= len(part) / 2:
                r = vertical[0]
        print(r)
        print()
        res += r
    return res


def part_two(file):
    res = 0
    for line in lines_of_file(file):
        ...
    return res


if __name__ == '__main__':
    res = part_one('day_13_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_13_input.txt')
    print(f"Ergebnis 1: {res}")
    assert res == 34202
    # res = part_two('day_13_input_ex.txt')
    # print(f"Beispiel 2: {res}")
    # res = part_two('day_13_input.txt')
    # print(f"Ergebnis 2: {res}")
