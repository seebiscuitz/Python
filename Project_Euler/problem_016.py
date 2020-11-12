# Problem: 16
#
#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?
#

import time, math
s=time.time()
sum=0
num=2**1000

digits=str(num)
for x in digits:
	sum+=int(x)

print sum
print time.time()-s