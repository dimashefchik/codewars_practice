# Using n as a parameter in the function pattern, where n>0, complete the codes to get the pattern (take the help of examples):
# Note: There is no newline in the end (after the pattern ends)

# Examples
# pattern(3) should return "1\n1*2\n1**3", e.g. the following:
# 1
# 1*2
# 1**3

def pattern(n):
    result = []
    count = 0
    start = 1
    s = '*'
    while count < n:
        if count >0:
            result.append(f'{start}{s*(count)}{count+1}')
        else:
            result.append(str(start))
        count += 1
    return '\n'.join(result)
