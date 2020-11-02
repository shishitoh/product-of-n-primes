from binarysearch import *
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

	T = np.zeros(n-2**pf, dtype=np.uint8)

	for p in P:
		T[(int(p - (2**pf))%p)::p] += 1

	func = lambda x:(P[x] < sup)
	for i in range(2, pf+2):
		sup = pow(n, 1/i)
		P = bitakewhile(P, func).astype(np.uint64)
		for p in P:
			p = np.power(p, i, casting="unsafe", dtype=np.uint64)
			T[(int(p - (2**pf))%p)::p] += 1
	del P

	return np.add(np.where(T == pf)[0], 2**pf, casting="unsafe", dtype=np.uint64)


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes2_2(pf, n)")