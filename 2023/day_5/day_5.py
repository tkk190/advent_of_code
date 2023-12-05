import re
from utils import lines_of_file

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def run(file):
    content = {}
    current_map = ''
    for line in lines_of_file(file):
        dest_range_start, source_range_start, range_length = None, None, None
        if 'seeds' in line:
            seeds = re.findall('[0-9]+', line)
        if 'map' in line:
            current_map = line.replace(' map:', '').split('-')
        if re.search('^[0-9]+ [0-9]+ [0-9]+$', line):
            dest_range_start, source_range_start, range_length = re.findall('[0-9]+', line)
        if len(current_map) > 0:
            if current_map[0] in content:
                if dest_range_start is not None:
                    content[current_map[0]]['ranges'].append(
                        {
                            'dest_range_start': int(dest_range_start),
                            'dest_range': range(int(dest_range_start), int(dest_range_start) + int(range_length)),
                            'source_range_start': int(source_range_start),
                            'source_range': range(int(source_range_start), int(source_range_start) + int(range_length)),
                            'range_length': int(range_length)
                        }
                    )
            else:
                content[current_map[0]] = {
                    'destination': current_map[2],
                    'ranges': []
                }
    location_numbers_a = []
    location_numbers_b = []

    for seed in seeds:
        seed = int(seed)
        location_numbers_a.append(recursive_solution(content, 'seed', seed))

    for seed_chunk in chunks(seeds, 2):
        seed_range = range(int(seed_chunk[0]), int(seed_chunk[0]) + int(seed_chunk[1]))
        for idx, seed in enumerate(seed_range):
            location_numbers_b.append(recursive_solution(content, 'seed', seed))
    return min(location_numbers_a), min(location_numbers_b)


def recursive_solution(content, key, value):
    if key == 'location':
        return value
    else:
        new_value = None
        ranges = content[key]['ranges']
        for range in ranges:
            if value in range['source_range']:
                new_value = value + range['dest_range_start'] - range['source_range_start']
                break
        if new_value is None:
            new_value = value
        return recursive_solution(content, content[key]['destination'], new_value)

if __name__ == '__main__':
    res_1, res_2 = run('day_5_input_ex.txt')
    print(f"Beispiel 1: {res_1}")
    print(f"Beispiel 2: {res_2}")
    res_1, res_2 = run('day_5_input.txt')
    print(f"Ergebnis 1: {res_1}")
    print(f"Ergebnis 2: {res_2}")