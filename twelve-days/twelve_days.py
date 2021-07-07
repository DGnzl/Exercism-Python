gifts = [
    "twelve Drummers Drumming,",
    "eleven Pipers Piping,",
    "ten Lords-a-Leaping,",
    "nine Ladies Dancing,",
    "eight Maids-a-Milking,",
    "seven Swans-a-Swimming,",
    "six Geese-a-Laying,",
    "five Gold Rings,",
    "four Calling Birds,",
    "three French Hens,",
    "two Turtle Doves,",
    "and a Partridge in a Pear Tree."
]

days = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]

def recite(start_verse, end_verse):
    ans = []
    for x in range(start_verse, end_verse + 1):
        song = [f'On the {days[x - 1]} day of Christmas my true love gave to me:']
        if x == 1:
            song.append(gifts[11][4:])
        else:
            song.extend(gifts[12 - x:])
        ans.append(' '.join(song))
    return ans