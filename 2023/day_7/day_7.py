from utils import lines_of_file
from itertools import groupby

cards = {'A': '13', 'K': '12', 'Q': '11', 'J': '10', 'T': '09', '9': '08', '8': '07', '7': '06', '6': '05', '5': '04', '4': '03', '3': '02', '2': '01'}
cards_b = {'A': '13', 'K': '12', 'Q': '11', 'T': '10', '9': '09', '8': '08', '7': '07', '6': '06', '5': '05', '4': '04', '3': '03', '2': '02', 'J': '01'}

def part_one(file):
    values = {}
    for line in lines_of_file(file):
        hand, value = line.split(' ')
        grouped_hand = sorted([len(list(g)) for k, g in groupby(sorted(hand))], reverse=True)
        if grouped_hand[0] == 5:
            rating = '7'
        elif grouped_hand[0] == 4:
            rating = '6'
        elif grouped_hand[0] == 3 and grouped_hand[1] == 2:
            rating = '5'
        elif grouped_hand[0] == 3:
            rating = '4'
        elif grouped_hand[0] == 2 and grouped_hand[1] == 2:
            rating = '3'
        elif grouped_hand[0] == 2:
            rating = '2'
        elif grouped_hand[0] == 1:
            rating = '1'
        else:
            raise Exception('keine Zuordnung gefunden')
        values[rating + ''.join([cards[letter] for letter in hand])] = int(value)

    values = dict(sorted(values.items()))
    return sum([(idx + 1) * v for idx, v in enumerate(values.values())])
def part_two(file):
    categories = {
        'five_of_a_kind': [],
        'four_of_a_kind': [],
        'full_house': [],
        'three_of_a_kind': [],
        'two_pair': [],
        'one_pair': [],
        'high_card': [],
    }
    cat = {
        '7': 'five_of_a_kind',
        '6': 'four_of_a_kind',
        '5': 'full_house',
        '4': 'three_of_a_kind',
        '3': 'two_pair',
        '2': 'one_pair',
        '1': 'high_card',
    }
    for line in lines_of_file(file):
        hand, value = line.split(' ')
        value = int(value)
        global_rating = '0'
        for key, card in cards_b.items():
            new_hand = hand.replace('J', key)
            grouped_hand = sorted([len(list(g)) for k, g in groupby(sorted(new_hand))], reverse=True)
            if grouped_hand[0] == 5:
                rating = '7'
            elif grouped_hand[0] == 4:
                rating = '6'
            elif grouped_hand[0] == 3 and grouped_hand[1] == 2:
                rating = '5'
            elif grouped_hand[0] == 3:
                rating = '4'
            elif grouped_hand[0] == 2 and grouped_hand[1] == 2:
                rating = '3'
            elif grouped_hand[0] == 2:
                rating = '2'
            elif grouped_hand[0] == 1:
                rating = '1'
            else:
                raise Exception('keine Zuordnung gefunden')
            if rating > global_rating:
                global_rating = rating
        categories[cat[global_rating]].append((hand, value))
    # kategorien nach wert sortieren
    values = []
    for category_name, category in categories.items():
        new_category = {}
        for line in category:
            hand, value = line
            key = ''.join([cards_b[letter] for letter in hand])
            new_category[key] = value
        sorted_new_category = dict(sorted(new_category.items(), reverse=True))
        values += [c for c in sorted_new_category.values()]
    values.reverse()
    return sum([(idx + 1) * v for idx, v in enumerate(values)])

if __name__ == '__main__':
    res = part_one('day_7_input_ex.txt')
    print(f"Beispiel 1: {res}")
    res = part_one('day_7_input.txt')
    print(f"Ergebnis 1: {res}")
    res = part_two('day_7_input_ex.txt')
    print(f"Beispiel 2: {res}")
    res = part_two('day_7_input.txt') # 229270775 too low - 243305080 too high
    print(f"Ergebnis 2: {res}")
