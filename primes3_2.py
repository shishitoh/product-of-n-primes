from binarysearch import *
from sieve import sieve
import numpy as np

def primes3_2(pf, n):
	if pf <= 0:
		raise ValueError
	elif n <= 2**pf:
		return []

	P = sieve(-(-n >> (pf-1))) # 小数点以下切り上げ

	if pf == 1:
		return P

	PF = []
	appendPF = PF.append

	func1 = lambda x: (P[x]**2 < -(-n >> (pf-2)))
	func2 = lambda x: (P[x+j]*p < -(-n >> (pf-2)))
	for j, p in enumerate(bitakewhile(P, func1)):
		appendPF(bitakewhile(P[j:], func2) * p)

	func1 = lambda x: (PF[x][0]*P[x] < -(-n >> (pf-i)))
	func2 = lambda x: (PF[j][x]*p < -(-n >> (pf-i)))
	func3 = lambda x: (PF[x][0]*p < -(-n >> (pf-i)))
	func4 = lambda x: (S[x]*p < -(-n >> (pf-i)))
	for i in range(3, pf+1):
		tophigh = biS(P, func1, high=len(PF))
		for j, p in enumerate(P[:tophigh]):
			PF[j] = [bitakewhile(PF[j], func2) * p]
			high = biS(PF, func3, low=j)
			for S in PF[j+1:high]:
				PF[j].append(bitakewhile(S, func4) * p)
			PF[j] = np.concatenate(PF[j])
			PF[j].sort()
		PF = PF[:tophigh]


	PF = np.concatenate(PF)
	PF.sort()

	return PF




if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes3_2(pf, n)")