from binarysearch import *
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
	sup = biS(P, (lambda x: (P[x] < pow(n, 1/pf))))
	while PH[0] < sup:
		index = PH[-1]
		Pprod = npprod(P[PH])
		if Pprod * P[index] < n:
			high = biS(P, func, low=index-1, high=high)
			appendPF(P[index:high] * Pprod)
			PH[-1] += 1
		else:
			for i in range(-2, -pf-1, -1):
				if PH[i] != index:
					PH[i:] = [PH[i] + 1] * (-i)
					high = None
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
