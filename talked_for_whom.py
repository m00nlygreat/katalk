import csv
from operator import itemgetter, attrgetter

c = open('e.csv','r', encoding='utf-8-sig')
rank = csv.reader(open('rate.csv', 'r', encoding='utf-8-sig'))

wc = csv.writer(open('result.csv', 'w', newline='', encoding='utf-8-sig'))

rc = list(enumerate(csv.reader(c)))
lines = []
result = []

who = '한조외길#3406.34남'


for line in rc:
    if line[1][2] == who:      
        lines.append(rc[line[0]-1][1][2])

respondent = set(lines)


for res in respondent:
    result.append([lines.count(res),res])

wc.writerows(sorted(result, key=itemgetter(0), reverse=True))