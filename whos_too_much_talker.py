import csv
from operator import itemgetter, attrgetter

c = open('e.csv','r')
rc = list(enumerate(csv.reader(c)))
lines = []
result = []

wc = csv.writer(open('rate.csv', 'w'))

speakers = []

for line in rc:
    speakers.append(line[1][2])

people = set(speakers)

counts = []

for person in people:
    counts.append([speakers.count(person), person])
    


wc.writerows(sorted(counts, key=itemgetter(0), reverse=True))