import time
from random import randint

start_time = time.time()
file = 'bulgakov_master-i-margarita.txt'


class Chatterer:
    analize_count = 12
    file = 'bulgakov_master-i-margarita.txt'

    def __init__(self):
        self.stat = {}

    def collect(self):
        sequence = ' ' * self.analize_count
        with open(self.file, 'r', encoding='utf8') as file:
            for line in file:
                line = line[:-1]
                for char in line:
                    if sequence in self.stat:
                        if char in self.stat[sequence]:
                            self.stat[sequence][char] += 1
                        else:
                            self.stat[sequence][char] = 1
                    else:
                        self.stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
            self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, N):
        printed = 0
        spaces_printed = 0
        sequence = ' ' * self.analize_count

        while printed < N:
            char_stats = self.stat_for_generate[sequence]
            total = self.totals[sequence]
            dice = randint(1, total)
            pos = 0
            for count, char in char_stats:
                pos += count
                if dice <= pos:
                    break
            print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char


chatterer = Chatterer()
chatterer.collect()
chatterer.prepare()
chatterer.chat(N=2000)

print('\n', '\n', ''"========== %s seconds ==========" % (time.time() - start_time))
