from binarysearch import upper_bound
from sieve import sieve
import numpy as np


def primes4_2(pf, n):
    if pf <= 0:
        raise ValueError
    elif n <= 2**pf:
        return []

    P = sieve(-(-n >> (pf-1)))

    if pf == 1:
        return P

    PH = [0] * (pf-1)
    PF = []
    appendPF = PF.append
    npprod = np.prod
    high = None
    func = lambda x: (Pprod*P[x] < n)
    while True:
        index = PH[-1]
        Pprod = npprod(P[PH])
        if Pprod * P[index] < n:
            high = upper_bound(index, high, func)
            appendPF(P[index:high] * Pprod)
            PH[-1] += 1
        else:
            for i in range(-2, -pf, -1):
                if PH[i] != index:
                    PH[i:] = [PH[i] + 1] * (-i)
                    high = None
                    break
            else:
                break
    del P

    PF = np.concatenate(PF)
    PF.sort()

    return PF


if __name__ == "__main__":
    import cProfile
    pf = eval(input("pf = "))
    n = eval(input("n = "))
    cProfile.run("primes4_2(pf, n)")
