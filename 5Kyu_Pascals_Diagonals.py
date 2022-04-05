# Create a function that returns an array containing the first l numbers from the nth diagonal of Pascal's triangle.

# n = 0 should generate the first diagonal of the triangle (the ones).
# The first number in each diagonal should be 1.
# If l = 0, return an empty array.
# Both n and l will be non-negative integers in all test cases.

def generate_diagonal(l, n):
    arr = []
    for i in range(n+l):
        arr.append([1]+[0]*((n+l)+1))
    for i in range(0, n+l):
        for j in range(0,i+1):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    result = []
    count = 0
    for k in range(l,l+n):
        result.append(arr[k][count])
        count += 1
    return result
