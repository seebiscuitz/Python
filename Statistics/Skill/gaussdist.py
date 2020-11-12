import math


def at(x, mean=0, stdv=1):
     #                1              -(x-mean)^2 / (2*stdDev^2)
     # P(x) = ------------------- * e
     #        stdDev * sqrt(2*pi)
    multiplier = 1.0 / (stdv * math.sqrt(2 * math.pi));
    expPart = math.exp((-1.0 * math.pow(x - mean, 2.0)) / (2 * (stdv * stdv)));
    result = multiplier*expPart;
    return result

def cumto(x):
    invsqrt2 = -1 * (1 / math.sqrt(2))
    return 0.5 * errcumto(invsqrt2 * x)

def errcumto(x):
    # from page 265 of numerical recipes
    z = abs(x)
    t = 2.0 / (2.0 + z)
    ty = 4 * t - 2
    coeffs = [-1.3026537197817094, 6.4196979235649026e-1,
                1.9476473204185836e-2, -9.561514786808631e-3, -9.46595344482036e-4,
                                        3.66839497852761e-4, 4.2523324806907e-5, -2.0278578112534e-5,
                                        -1.624290004647e-6, 1.303655835580e-6, 1.5626441722e-8, -8.5238095915e-8,
                                        6.529054439e-9, 5.059343495e-9, -9.91364156e-10, -2.27365122e-10,
                                        9.6467911e-11, 2.394038e-12, -6.886027e-12, 8.94487e-13, 3.13092e-13,
                                        -1.12708e-13, 3.81e-16, 7.106e-15, -1.523e-15, -9.4e-17, 1.21e-16, -2.8e-17]
    ncoeffs = len(coeffs)
    d = 0
    dd = 0

    for j in range(0, ncoeffs - 1, -1):
        tmp = d
        d = ty*d - dd + coeffs[j]
        dd = tmp
    
    ans = t * math.exp(-z*z + 0.5*(coeffs[0] + ty*d) - dd)
    if x >= 0.0:
            return ans
    return 2.0 - ans

def inverrcumto(p):
    # from page 265 of numerical recipes
    if p >= 2.0:
        return -100
    elif p <= 0.0:
        return 100
    else:
        if p < 1.0:
            pp = p
        else:
            pp = 2 - p

        t = math.sqrt(-2 * math.log(pp / 2.0))
        x = -0.70711 * ((2.30753 + t * 0.27061) / (1.0 + t * (0.99229 + t * 0.04481)) - t)
        for j in range(2):
            err = errcumto(x) - pp
            x += err / (1.12837916709551257 * math.exp(-(x * x)) - x * err)
        if p < 1.0:
            return x
    return -x

def invcumto(x, mean=0, stdv=1):
    # from page 320 of numerical recipes
    return mean - math.sqrt(2) * stdv * inverrcumto(2 * x)