import re
inp = input('enter the file name : ')
fh = open(inp)
lst = list()
for i in fh:
    i = i.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',i)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    lst.append(num)
print('maximum:',max(lst))
