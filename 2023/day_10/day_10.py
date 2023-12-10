from utils import lines_of_file

direction_map = {
    '|': (1,0),
    '-': (0,1),
    'L': (1,1),
    'J': (1,-1),
    '7': (-1,-1),
    'F': (-1,1),
    '.': (None, None),
}
current_direction = ''
possible_directions = {
    'n': (-1,0),
    'e': (0,1),
    's': (1,0),
    'w': (0, -1)
}
def run(file):
    res_a = 0
    lines = [l for l in lines_of_file(file)]
    for idx, line in enumerate(lines):
        if 'S' in line:
            start_position = (idx, line.find('S'))
    positions = {}
    for current_direction in possible_directions:
        local_positions = {}
        current_position = start_position
        start_direction = ''
        i = 0
        while True:
            if start_direction not in ['n', 's']:
                start_direction = current_direction
            new_position = tuple(map(sum, zip(current_position, possible_directions[current_direction])))

            if not all(p >= 0 for p in new_position):
                break
            next_field = lines[new_position[0]][new_position[1]]
            if next_field == '.':
                break
            if next_field == 'S':
                if i+1 > res_a:
                    res_a = i+1
                    positions = local_positions
                break
            new_direction = None
            x_direction = None
            if next_field in ['|', '-']:
                if next_field == '|' and current_direction in ['n', 's']:
                   x_direction = current_direction

                if next_field == '-' and current_direction not in ['e', 'w']:
                    break
                elif next_field == '-' and current_direction in ['e', 'w']:
                   x_direction = 'v'
                new_direction = current_direction

            if next_field in ['L', 'J', '7', 'F']:
                if current_direction == 'n':
                    if next_field == '7':
                        new_direction = 'w'
                    elif next_field == 'F':
                        new_direction = 'e'
                    x_direction = 'n'
                elif current_direction == 's':
                    if next_field == 'L':
                        new_direction = 'e'
                    elif next_field == 'J':
                        new_direction = 'w'
                    x_direction = 's'
                elif current_direction == 'e':
                    if next_field == 'J':
                        new_direction = 'n'
                        x_direction = 'n'
                    if next_field == '7':
                        new_direction = 's'
                        x_direction = 's'
                elif current_direction == 'w':
                    if next_field == 'L':
                        new_direction = 'n'
                        x_direction = 'n'
                    if next_field == 'F':
                        new_direction = 's'
                        x_direction = 's'
            if new_direction is None:
                break
            current_direction = new_direction
            current_position = new_position
            i += 1
            if x_direction is not None:
                if current_position[0] in local_positions:
                    local_positions[current_position[0]].append((current_position[1], x_direction))
                else:
                    local_positions[current_position[0]] = [(current_position[1], x_direction)]

    for row, columns in positions.items():
        positions[row] = sorted(positions[row])

    res_b = 0
    for row, columns in positions.items():
        row_count = 0
        start_value = 0
        last_direction = ''
        opened = False
        remove_counter = 0
        start_direction = ''
        for idx, column in enumerate(columns):
            value, direction = column
            if direction in ['s', 'n'] and start_direction == '':
                start_direction = direction
            if direction == start_direction:
                opened = True
            if (start_direction == 'n' and direction == 's') or (start_direction == 's' and direction == 'n'):
                opened = False
            if idx == 0:
                start_value = value
            else:
                if last_direction == direction or direction == 'v':
                    start_value = value
                else:
                    if value - start_value > 1 and opened is False:
                        res_b += value - start_value - 1 - remove_counter
                        row_count += value - start_value - 1 - remove_counter
                    start_value = value
            last_direction = direction

    return int(res_a/2), res_b


if __name__ == '__main__':
    res_1, res_2 = run('day_10_input_ex.txt')
    print(f"Beispiel 1a {res_1}")
    print(f"Beispiel 2a: {res_2}")
    res_1, res_2 = run('day_10_input_ex2.txt')
    print(f"Beispiel 1b {res_1}")
    print(f"Beispiel 2b: {res_2}")
    res_1, res_2 = run('day_10_input_ex3.txt')
    print(f"Beispiel 1c {res_1}")
    print(f"Beispiel 2c: {res_2}")
    res_1, res_2 = run('day_10_input_ex4.txt')
    print(f"Beispiel 1d {res_1}")
    print(f"Beispiel 2d: {res_2}")
    res_1, res_2 = run('day_10_input.txt')
    print(f"Ergebnis 1: {res_1}")
    print(f"Ergebnis 2: {res_2}")
