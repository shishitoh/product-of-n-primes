from mytakewhile import mytakewhile
from sieve import sieve
import numpy as np
from sys import getsizeof

def primes2_2(pf, n):
	if pf <= 0:
		raise ValueError
	elif n <= 2**pf:
		return []

	P = sieve(n)

	if pf == 1:
		return P

	T = np.zeros(n, dtype=np.uint8)

	for p in P:
		T[p::p] += 1

	func = lambda i:(lambda x:(P[x]**i < n))
	for i in range(2, pf+2):
		P = mytakewhile(P, func(i)).astype(np.uint64)
		for p in P:
			p = np.power(p, i, casting="unsafe", dtype=np.uint64)
			T[p::p] += 1
	del P

	return np.where(T == pf)[0].astype(np.uint64)


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes2_2(pf, n)")