def recite(start_verse, end_verse):
    days_and_gifts = {
        1: {'day_number': 'first', 'gift': 'a Partridge in a Pear Tree'},
        2: {'day_number': 'second', 'gift': 'two Turtle Doves'},
        3: {'day_number': 'third', 'gift': 'three French Hens'},
        4: {'day_number': 'fourth', 'gift': 'four Calling Birds'},
        5: {'day_number': 'fifth', 'gift': 'five Gold Rings'},
        6: {'day_number': 'sixth', 'gift': 'six Geese-a-Laying'},
        7: {'day_number': 'seventh', 'gift': 'seven Swans-a-Swimming'},
        8: {'day_number': 'eighth', 'gift': 'eight Maids-a-Milking'},
        9: {'day_number': 'ninth', 'gift': 'nine Ladies Dancing'},
        10: {'day_number': 'tenth', 'gift': 'ten Lords-a-Leaping'},
        11: {'day_number': 'eleventh', 'gift': 'eleven Pipers Piping'},
        12: {'day_number': 'twelfth', 'gift': 'twelve Drummers Drumming'},
    }

    def gather_gifts(current_day):
        gifts = []
        for previous_day in range(current_day, 0, -1):
            gifts.append(days_and_gifts.get(previous_day).get('gift'))
            if previous_day == 1 and len(gifts) > 1:
                gifts[-1] = f'and {gifts[-1]}'
        return ', '.join(gifts)

    verses = []
    for day_of_xmas in range(start_verse, end_verse + 1):
        verses.append(
            f'On the {days_and_gifts.get(day_of_xmas).get("day_number")} '
            f'day of Christmas my true love gave to me: '
            f'{gather_gifts(day_of_xmas)}.'
        )
    return verses
# x = [recite(n, n)[0] for n in range(1, 4)]
# print(x)
print(recite(1, 3))