def all_variants(text):
    lenght = len(text)
    for i in range(lenght):
        yield text[i]
    for i in range(lenght - 1):
        yield text[i:i + 2]
    if lenght >= 3:
        yield text


a = all_variants("abc")
for i in a:
    print(i)
