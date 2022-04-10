# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

from collections import Counter
def prime_factors(n):
    div = 1
    result = []
    while n != 1:
        div +=1
        while n % div == 0:
            print(div)
            result.append(div)
            n = n/div
    aa = Counter(result)
    s = ''
    for k,v in aa.items():
        if v == 1:
            s += '('+ str(k) + ')'
            continue
        else:
            s += '(' + str(k) +'**'+ str(v) +')'
    return s
