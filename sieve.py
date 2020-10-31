import numpy as np
import math


def sieve(n):
	T = np.ones(n, dtype="bool")
	T[4::2] = False
	for i in range(3, int(math.sqrt(n)), 2):
		if T[i]:
			T[i*i::2*i] = False
	return np.nonzero(T)[0][2:]


if __name__ == "__main__":
	import time
	n = eval(input("n = "))
	start = time.time()
	print(sieve(n))
	print(time.time()-start)
	input()
