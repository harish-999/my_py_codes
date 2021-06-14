smallest = None
print('before:',smallest)
for i in (1,23,4,567,0,345,67,56):
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    print(smallest, i)
print('smallest:',smallest)
