# Project Euler
# Problem 69 : Totient Maximum
#
import numpy as np
import os
from time import time
#


def __seive(n): 
    _out = []
    prime = [True for i in xrange(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in xrange(n + 1): 
        if prime[p]: 
            _out.append(p)
    return _out
    
def __augphi(n):
    def __gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    x = 0
    for i in xrange(n):
        if __gcd(i,n) == 1:
            x += 1
    return x

def __output(_s, _prob, _ans):
    print '#########################'
    print 'Problem Number: ', _prob
    print 'Time Taken: ', time() - _s
    print 'Answer: ', _ans
    print '#########################'

def main():
    # generics
    s = time()
    result = 1
    problem = 69
    # problem specific variables
    n = 10**6
    max = 1
    i = 0
    primes = __seive(n)
    # compute answer 
    while(result * primes[i] < n):
        result *= primes[i]
        i += 1
    # output to screen
    __output(s, problem, result)
    return 

if __name__ == "__main__":
    main()