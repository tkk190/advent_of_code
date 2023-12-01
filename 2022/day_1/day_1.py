from day_1_input import input

if __name__ == '__main__':
    res = []
    temp_res = 0
    for i in input.splitlines():
        if i != '':
            temp_res += int(i)
        else:
            res.append(temp_res)
            temp_res = 0
    res.sort(reverse=True)
    print(f"Ergebnis 1: {res[0]}")
    print(f"Ergebnis 2: {sum(res[:3])}")