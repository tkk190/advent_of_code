from utils import lines_of_file

def run(file):
    res_a, res_b = 0, 0
    for line in lines_of_file(file):
        numbers = [int(number) for number in line.split(' ')]
        i = 1
        while not all(num == 0 for num in numbers):
            res_a += numbers[-1]
            res_b += numbers[0] * (1 if i % 2 != 0 else -1)
            numbers = [numbers[idx] - numbers[idx - 1] for idx, n in enumerate(numbers) if idx > 0]
            i += 1
    return res_a, res_b

if __name__ == '__main__':
    res_1, res_2 = run('day_9_input_ex.txt')
    print(f"Beispiel 1: {res_1}")
    print(f"Beispiel 2: {res_2}")
    res_1, res_2 = run('day_9_input.txt')
    print(f"Ergebnis 1: {res_1}")
    print(f"Ergebnis 2: {res_2}")