from binarysearch import *
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
	func = lambda x: (PF[x]*p < -(-n >> (pf-i)))
	for i in range(2, pf+1):
		ip = 2**i
		T = np.zeros(n-ip, dtype=np.bool)
		for p in P:
			T[(bitakewhile(PF, func) * p) - ip] = True
		PF = np.add(np.nonzero(T)[0].astype(np.uint64), np.uint64(ip))
		del T

	return PF


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes3(pf, n)")