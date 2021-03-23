from urllib.request import urlopen

u = urlopen("https://www.kaggle.com")
words = {}

for line in u:
    line = str(line, encoding='utf-8')
    line = line.strip(" \n")
    for word in line.split():
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1


pairs = words.items()

A = sorted(pairs, key=lambda x: x[1], reverse=True)

for p in A[:5]:
    print(p[0], p[1])
