import string

def count_words(sentence: str) -> dict:
    ans = {}
    # sentence = sentence.replace(',', ' ')
    # sentence = sentence.replace('_', ' ')
    # sentence = sentence.replace('\n', ' ')
    sentence.translate(None, string.punctuation)


    for x in sentence.lower().split():
        print(x)
        if ans.get(x):
            ans[x] += 1
        else:
            ans[x] = 1
    return ans

print(count_words("car: carpet as java: javascript!!&@$%^&"))