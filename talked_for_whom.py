import csv
from operator import itemgetter, attrgetter

c = open('e.csv','r')
rank = csv.reader(open('rate.csv', 'r'))

rc = list(enumerate(csv.reader(c)))
lines = []
result = []

who = '한조외길#3406.34남'

wc = csv.writer(open('result.csv', 'w'))

for line in rc:
    if line[1][2] == who:      
        lines.append(rc[line[0]-1][1][2])

respondent = set(lines)


for res in respondent:
    result.append([lines.count(res),res])

wc.writerows(sorted(result, key=itemgetter(0), reverse=True))