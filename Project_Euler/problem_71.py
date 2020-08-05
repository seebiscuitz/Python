# Project Euler
# Problem 71 : Totient Permutation
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

def gcd(a, b):
    y = float(0)
    x = float(0)
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while x % y <> 0:
        temp = float(x)
        x = y
        y = temp % x
    return y


def main():
    # generics
    _time = time()
    result = 1
    problem = 70
    # problem specific variables
    _limit = 10 ** 7
    _lower = 2
    q = _limit
    s = 1
    r = 0
    a = 3
    b = 7
    # compute answer 
    while q >= _lower:
        p = (a * q - 1) / float(b)
        if (p * s > r * q):
            s = q
            r = p
            _lower = float(s) / (a * s - b * r)
        q += -1
    factor = gcd(r, s)
    r /= factor
    s /= factor
    # output to screen
    print r, s
    project_euler.__output(_time, problem, r)
    return 

if __name__ == "__main__":
    main()