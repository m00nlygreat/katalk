import csv
from operator import itemgetter, attrgetter

c = open('conversation.csv','r', encoding='utf-8-sig')
rc = list(enumerate(csv.reader(c)))
wc = csv.writer(open('rank.csv', 'w', encoding='utf-8-sig', newline=''))
lines = []
result = []


speakers = []

for line in rc:
    speakers.append(line[1][2])

people = set(speakers)

counts = []

for person in people:
    counts.append([speakers.count(person), person])
    


wc.writerows(sorted(counts, key=itemgetter(0), reverse=True))