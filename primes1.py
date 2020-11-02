from binarysearch import *

def primes1(pf, n):
	if pf <= 0:
		raise ValueError
	if n <= 2**pf:
		return []

	PF = [[1]]
	tmp = 2
	while tmp < n:
		PF.append([])
		tmp *= 2
	for i in range(2, n):
		for j in range(1, pf+1):
			if PF[j] == []:
				PF[j].append(i)
				break
			else:
				func = (lambda x:x <= i//2)
				if all(i % k for k in bitakewhile(PF[j], func)):
					PF[j].append(i)
					break
	return PF[pf]


if __name__ == "__main__":
	import cProfile
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	cProfile.run("primes1(pf, n)")