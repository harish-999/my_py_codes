# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.


inp = input('enter the file name: ')
fh = open(inp)
lst = list()
for i in fh:
    i = i.rstrip()
    i = i.split()
    print(i)
    lst.append(i)
print(lst)
print(len(lst))
p1 = lst[0]
print(p1)
p2 = lst[1]
print(p2)
a = p1 + p2
print(a)
p3 = lst[2]
print(p3)
p4 = lst[3]
print(p4)
b = p3 + p4
print(b)
c = a + b
c.sort()
l1 =c[0:7]
l2 =c[9:15]
l3 =c[17:24]
l4 =c[27:]
l = l1 + l2 + l3 + l4
print(l)
