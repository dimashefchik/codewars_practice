# The function parts_sums (or its variants in other languages) will take as parameter a list ls 
# and return a list of the sums of its parts as defined above.
ls = [1, 2, 3, 4, 5, 6]

def parts_sums(ls):
    result = [sum(ls)]
    for i in ls:
        result.append(result[-1]-i)
    return result
