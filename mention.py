import csv
import re
from operator import itemgetter, attrgetter

c = open('conversation.csv','r', encoding='utf-8-sig')
rc = csv.reader(c)
wc = csv.writer(open('result.csv', 'w', encoding='utf-8-sig', newline=''))

words = ['다다']

patterns = list(map(re.compile, words))
speakers = []

while True:
    try:
        line = next(rc)
        if any(reg.search(line[3]) for reg in patterns):
            speakers.append(line[2])
    except:
        break

people = set(speakers)

counts = []

for person in people:
    counts.append([speakers.count(person), person])

wc.writerows(sorted(counts, key=itemgetter(0), reverse=True))