# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.
largest = -1
smallest = None
while True:
    num = input('enter the number: ')
    if num == 'done':
        break
    try:
        nu = int(num)
    except:
        print('invalid input')
        continue
    if nu > largest:
        largest = nu
    if smallest is None:
        smallest = nu
    elif nu < smallest:
        smallest = nu
print('largest is:',largest)
print('smallest is:',smallest)
