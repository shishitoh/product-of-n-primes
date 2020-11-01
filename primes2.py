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

	func = lambda p:(lambda x:(powP[p][x]*P[x] < n))
	for p in range(pf):
		tmpP = mytakewhile(powP[p], func(p))
		powP.append(tmpP * P[:len(tmpP)])
		print(powP[-1])
	del tmpP

	T = np.zeros(n, dtype=np.uint8)

	for Ps in powP:
		for p in Ps:
			T[p::p] += 1
	del powP

	return np.where(T == pf)[0]


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes2(pf, n)")
	print(primes2(pf, n))