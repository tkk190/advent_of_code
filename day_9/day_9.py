from day_9_input import input
from pprint import pprint
import os
from time import sleep

input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

def readable(vars, idx, height_list, width_list):
    new_vars = []
    for i, j in enumerate(vars):
        if j == 0:
            new_vars.append('.')
        else:
            new_vars.append('#')
    for width, height in zip(width_list, height_list):
        if height == idx:
            new_vars[width] = 'X'
    return new_vars

def print_field(height_list, width_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    # print('='*(field_width+field_width-1))
    print('='*(field_width))
    for idx, t in enumerate(t_field.values()):
        # if height - 10 < idx < height + 10:
        print(''.join(readable(t.values(), idx, height_list, width_list)))
    # print('='*(field_width+field_width-1))
    print('='*(field_width))
    sleep(0.05)

def check_move_direction(right, right_before):
    # direction = ''
    # direction_before = ''
    # if right in 'UD':
    #     direction = 'UD'
    # elif right in 'LR':
    #     direction = 'LR'
    # if right_before in 'UD':
    #     direction_before = 'UD'
    # elif right_before in 'LR':
    #     direction_before = 'LR'
    # return direction == direction_before
    # print(right == right_before)
    return right == right_before

def check_distance(t_height, t_width, height, width, right):
    distance = abs(t_height - height) + abs(t_width - width)
    if right in 'UD':
        if t_width != width:
            if distance >= 1:
                return True
            else:
                return False
    elif right in 'LR':
        if t_height != height:
            if distance >= 1:
                return True
            else:
                return False

    # print('h_pos', height, width)
    # print('t_pos', t_height, t_width)
    # print('distance', distance)
    #return distance > 1
    return True

if __name__ == '__main__':
    # get field-size
    max_u = 0
    max_d = 0
    max_l = 0
    max_r = 0
    height = 0
    width = 0
    for i in input.splitlines():
        [right, steps] = i.split(' ')
        steps = int(steps)
        match right:
            case 'U':
                height += steps
                if height > max_u:
                    max_u = height
            case 'D':
                height -= steps
                if height < max_d:
                    max_d = height
            case 'R':
                width += steps
                if width > max_r:
                    max_r = width
            case 'L':
                width -= steps
                if width < max_l:
                    max_l = width
    # print('u', max_u)
    # print('d', max_d)
    # print('l', max_l)
    # print('r', max_r)
    field_height = abs(max_u) + abs(max_d) + 1 + 20
    field_width = abs(max_l) + abs(max_r) + 1 + 20
    # print('field', field_height, field_width)
    start_height = abs(max_u)
    start_width = abs(max_l)
    field = {}
    t_field = {}
    for i in range(field_height):
        field[i] = {}
        t_field[i] = {}
        for j in range(field_width):
            field[i][j] = 0
            t_field[i][j] = 0

    # print(field)
    height = start_height
    width = start_width
    t_height = height
    t_width = width
    # print('start pos', height, width)
    right_before = ''
    height_list = [height]*10
    width_list = [width]*10
    t_height_list = [t_height]*10
    t_width_list = [t_width]*10
    for i in input.splitlines():
        # print(height, width)
        [right, steps] = i.split(' ')
        steps = int(steps)
        for i in range(1, steps+1):
            height = height_list.pop(0)
            width = width_list.pop(0)
            t_height = t_height_list.pop(0)
            t_width = t_width_list.pop(0)
            if i > 1:
                if check_move_direction(right, right_before) and check_distance(t_height, t_width, t_height_list[0], t_width_list[0], right):
                    t_height = t_height_list[0]
                    t_width = t_width_list[0]
            else:
                if check_move_direction(right, right_before):
                    t_height = t_height_list[0]
                    t_width = t_width_list[0]

            height = height_list[-1]
            width = width_list[-1]

            match right:
                case 'U':
                    height -= 1
                case 'D':
                    height += 1
                case 'R':
                    width += 1
                case 'L':
                    width -= 1
            field[height][width] = 1
            t_field[t_height][t_width] = 1

            right_before = right
            height_list.append(height)
            width_list.append(width)
            t_height_list.append(t_height)
            t_width_list.append(t_width)
            # print(height_list)
            print_field(height_list, width_list)

    result_a = 0
    for f in t_field.values():
        result_a += sum(f.values())

    print(f"Ergebnis 1: {result_a}")
    # 6029 too low

    print(f"Ergebnis 2: {result_a}")
    # 882 too low
    # 2211 too low
    # 6154 too high

