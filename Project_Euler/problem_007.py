# -*- coding: utf-8 -*-
#     - projecteuler.net -
#
# Problem 7:
#	10001st Prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

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

def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]
	
print primes(10001)