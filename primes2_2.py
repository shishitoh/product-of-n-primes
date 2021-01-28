from binarysearch import binary_takewhile
from sieve import sieve
import numpy as np


def primes2_2(pf, n):
    if pf <= 0:
        raise ValueError
    elif n <= 2**pf:
        return []

    P = sieve(-(-n >> (pf-1)))

    if pf == 1:
        return P

    pwpf = 2**pf

    T = np.zeros(n-pwpf, dtype=np.uint8)

    for p in P:
        T[int((p - pwpf) % p)::p] += 1

    func = lambda x: (P[x] < sup)
    for i in range(2, pf+2):
        sup = pow(n, 1/i)
        P = binary_takewhile(P, func).astype(np.uint64)
        for p in P**np.uint64(i):
            T[int((p - pwpf) % p)::p] += 1
    del P

    return np.add(np.where(T == pf)[0].astype(np.uint64), np.uint64(pwpf))


if __name__ == "__main__":
    import cProfile
    pf = eval(input("pf = "))
    n = eval(input("n = "))
    cProfile.run("primes2_2(pf, n)")
