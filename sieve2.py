import numpy as np
import math


def sieve(n):
    T = np.ones(n//2, dtype=np.bool)
    for i in range(1, math.ceil(math.sqrt(n)-1)//2):
        if T[i]:
            T[2*i**2+2*i::2*i+1] = False
    T = (np.nonzero(T)[0] * 2 + 1).astype(np.uint64)
    T[0] = 2
    return T


if __name__ == "__main__":
    import cProfile
    n = eval(input("n = "))
    cProfile.run("sieve(n)")
    # print(sieve(n))
