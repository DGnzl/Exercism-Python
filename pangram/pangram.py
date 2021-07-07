def is_pangram(sentence):
    return len({x.lower() for x in sentence if x.isalpha()}) == 26