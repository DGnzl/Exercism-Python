def is_isogram(string):
    s = set()
    d = dict()
    x = [c.casefold() for c in string.upper() if c.isalpha]
    print(x)
    print(set(x))
    for c in string.upper():
        if c.isalpha():
            if d.get(c):
                return False
            else:
                d[c] = True
    return True

is_isogram('AAA')
is_isogram('lumberjack')