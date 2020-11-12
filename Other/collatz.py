#collatz.py
#
# Rules:
# If even -> n / 2
# If odd  -> (3 * n) + 1
#
import math
import numpy
import matplotlib.pyplot as plt
import os
#
#
start = 10**6
iterations = 100
num_iter = 0
n = 0
collatz = [0 for i in range(iterations+1)]
#
for i in range(start,start+iterations):
    n = i
    while n != 1:
        if n < 0:
            print("Break at ",  i, " sequence hit ", n)
        if n%2 == 0:
            n = n / 2
            collatz[i - start] += 1
        else:
            n = (3 * n) + 1
            collatz[i - start] += 1
#
plt.plot(collatz, 'r+')
plt.show()
#print(collatz)
#