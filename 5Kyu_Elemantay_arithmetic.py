# In elementary arithmetic a "carry" is a digit that is transferred from one column of digits to another column of more significant digits during a calculation algorithm.
# This Kata is about determining the number of carries performed during the addition of multi-digit numbers.
# You will receive an input string containing a set of pairs of numbers formatted as follows:

# 123 456
# 555 555
# 123 594
# And your output should be a string formatted as follows:

# No carry operation
# 3 carry operations
# 1 carry operations
# ###Some Assumptions

# Assume that numbers can be of any length.
# But both numbers in the pair will be of the same length.
# Although not all the numbers in the set need to be of the same length.
# If a number is shorter, it will be zero-padded.
# The input may contain any arbitrary number of pairs.

def solve(a):
    a = a.replace('\n', ' ')
    b = a.split(' ')
    arr = []
    c = []
    m = []
    for i in range(0,len(b),2):
        arr.append(b[i])
        arr.append(b[i+1])
        c.append(arr)
        arr = []
    for d in c:
        count = 0
        plus = 0
        for k in range((len(d[0])-1),-1,-1):
            if (int(d[0][k]) + int(d[1][k])) >= 10:
                count +=1
                plus = 1
            elif (int(d[0][k]) + int(d[1][k])) == 9 and plus == 1:
                count += 1
            else:
                plus = 0
        if count == 0:
            m.append('No carry operation')
        else:
            m.append(f'{count} carry operations')
    return '\n'.join(m)

  
