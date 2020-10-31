from mytakewhile import mytakewhile

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
	PF[1] = [2, 3, 5]
	PF[2] = [4]
	
	for i in range(6, n):
		primecount = 0
		divi = i
		for p in [2, 3, 5]:
			while divi % p == 0:
				primecount += 1
				divi //= p
		if primecount:
			for j in range(0, pf+1-primecount):
				func = (lambda x:x <= i//2)
				if divi in mytakewhile(PF[j], func):
					PF[j+primecount].append(i)
					break
		else:
			for j in range(1, pf+1):
				func = (lambda x:x <= i//2)
				if all(i % k for k in mytakewhile(PF[j], func)):
					PF[j].append(i)
					break
	return PF[pf]


if __name__ == "__main__":
	import time
	pf = eval(input("pf = "))
	n = eval(input("n = "))
	start = time.time()
	print(primes1(pf, n))
	print(time.time()-start)
	input()