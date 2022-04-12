# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.
  
def solution(number):
    ar = []
    div = 1
    while div < number:
        if div % 3 == 0 and div % 5 != 0:
            ar.append(div)
        elif div % 5 == 0:
            ar.append(div)
        div +=1
    return sum(ar)
