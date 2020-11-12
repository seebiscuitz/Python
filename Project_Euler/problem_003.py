#     - projecteuler.net -
#
# Problem 3:
#	Largest Prime Factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
# 

# Created on: 	26/12/2016
# Last Updated:	28/12/2016

#imports
import sys
import math

#splash
print	""
print	"				-dx4-			"
print	""
#\splash 

#program begins
num = 600851475143; #A
spf = 2; 			#B
lpf = 0; 			#C
flag = 1;

print "Brute forcing... this may take some time"
while flag:
	if spf==num:
		flag = 0;
	else:
		if (num%spf)>0:
			spf = spf + 1;
		else:
			if spf>lpf:
				lpf = spf;
			num = num/spf;
			spf = 2;
			
if num>spf:
	out = num;
else:
	out = spf;
print "The largest prime factor is ", out
print 