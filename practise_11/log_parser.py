import time
import re

start_time = time.time()

file_name = 'events.txt'

class Parser:

    def reader(self, filename):
        regexp = r'(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}):[\d.]+\]\sNOK'
        with open(filename, 'r', encoding='utf8') as file:
            log = file.read()
            time_list = re.findall(regexp, log)
        return time_list


    def counter(self, time_list):
        count = {i: time_list.count(i) for i in time_list}
        return count


    def write(self, count, out_file_txt):
        if out_file_txt is not None:
            file = open(out_file_txt, 'w', encoding='utf8')
        else:
            file = None
        for key, val in count.items():
            file.write(f'[{key}]: NOK - {val}\n')
        if file:
            file.close()

parser = Parser()

if __name__ == '__main__':
    read = parser.reader(filename=file_name)
    counter = parser.counter(read)
    parser.write(counter, out_file_txt='log_parser_1')
    # write(counter(reader(filename=file_name)), out_file_txt='log_parser_1')
    print(f'===============  {round((time.time() - start_time), 4)} seconds ===============')
