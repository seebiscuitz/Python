import math
import gaussdist

def voutmarg(delta, margin, c=1):
    cdelta = delta / c
    cmargin = margin / c

    denom = gaussdist.cumto(cdelta - cmargin)

    if denom < 2.222758749e-162:
        return -1 * cdelta + cmargin
    else:
        return gaussdist.at(cdelta - cmargin) / denom

def woutmarg(delta, margin, c=1):
    cdelta = delta / c
    cmargin = margin / c

    denom = gaussdist.cumto(cdelta - cmargin)

    if denom < 2.222758749e-162:
        if cdelta < 0:
            return 1
        else:
            return 0
    else:
        vwin = voutmarg(cdelta, cmargin)
        return vwin * (vwin + cdelta + cmargin)

def vinmarg(delta, margin, c=1):
    cdelta = delta / c
    cmargin = margin / c

    cdeltaabs = abs(cdelta)
    denom = gaussdist.cumto(cmargin - cdeltaabs) - gaussdist.cumto(-cmargin - cdeltaabs)

    if denom < 2.222758749e-162:
        if cdelta < 0:
            return -cdelta - cmargin
        else:
            return -cdelta + cmargin
    else:
        numer = gaussdist.at(-cmargin - cdeltaabs) - gaussdist.at(cmargin - cdeltaabs)

        if cdelta < 0:
            return -numer / denom
        else:
            return numer / denom

def winmarg(delta, margin, c=1):
    cdelta = delta / c
    cmargin = margin / c
    cdeltaabs = abs(cdelta)

    denom = gaussdist.cumto(cmargin - cdeltaabs) - gaussdist.cumto(-cmargin - cdeltaabs)

    if denom < 2.222758749e-162:
        return 1
    else:
        
        vt = vinmarg(cdeltaabs, cmargin)
        
        return vt * vt + ((cmargin - cdeltaabs) * gaussdist.at(cmargin - cdeltaabs) - (-cmargin - cdeltaabs) * gaussdist.at(-cmargin - cdeltaabs)) / denom
