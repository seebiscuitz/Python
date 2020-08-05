# Project Euler
# Problem 70 : Totient Permutation
#
# Find the value of n < 10 ** 7 for which phi(n) is a perm of n and
# the ratio n / phi(n) produces a minimum.
#
import numpy as np
import os
import math
from time import time
import project_euler
#

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

def main():
    # generics
    s = time()
    result = 1
    problem = 70
    # problem specific variables
    _lower = 2000
    _upper = 5000
    _limit = 10 ** 7
    _primes = project_euler.__eseive(_lower, _upper)
    _n = 0
    _bn = 1
    _phi = 1
    _bphi = 0
    _ratio = 0
    _bratio = float("inf")
    # compute answer 
    for i in xrange(len(_primes)):
        for j in xrange(i + 1, len(_primes)):
            _n = long(_primes[i] * _primes[j])
            if _n > _limit:
                break
            _phi = long((_primes[i] - 1) * (_primes[j] - 1))
            _ratio = float(_n) / _phi
            if project_euler.__isperm(_n, _phi) and _bratio > _ratio:
                _bn = _n
                _bphi = _phi
                _bratio = _ratio
    # output to screen
    project_euler.__output(s, problem, _bn)
    print _bratio
    return 

if __name__ == "__main__":
    main()