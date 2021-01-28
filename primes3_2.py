from binarysearch import upper_bound, binary_takewhile
from sieve import sieve
import numpy as np


def primes3_2(pf, n):
    if pf <= 0:
        raise ValueError
    elif n <= 2**pf:
        return []

    P = sieve(-(-n >> (pf-1)))  # nを2**(pf-1)で割って小数点以下切り上げ

    if pf == 1:
        return P

    PF = []
    appendPF = PF.append

    func1 = lambda x: (P[x]**2 < -(-n >> (pf-2)))
    func2 = lambda x: (P[x]*p < -(-n >> (pf-2)))
    high = len(P)
    for j, p in enumerate(binary_takewhile(P, func1)):
        high = upper_bound(j, high, func2)
        appendPF(P[j:high] * p)

    func1 = lambda x: (PF[x][0]*P[x] < sup)
    func2 = lambda x: (PF[j][x]*p < sup)
    func3 = lambda x: (PF[x][0]*p < sup)
    func4 = lambda x: (S[x]*p < sup)
    high1 = len(P)
    for i in range(3, pf+1):
        sup = -(-n >> (pf-i))
        high1 = upper_bound(0, high1, func1)
        high3 = len(PF)
        for j, p in enumerate(P[:high1]):
            PF[j] = [binary_takewhile(PF[j], func2) * p]
            high3 = upper_bound(j+1, high3, func3)
            for S in PF[j+1:high3]:
                PF[j].append(binary_takewhile(S, func4) * p)
            PF[j] = np.concatenate(PF[j])
            PF[j].sort()
        PF = PF[:high1].copy()
    del P

    PF = np.concatenate(PF)
    PF.sort()

    return PF


if __name__ == "__main__":
    import cProfile
    pf = eval(input("pf = "))
    n = eval(input("n = "))
    cProfile.run("primes3_2(pf, n)")
