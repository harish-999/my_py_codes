 # Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 # The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
 # The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
 # After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


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
        i = i[1]
        lst.append(i)
print(lst)
for c in lst:
    count[c] = count.get(c,0) + 1
print(count)
bigword = None
bigcount = None
for k,v in count.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
        print(bigword,bigcount)
#from line 23 we can write code as follows
#largest = -1
#bigword = None
#for k,v in count.items():
    #if v > largest:
        #largest = v
        #bigword = k
#print(bigword,largest)
