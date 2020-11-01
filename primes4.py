from mytakewhile import mytakewhile
from sieve import sieve
import numpy as np

def primes4(pf, n):
	if pf <= 0:
		raise ValueError
	elif n <= 2**pf:
		return []

	P = sieve(-(-n >> (pf-1)))

	if pf == 1:
		return P

	PH  = [0] * (pf - 1)
	sup = pow(n, 1/pf)
	PL = []
	func = lambda Pprod:(lambda x:(Pprod*P[x+index] < n))
	while P[PH[0]] < sup:
		index = PH[-1]
		Pprod = np.prod(P[PH])
		if Pprod * P[index] < n:
			PL.append(mytakewhile(P[index:], func(Pprod)) * Pprod)
			PH[-1] += 1
		else:
			for i in range(-2, -pf-1, -1):
				if PH[i] != index:
					PH[i:] = [PH[i] + 1] * (-i)
					break
	del P

	PF = np.concatenate(PL)
	PF.sort()

	return PF


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes4(pf, n)")
