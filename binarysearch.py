def upper_bound(low, high, func):
    low -= 1
    while (high-low) > 1:
        middle = (high+low)//2
        if func(middle):
            low = middle
        else:
            high = middle
    return high


def binary_takewhile(L, func, low=0, high=None):
    low -= 1
    if high is None:
        high = len(L)
    while (high-low) > 1:
        middle = (high+low)//2
        if func(middle):
            low = middle
        else:
            high = middle
    return L[:high]
