# Problem: 21
#
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called 
#amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
#therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
#

import time, math
s=time.time()

maxnum=10000
amicable_nums=set()

def sum_div(n):
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

for i in range(1, 10000):
    sdi = sum_div(i)
    for j in range(i+1, 10000):
        if sdi == j and sum_div(j) == i:
            amicable_nums.update([i, j])

print sum(amicable_nums)
print time.time()-s