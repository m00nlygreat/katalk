import re
import csv
import matplotlib.pyplot as plt

file = './combined.txt'

txt = open(file, 'r', encoding='utf-8-sig')
w = open('e.csv','w', newline='' ,encoding='utf-8-sig')
wr = csv.writer(w)

message_pattern = '^(\d{4}. \d{1,2}. \d{1,2}). (\d{2}:\d{2}), (.+?(?=\s:\s))\s:\s(.+)$'
exception_patterns_str = ['^\d+년 \d+월 \d+일 .요일','^저장한 날짜 : .+$','[\ufeff]?Talk_\d{4}.\d{1,2}.\d{1,2} \d{2}:\d{2}-\d+.txt','\d{4}[.] \d+[.] \d+[.] \d+:\d+: .+(나갔습니다.|들어왔습니다.|가렸습니다.|내보냈습니다.|남게됩니다.|공유했습니다.)$','운영정책을 위반한 메시지로 신고 접수 시 카카오톡 이용에 제한이 있을 수 있습니다.']
exception_patterns = list(map(re.compile, exception_patterns_str))

p = re.compile(message_pattern)

e = []
wr.writerow(['date','time','person','message'])

while(True):
    l = txt.readline()
    if l == '':
        wr.writerows(e)
        exit()
    m = p.match(l)
    if m:
        e.append([m.group(1),m.group(2),m.group(3),m.group(4)])
    else:
        if any(reg.match(l) for reg in exception_patterns):
            print(l)
            continue
        else:
            if len(e) != 0:
                z = e.pop()
                z[3] += l
                e.append(z)