from binarysearch import binary_takewhile


def primes1_2(pf, n):
    if pf <= 0:
        raise ValueError
    if n <= 2**pf:
        return []

    PF = [[1]]
    tmp = 2
    while tmp < n:
        PF.append([])
        tmp *= 2
    PF[1] = [2, 3, 5]
    PF[2] = [4]

    func = lambda x: (PF[j][x] <= i//2)
    for i in range(6, n):
        primecount = 0
        divi = i
        for p in [2, 3, 5]:
            while divi % p == 0:
                primecount += 1
                divi //= p
        if primecount:
            for j in range(pf+1-primecount):
                if divi in binary_takewhile(PF[j], func):
                    PF[j+primecount].append(i)
                    break
        else:
            for j in range(1, pf+1):
                if all(i % k for k in binary_takewhile(PF[j], func)):
                    PF[j].append(i)
                    break
    return PF[pf]


if __name__ == "__main__":
    import cProfile
    pf = eval(input("pf = "))
    n = eval(input("n = "))
    cProfile.run("primes1_2(pf, n)")
