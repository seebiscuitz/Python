import math
import player
import gameinfo
import truncgcf
import margin


def trueskillcalc(game, selfRating, oppRating, result):
    
    drawMargin = margin.getmarginfromprob(game.dp, game.beta)
    
    c = math.sqrt( math.pow(selfRating.stdv, 2) + math.pow(oppRating.stdv, 2) + (2*math.pow(game.beta, 2)) )
        
    [winMean, loseMean] = detmeans(result, selfRating, oppRating)
 
    meanDelta = winMean - loseMean

    if result!=0:
        v = truncgcf.voutmarg(meanDelta, drawMargin, c)
        w = truncgcf.woutmarg(meanDelta, drawMargin, c)
        rankMu = result
    else:
        v = truncgcf.vinmarg(meanDelta, drawMargin, c)
        w = truncgcf.winmarg(meanDelta, drawMargin, c)
        rankMu = 1

    varwDyn = math.pow(selfRating.stdv, 2) + math.pow(game.dyn, 2)
    meanMu = varwDyn / c
    stdvMu = varwDyn / math.pow(c, 2)

    newMean = selfRating.mean + (rankMu * meanMu * v)
    newStdv = math.sqrt(varwDyn * (1 - w * stdvMu))

    return [newMean, newStdv]

def getmarginfromprom():
    return

def detmeans(result, selfRating, oppRating):
    if result=='win':
        winMean = selfRating.stdv
        loseMean = oppRating.stdv
    elif result=='draw':
        winMean = selfRating.stdv
        loseMean = oppRating.stdv
    else:
        loseMean = selfRating.stdv
        winMean = oppRating.stdv
    return [winMean, loseMean]
