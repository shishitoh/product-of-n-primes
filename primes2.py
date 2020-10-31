from mytakewhile import mytakewhile
from sieve import sieve
import numpy as np

def primes2(pf, n):
	if pf <= 0:
		raise ValueError
	elif n <= 2**pf:
		return []

	P = sieve(n)

	if pf == 1:
		return P

	powP = [P]
	for p in range(1, pf):
		func = lambda x:(powP[p-1][x]*P[x] < n)
		tmpP = mytakewhile(powP[p-1], func)
		powP.append(tmpP * P[:len(tmpP)])
	del tmpP

	T = np.zeros(n, dtype=np.uint8)

	for Ps in powP:
		for p in Ps:
			T[p::p] += 1
	del powP

	return np.where(T == pf)


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes2(pf, n)")