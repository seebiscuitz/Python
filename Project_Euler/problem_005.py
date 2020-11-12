import sys
import math
from functools import reduce
from fractions import gcd


def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

print reduce(lcm, range(1,20+1))