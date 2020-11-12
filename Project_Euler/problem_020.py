# Problem: 20
#
#n means n * (n - 1) * ... * 3 * 2 * 1
#
#For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!
#

import time
s=time.time()

n=100
total=1
for x in xrange(1,n+1):
	total*=x

total=str(total)
sum=0
for x in total:
	sum+=int(x)
	
print sum
print time.time()-s