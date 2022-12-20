from day_5_input import input, field as def_field
from pprint import pprint
FIELD_ROWS = 9

# def_field = """
#     [D]
# [N] [C]
# [Z] [M] [P]
# """
# FIELD_ROWS = 3
# input = """move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """

if __name__ == "__main__":
    field = {}
    field_b = {}
    for i in range(FIELD_ROWS):
        field[i+1] = []
        field_b[i+1] = []
    for idx, i in enumerate(reversed(def_field.splitlines())):
        if i != '':
            for j in range(FIELD_ROWS):
                if i[j*4+1] != ' ':
                    field[j+1].append(i[j*4+1])
                    field_b[j+1].append(i[j*4+1])
    for i in input.splitlines():
        i_list = i.split(' ')
        s_move = int(i_list[1])
        s_from = int(i_list[3])
        s_to = int(i_list[5])
        move_idx = -1*s_move
        field[s_to].extend(reversed(field[s_from][move_idx:]))
        field[s_from] = field[s_from][:move_idx]

        field_b[s_to].extend(field_b[s_from][move_idx:])
        field_b[s_from] = field_b[s_from][:move_idx]
    result = ''
    result_b = ''
    for i in field.values():
        result += i[-1]
    for i in field_b.values():
        result_b += i[-1]

    print(f'Ergebnis 1: {result}')
    print(f'Ergebnis 2: {result_b}')




