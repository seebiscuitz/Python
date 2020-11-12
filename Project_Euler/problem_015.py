# Problem: 15
#
# Starting in the top left corner of a 2*2 grid, and only being able to 
# move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20*20 grid?
#

import time, math
s=time.time()
sum=0
gridsize = 20

def binom( n, k ):
	if k==0:
		return 1
	else:	
		if n==k:
			nfact,nnfact=1,1
			for i in xrange(1,n):
				nfact*=i
			for i in xrange(1,2*n):
				nnfact*=i
			result = nfact/(nnfact*nnfact)
		else:
			nfact,kfact,nkfact=1,1,1
			for i in xrange(1,n):
				nfact*=i
			for i in xrange(1,k):
				kfact*=i
			for i in xrange(1,n-k):
				nkfact*=i
			result = nfact/(kfact*nkfact)
	return result


print binom(2*gridsize,gridsize)
print time.time()-s