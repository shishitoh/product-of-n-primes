import numpy as np
import math


def sieve(n):
    T = np.ones(n, dtype="bool")
    T[0:2] = False
    T[4::2] = False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if T[i]:
            T[i*i::2*i] = False
    return np.nonzero(T)[0].astype(np.uint64)


if __name__ == "__main__":
    import cProfile
    n = eval(input("n = "))
    cProfile.run("sieve(n)")
