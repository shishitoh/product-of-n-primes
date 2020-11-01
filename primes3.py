from mytakewhile import mytakewhile
from sieve import sieve
import numpy as np

def primes3(pf, n):
	if pf <= 0:
		raise ValueError
	elif n <= 2**pf:
		return []

	P = sieve(n)

	if pf == 1:
		return P

	PF = P.copy()
	func1 = lambda x:(PF[0]*P[x] < n)
	func2 = lambda p:(lambda x:(PF[x]*p < n))
	for _ in range(2, pf+1):
		P = mytakewhile(P, func1)
		T = np.zeros(n, dtype=np.bool)
		for p in P:
			T[mytakewhile(PF, func2(p)) * p] = True
		PF = np.nonzero(T)[0]

	return PF


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes3(pf, n)")