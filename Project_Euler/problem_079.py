# Project Euler
# Problem 79 : Passcode Derivation
#
# A common security method used for online banking is to ask the user for three random characters from
# a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th
# characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file so as to determine the
# shortest possible secret passcode of unknown length.
#
# Submitted answer: 73162890
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
    problem = 76
    # problem specific variables
    
    # compute answer 
    
    # output to screen
    project_euler.__output(time() - _time, problem, result)
    return 

if __name__ == "__main__":
    main()