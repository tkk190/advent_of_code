from day_2_input import input

# A for Rock
# B for Paper
# C for Scissors

# X for Rock
# Y for Paper
# Z for Scissors
# C < A < B < C
# 3 < 1 < 2 < 3

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}
# input = """A Y
# B X
# C Z
# """

#X means you need to lose,
# Y means you need to end the round in a.py draw, and
# Z means you need to win

def get_loser_hand(number):
    res = number - 1
    if res > 0:
        return res
    else:
        return 3

def get_winner_hand(number):
    res = number + 1
    if res <= 3:
        return res
    else:
        return 1


if __name__ == '__main__':
    result = 0
    for i in input.splitlines():
        a = i.split(' ')
        opp = points[a[0]]
        me = points[a[1]]
        res = me - opp
        if res == 0:
            factor = 3
        elif abs(res) == 1:
            factor = 6 if res > 0 else 0
        elif abs(res) == 2:
            factor = 0 if res > 0 else 6
        result += factor + me
    print(f"Ergebnis 1: {result}")
    result = 0
    for i in input.splitlines():
        a = i.split(' ')
        opp = points[a[0]]
        win_loss = a[1]
        if win_loss == 'X':
            factor = 0
            me = get_loser_hand(opp)
        elif win_loss == 'Y':
            factor = 3
            me = opp
        elif win_loss == 'Z':
            factor = 6
            me = get_winner_hand(opp)
        result += factor + me
    print(f"Ergebnis 2: {result}")

