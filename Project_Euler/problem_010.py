# Problem:	10
#	
#	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#	Find the sum of all the primes below two million.
#

import time, math
s = time.time()
def IsPrime( n ):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0
	
	i = 3
	while( i < int( math.sqrt(n) ) + 1 ):
		if( n % i == 0):
			return 0
		i += 1
	return 1
	

N,T,sum = 1,1,1

while T < 2000000:
	if IsPrime(T):
		N+=1
		sum=sum+T;
	T+=2
print sum
print time.time() - s