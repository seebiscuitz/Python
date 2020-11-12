# Project Euler
# Problem 75 : Singular Integer Right Triangles
#
# Given that L is the length of the wire, for how many values of 
# L <= 1,500,000 can exactly one integer sided right angle triangle
# be formed?
#
# eg    12: 3,4,5
#       24: 6,8,10
#       120: 30,40,50   20,48,52
#
import numpy as np
import os
import math
from time import time
import project_euler
#

def main():
    # generics
    _time = time()
    result = 0
    problem = 75
    # problem specific variables
    limit = 1500000
    mlimit = int(math.sqrt(limit / 2))
    tri = [0 for i in range(limit+1)]
    # compute answer 
    for m in range(2,mlimit):
        for n in range(1,m):
            if ((n + m) % 2) == 1 and project_euler.__gcd(n, m) == 1:
                a = (m * m) + (n * n)
                b = (m * m) - (n * n)
                c = 2 * m * n
                p = a + b + c
                while p < limit:
                    tri[p] += 1
                    if tri[p] == 1: result += 1
                    if tri[p] == 2: result -= 1
                    p += a + b + c   
    # output to screen
    project_euler.__output(time() - _time, problem, result)
    return 

if __name__ == "__main__":
    main()