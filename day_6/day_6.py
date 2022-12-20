from day_6_input import input

# input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def run(length):
    res = -1
    for i in range(len(input)-length):
        if len(set(input[i:i+length])) == length:
            res = i + length
            break
    return res

if __name__ == '__main__':
    print(f"Ergebnis 1: {run(4)}")
    print(f"Ergebnis 2: {run(14)}")
