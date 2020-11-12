# -*- coding: utf-8 -*-
#     - projecteuler.net -
#
# Problem 6:
#	Sum Square Difference
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

# Created on: 	17/09/2017
# Last Updated:	17/09/2017

#imports
import sys
import math

#splash
print	""
print	"				-dx4-			"
print	""
#\splash 

#program begins
a = 1;
sum = 0;
ssum = 0;

while a <= 100:
	sum = sum + a;
	ssum = (a*a) + ssum;
	a = a + 1;
print "The answer is ", abs(ssum - (sum*sum))	

#program ends