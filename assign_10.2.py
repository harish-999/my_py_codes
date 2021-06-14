# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

inp = input('enter the file name: ')
fh = open(inp)
count = dict()
lst = list()
for i in fh:
    i = i.rstrip()
    if i.startswith('From:'):
        continue
    if i.startswith('From'):
        i = i.split()
        i = i[5]
        i = i.split(':')
        i = i[0]
        lst.append(i)
print(lst)
for c in lst:
    count[c] = count.get(c,0) + 1
print(count)
for k,v in sorted(count.items()):
    print(k,v)

#we can also use list comprehension
#syntax: [(expression) for loop ]
#s = sorted([(k,v) for k,v in count.items()])
#print(s)
