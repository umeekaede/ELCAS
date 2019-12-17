import re

f = open('lengthfile.dat', 'rt')
s=f.read()
print(s)

num = re.sub("\\D", "", s)
print(num)    # "2019"