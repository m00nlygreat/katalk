import csv
from operator import itemgetter, attrgetter

c = open('conversation.csv','r', encoding='utf-8')

wc = csv.writer(open('result.csv', 'w', newline='', encoding='utf-8-sig'))

rc = list(enumerate(csv.reader(c)))

lines = []
result = []

who = '문형'

for line in rc:
    if line[1][2] == who:      
        lines.append(rc[line[0]-1][1][2])

respondent = set(lines)


for res in respondent:
    result.append([lines.count(res),res])

wc.writerows(sorted(result, key=itemgetter(0), reverse=True))