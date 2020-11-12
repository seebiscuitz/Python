#     - projecteuler.net -
#
# Problem 1:
#	Multiples of 3 and 5
#
# If we list all natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Created on: 	21/12/2016
# Last Updated:	26/12/2016

#imports
import sys
import math

#splash
print	""
print	"				-dx4-			"
print	""
#\splash 

#program begins
flag = 1;
i = 1;
total = 0;

#while begins
while flag:
	if (i%3==0) or (i%5==0):
		total = total + i;
	i=i+1;
	if i>=1000:
		flag = 0;

#while ends
print "The total sum is ", total
print 