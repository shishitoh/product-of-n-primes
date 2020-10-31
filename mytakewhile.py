def mytakewhile(L, f):
	low = -1
	high = len(L)
	while (high-low) > 1:
		middle = (high+low)//2
		if f(L[middle]):
			low = middle
		else:
			high = middle
	return L[:high]