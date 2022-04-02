# The function 'fibonacci' should return an array of fibonacci numbers. The function takes a number as an argument to decide how many no. of elements to produce. If the argument is less than or equal to 0 then return empty array

# Example:
# fibonacci(4) # should return  [0,1,1,2]
# fibonacci(-1) # should return []

def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    result = []
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        while count < n:
            result.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return result

a = fibonacci(7)
print(a)
