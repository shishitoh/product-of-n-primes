from mytakewhile import mytakewhile
from sieve import sieve
import numpy as np

def primes3(pf, n):
	if pf <= 0:
		raise ValueError
	elif n <= 2**pf:
		return []

	P = sieve(-(-n >> (pf-1))) # 小数点以下切り上げ

	if pf == 1:
		return P

	PF = P.copy()
	func = lambda p:(lambda x:(PF[x]*p < n))
	for _ in range(2, pf+1):
		T = np.zeros(n, dtype=np.bool)
		for p in P:
			T[mytakewhile(PF, func(p)) * p] = True
		PF = np.nonzero(T)[0].astype(np.uint64)

	return PF


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes3(pf, n)")