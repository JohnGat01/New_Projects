import time
#from pprint import pprint
from random import randint

start_time = time.time()
file = 'bulgakov_master-i-margarita.txt'


stat = {}
sequence = ' '

with open(file, 'r', encoding='utf8') as file:
    for line in file:
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = char
            # sequence = sequence[:1] + char

totals = {}
stat_for_generate = {}

for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

char_to_generate = 1000
printed = 0

while printed < char_to_generate:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    printed += 1
    sequence = char


print("--- %s seconds ---" % (time.time() - start_time))


