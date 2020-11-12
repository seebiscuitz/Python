#     - projecteuler.net -
#
# Problem 9:
#	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#	
#	a2 + b2 = c2
#	For example, 32 + 42 = 9 + 16 = 25 = 52.
#	
#	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#	Find the product abc.
#
# Created on:	29/05/2018 	
# Last Updated:	02/06/2018

#imports
import sys
import math

#splash
print	""
print	"				-dx4-			"
print	""
#\splash 

#program begins

#vars
for num in range(1,1000):
	for dig in range(num, 1000 - num):
		i = 1000 - num - dig
		if num * num + dig * dig == i * i:
			print(num, dig, i)
			print("Product: {}".format(num * dig * i))
		
#/vars

#funs

#/funs


#program ends