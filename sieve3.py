import numpy as np
import math


D = (1, 7, 11, 13, 17, 19, 23, 29)

# inverse_function of D
# i_D = {1:0, 7:1, 11:2, 13:3, 17:4, 19:5, 23:6, 29:7}

# Dp_q = tuple(tuple(i*j//30 for i in D) for j in D)
Dp_q = (
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 2, 3, 3, 4, 5, 6),
    (0, 2, 4, 4, 6, 6, 8, 10),
    (0, 3, 4, 5, 7, 8, 9, 12),
    (0, 3, 6, 7, 9, 10, 13, 16),
    (0, 4, 6, 8, 10, 12, 14, 18),
    (0, 5, 8, 9, 13, 14, 17, 22),
    (0, 6, 10, 12, 16, 18, 22, 28)
)

# Dp_r = tuple(tuple(i*j%30 for i in D) for j in D)
"""
Dp_r = (
    (1, 7, 11, 13, 17, 19, 23, 29),
    (7, 19, 17, 1, 29, 13, 11, 23),
    (11, 17, 1, 23, 7, 29, 13, 19),
    (13, 1, 23, 19, 11, 7, 29, 17),
    (17, 29, 7, 11, 19, 23, 1, 13),
    (19, 13, 29, 7, 23, 1, 17, 11),
    (23, 11, 13, 29, 1, 17, 19, 7),
    (29, 23, 19, 17, 13, 11, 7, 1)
)
"""

# i_Dp_r = tuple(tuple(i_D[i*j%30] for i in D) for j in D)
"""
i_Dp_r = (
    (0, 1, 2, 3, 4, 5, 6, 7),
    (1, 5, 4, 0, 7, 3, 2, 6),
    (2, 4, 0, 6, 1, 7, 3, 5),
    (3, 0, 6, 5, 2, 1, 7, 4),
    (4, 7, 1, 2, 5, 6, 0, 3),
    (5, 3, 7, 1, 6, 0, 4, 2),
    (6, 2, 3, 7, 0, 4, 5, 1),
    (7, 6, 5, 4, 3, 2, 1, 0)
)
"""

# bitmasks = 0xff - (1 << i_Dp_r)
bitmasks = (
    (0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f),
    (0xfd, 0xdf, 0xef, 0xfe, 0x7f, 0xf7, 0xfb, 0xbf),
    (0xfb, 0xef, 0xfe, 0xbf, 0xfd, 0x7f, 0xf7, 0xdf),
    (0xf7, 0xfe, 0xbf, 0xdf, 0xfb, 0xfd, 0x7f, 0xef),
    (0xef, 0x7f, 0xfd, 0xfb, 0xdf, 0xbf, 0xfe, 0xf7),
    (0xdf, 0xf7, 0x7f, 0xfd, 0xbf, 0xfe, 0xef, 0xfb),
    (0xbf, 0xfb, 0xf7, 0x7f, 0xfe, 0xef, 0xdf, 0xfd),
    (0x7f, 0xbf, 0xdf, 0xef, 0xf7, 0xfb, 0xfd, 0xfe)
)

# K = np.array([[D[i] if (k >> i) & 1 else 0 for i in range(8)] for k in range(256)], dtype=np.uint64)


def sieve(n):
    if n < 2:
        return np.array([])
    elif n < 3:
        return np.array([2])
    elif n < 5:
        return np.array([2, 3])
    elif n < 7:
        return np.array([2, 3, 5])

    lenT = (n-1)//30+1
    T = np.full(lenT, 0xff, dtype=np.uint8)
    T[0] -= 1
    T[-1] = 0

    tmp = (n-1) % 30 + 1
    for i, p in enumerate(D):
        if p < tmp:
            T[-1] += (1 << i)
        else:
            break

    for m1, byte in enumerate(T[:math.ceil((math.sqrt(1+30*n)-1)/30)]):
        for index_i1 in range(8):
            if (byte >> index_i1) % 2:
                t = 30*m1 + D[index_i1]
                Dp_q_i1 = Dp_q[index_i1]
                bitmasks_i1 = bitmasks[index_i1]
                for index_i2, i2 in enumerate(D[index_i1:]):
                    index_i2 += index_i1
                    T[m1 * t + m1*i2 + Dp_q_i1[index_i2]::t] &= bitmasks_i1[index_i2]
                for index_i2, i2 in enumerate(D[:index_i1]):
                    T[(m1 + 1)*t + m1*i2 + Dp_q_i1[index_i2]::t] &= bitmasks_i1[index_i2]

    T = np.unpackbits(T, bitorder="little")
    P = (np.tile(D, lenT) + np.repeat(np.arange(0, n, 30), 8))[T == 1]
    P = np.concatenate([[2, 3, 5], P])
    return P


if __name__ == "__main__":
    import cProfile
    n = eval(input("n = "))
    cProfile.run("sieve(n)")
    # print(sieve(n))
