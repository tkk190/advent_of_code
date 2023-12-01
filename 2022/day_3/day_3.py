from day_3_input import input

# input = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """

def get_priority(char):
    return ord(char)-64+26 if char.isupper() else ord(char)-64-32

if __name__ == '__main__':
    sum = 0
    for i in input.splitlines():
        splitter = int(len(i)/2)
        sum += get_priority(list(set(i[:splitter]) & set(i[splitter:]))[0])
    print(f"Ergebnis 1: {sum}")
    sum = 0
    lines = {}
    for idx, i in enumerate(input.splitlines()):
        key = int(idx/3)
        if key in lines:
            lines[key] = list(set(i) & set(lines[key]))
        else:
            lines[key] = list(i)
    for i in lines.values():
        sum += get_priority(i[0])
    print(f"Ergebnis 2: {sum}")
