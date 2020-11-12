# Problem: 14
#
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million
#

import time, math
s=time.time()

MaxChain=0
MaxChainStart=0
lim=1000000

for n in xrange(1,lim):
	flag=False
	startnum=n
	chainlen=0
	while not flag:
		chainlen+=1
		if startnum==1:
			flag=True
			if chainlen>MaxChain:
				MaxChain=chainlen
				MaxChainStart=n
		if startnum%2==0:
			startnum = startnum/2
		else:
			startnum = (3*startnum)+1
	
print 'Start number:',MaxChainStart
print 'Chain Length:',MaxChain
print time.time()-s