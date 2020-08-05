# Project Euler
# Problem 74 : Digit Fractorial Chains
#
# How many chains, with a starting number below one-million, contain 
# exactly sisty non-repeating terms?
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
    result = 1
    problem = 74
    # problem specific variables
    limit = 10**6
    chains_eq60 = 0
    target_chain_length = 60
    # compute answer
    for i in range(1, limit):
        chain_length = fact_loop(i)
        if chain_length == target_chain_length:
            chains_eq60 += 1
            #print(i, chains_eq60)
    # output to screen
    project_euler.__output(_time, problem, chains_eq60)
    return 

def fact_loop(n):
    nlist = list(map(int, str(n)))
    chain_length = 1
    chain = [n]
    res = 0
    looped = False
    while not looped:
        res = 0
        for i in nlist:
            res += math.factorial(i)
        if res in chain:
            looped = True
            #print(chain_length, chain)
        else:
            chain_length += 1
            chain.append(res)
        nlist = list(map(int, str(res)))
    return chain_length

if __name__ == "__main__":
    main()