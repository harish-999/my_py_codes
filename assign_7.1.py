# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
# Use the file coursera_assign.txt to produce the output below.
fname = input('enter the file name: ')
try:
    fh = open(fname)
except:
    print('invalid file name:',fname)
    quit()
for i in fh:
    i = i.rstrip()
    i = i.upper()
    print(i)
