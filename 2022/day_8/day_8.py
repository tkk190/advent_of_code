from day_8_input import input

t_input = """30373
25512
65332
33549
35390
"""

def is_seen(row, idx, reverse = False):
    if reverse:
        row = list(reversed(row))
        idx = len(row)-1-idx
    return True if max(row[:idx]) < row[idx] else False

def check_view(field, row, idx_row, idx_col):
    res = 0
    if idx_col in [0, len(field)-1] or idx_row in [0, len(field)-1]:
        return res
    new_row = [i[idx_col] for i in field]
    if is_seen(row, idx_col)\
            or is_seen(row, idx_col, reverse = True)\
            or is_seen(new_row, idx_row)\
            or is_seen(new_row, idx_row, reverse = True):
        res = 1
    return res

def count_seen(row, idx, reverse = False):
    if reverse:
        row = list(reversed(row))
        idx = len(row)-1-idx
    counter = 0
    for i in reversed(row[:idx]):
        if i >= row[idx]:
            counter += 1
            break
        else:
            counter += 1
    return counter

def count_trees(field, row, idx_row, idx_col):
    if idx_col in [0, len(field)-1] or idx_row in [0, len(field)-1]:
        return 0
    new_row = [i[idx_col] for i in field]
    res = count_seen(row, idx_col)
    res *= count_seen(row, idx_col, reverse = True)
    res *= count_seen(new_row, idx_row)
    res *= count_seen(new_row, idx_row, reverse = True)
    return res

if __name__ == '__main__':
    field = []
    for i in input.splitlines():
        field.append([int(j) for j in i])
    res_a = len(field)*2 + (len(field)-2)*2
    res_b = 0
    for idx_row, row in enumerate(field):
        for idx_col, col in enumerate(row):
            if check_view(field, row, idx_row, idx_col):
                res_a += 1
            local_res_b = count_trees(field, row, idx_row, idx_col)
            if res_b < local_res_b:
                res_b = local_res_b

    print(f"Ergebnis 1: {res_a}") # 1776
    print(f"Ergebnis 2: {res_b}") # 234416
