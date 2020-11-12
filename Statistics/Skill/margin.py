import math
import numpy
import gaussdist

def getmarginfromprob(drawProb, beta):

    # draw probability = 2 * CDF(margin/(sqrt(n1+n2)*beta)) -1
    #
    # implies
    #
    # margin = inversecdf((draw probability + 1)/2) * sqrt(n1+n2) * beta
    # n1 and n2 are the number of players on each team
    margin = gaussdist.invcumto( 0.5 * (drawProb + 1), 0, 1) * math.sqrt(2) * beta

    return margin