# Project Euler
# Problem 76 : Counting Summations
#
# How many different ways can one hundred be written as a sum of at least two positive integers?
#
# eg    5:
#       4+1
#       3+2
#       3+1+1
#       2+2+1
#       2+1+1+1
#       1+1+1+1+1
#
import numpy as np
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
    total = 100
    # compute answer 
    
    # output to screen
    project_euler.__output(time() - _time, problem, result)
    return 

if __name__ == "__main__":
    main()