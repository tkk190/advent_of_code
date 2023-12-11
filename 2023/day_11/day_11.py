from utils import lines_of_file

def part_one(file):
    res = 0
    new_lines = []
    for line in lines_of_file(file):
        if '#' not in line:
            new_lines.append(line)
        new_lines.append(line)
    rows = [0] * len(new_lines[0])
    for line in new_lines:
        for idx, letter in enumerate(line):
            if letter == '#':
                rows[idx] += 1
    # print('lines created')
    lines = []
    i = 1
    galaxies = {}
    for row_idx, line in enumerate(new_lines):
        new_row = []
        appended_cols = 0
        for col_idx, (counter, letter) in enumerate(zip(rows, line)):
            if counter == 0:
                new_row.append('.')
                appended_cols += 1
            if letter == '#':
                letter = i
                galaxies[i] = (row_idx, col_idx + appended_cols)
                i += 1
            new_row.append(letter)
        lines.append(new_row)
    # print('rows created')
    # [print(line) for line in lines]
    # print()
    min_lengths = []
    pairs = []
    for galaxy_from, coords_from in galaxies.items():
        lengths = []
        # print(galaxy_from, coords_from)
        for galaxy_to, coords_to in galaxies.items():
            if galaxy_to != galaxy_from:
                length_a = abs(coords_from[0] - coords_to[0])
                length_b = abs(coords_from[1] - coords_to[1])
                length = length_a + length_b
                lengths.append(length)

                # print(f"{galaxy_from}-{galaxy_to}", length)
                pair = '-'.join(sorted([str(galaxy_from), str(galaxy_to)]))
                if pair not in pairs:
                    min_lengths.append(length)
                    pairs.append(pair)

    return sum(min_lengths)


def run(file, factor):
    empty_rows = []
    empty_cols = []
    lines = [l for l in lines_of_file(file)]
    i = 1
    rows = [0] * len(lines[0])
    galaxies = {}
    for idx, line in enumerate(lines):
        if '#' not in line:
            empty_rows.append(idx)
        for row_idx, letter in enumerate(line):
            if letter == '#':
                rows[row_idx] += 1
        appended_cols = 0
        for col_idx, (counter, letter) in enumerate(zip(rows, line)):
            if letter == '#':
                galaxies[i] = (idx, col_idx + appended_cols)
                i += 1

    for idx, row in enumerate(rows):
        if row == 0:
            empty_cols.append(idx)

    min_lengths = []
    pairs = []
    for galaxy_from, coords_from in galaxies.items():
        lengths = []
        for galaxy_to, coords_to in galaxies.items():
            if galaxy_to != galaxy_from:
                coords_from_a = coords_from[0]
                coords_to_a = coords_to[0]
                factor_a = 0
                for r in empty_rows:
                    coords = sorted([coords_from_a, coords_to_a])
                    if r in range(coords[0], coords[1]):
                        factor_a += factor

                coords_from_b = coords_from[1]
                coords_to_b = coords_to[1]
                factor_b = 0
                for r in empty_cols:
                    coords = sorted([coords_from_b, coords_to_b])
                    if r in range(coords[0], coords[1]):
                        factor_b += factor
                length_a = abs(coords_from[0] - coords_to[0]) + factor_a
                length_b = abs(coords_from[1] - coords_to[1]) + factor_b
                length = length_a + length_b
                lengths.append(length)

                pair = '-'.join(sorted([str(galaxy_from), str(galaxy_to)]))
                if pair not in pairs:
                    min_lengths.append(length)
                    pairs.append(pair)
    return sum(min_lengths)

if __name__ == '__main__':
    res = run('day_11_input_ex.txt', 1)
    print(f"Beispiel 1: {res}")
    res = run('day_11_input.txt', 1)
    print(f"Ergebnis 1: {res}")
    res = run('day_11_input_ex.txt', 10-1)
    print(f"Beispiel 2a: {res}")
    res = run('day_11_input_ex.txt', 100-1)
    print(f"Beispiel 2b: {res}")
    res = run('day_11_input_ex.txt', 1_000_000-1)
    print(f"Beispiel 2: {res}")
    res = run('day_11_input.txt', 1_000_000-1)
    print(f"Ergebnis 2: {res}")

