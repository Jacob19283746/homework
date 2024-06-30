def all_variants(text):
    length = len(text)
    for i in range(length):
        for j in range(1, 3):
            if i + j <= length:
                yield text[i:i + j]
    if length >= 3:
        yield text

a = all_variants("abcde")
for i in a:
    print(i)
