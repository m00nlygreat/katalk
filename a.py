import re
a = ['a', 'b']
a = list(map(re.compile, a))

line = 'aaa'

b = any(reg.match(line) for reg in a)

print(b)