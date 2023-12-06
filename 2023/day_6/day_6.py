import re
from utils import lines_of_file

def part_one(file):
    res = 1
    lines = [l for l in lines_of_file(file)]
    times = re.findall('[0-9]+', lines[0])
    distances = re.findall('[0-9]+', lines[1])
    for time, distance_record in zip(times, distances):
        time = int(time)
        distance_record = int(distance_record)
        record_beats = 0
        for i in range(1, time + 1):
            acceleration_time = time - i
            distance = (time - acceleration_time) * acceleration_time
            if distance > distance_record:
                record_beats += 1
        res *= record_beats
    return res


def part_two(file):
    res = 0
    lines = [l for l in lines_of_file(file)]
    time = int(''.join(re.findall('[0-9]+', lines[0])))
    distance_record = int(''.join(re.findall('[0-9]+', lines[1])))
    for i in range(1, time + 1):
        acceleration_time = time - i
        distance = (time - acceleration_time) * acceleration_time
        if distance > distance_record:
            res += 1
    return res


if __name__ == '__main__':
    res = part_one('day_6_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_6_input.txt')
    print(f"Ergebnis 1: {res}")
    res = part_two('day_6_input_ex.txt')
    print(f"Beispiel 2: {res}")
    res = part_two('day_6_input.txt')
    print(f"Ergebnis 2: {res}")
