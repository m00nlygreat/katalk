import os
import re

file_path = './src'
file_list = list(sorted(os.listdir(file_path)))
if '.DS_Store' in file_list:
    file_list.remove('.DS_Store')


result = open('combined.txt', 'w', newline='', encoding='utf-8-sig')

for file in file_list:
    txt = open(file_path+'/'+file, 'r', encoding='utf-8-sig')
    
    for line in txt:
        try:
            result.write(line)
        except:
            print(line)