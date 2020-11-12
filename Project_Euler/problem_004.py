#     - projecteuler.net -
#
# Problem 4:
#	Largest Palindrome Product
#
# A plaindrome number reads the same both ways. The largest 
# palindrome made from the product of twp 2-digit numbers is
# 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two
# three digit numbers.
#

# Created on: 	28/12/2016
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
def reverse(n):
	reversed = 0
	while n > 0:
		reversed = 10*reversed + (n % 10);
		n = n/10;
	return reversed
def isPalindrome(n):
	return n == reverse(n)


largestPalindrome = 0;
a = 999;
while a >= 100:
	if a % 11 == 0:
		b = 999
		db = 1
	else:
		b = 990 #The largest number less than or equal 999 and divisible by 11
		db = 11
	while b >= a:
		if a*b <= largestPalindrome:
			break
		if isPalindrome(a*b):
			print "LP := ", largestPalindrome
			largestPalindrome = a*b
		b = b-db
	a = a-1
print "Largest palindrome is ", largestPalindrome, " from factors ", a, " and ", b
