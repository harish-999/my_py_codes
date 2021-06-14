#finding numbers from 0 to 100 except which are divisible by 3,5
i = 0
while i<100:
    i = i + 1
    if i % 3 != 0:
        if i % 5 != 0:
            print('numbers from 0 to 100 expect 3,5 multiples are:',i)

#finding perfect square between numbers code:
 import math
 for i in range(1,11):
     if math.sqrt(i) % 1 == 0:
         print(i)















