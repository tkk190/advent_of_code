from day_4_input import input

# input = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# """


if __name__ == '__main__':
    counter = 0
    counter_b = 0
    for i in input.splitlines():
        elf_a, elf_b = i.split(',')
        min_a, max_a = elf_a.split('-')
        min_b, max_b = elf_b.split('-')
        min_a = int(min_a)
        min_b = int(min_b)
        max_a = int(max_a)
        max_b = int(max_b)

        if min_a <= min_b <= max_b <= max_a or min_b <= min_a <= max_a <= max_b:
            counter += 1
        if min_a <= min_b <= max_a or min_a <= max_b <= max_a or min_b <= max_a <= max_b or min_b <= min_a <= max_b:
            counter_b += 1

    print(f"Ergebnis 1: {counter}")
    print(f"Ergebnis 2: {counter_b}")
