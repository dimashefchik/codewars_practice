# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    result = []
    for i in s:
        if i.isupper():
            result.append(' ')
            result.append(i)
        else:
            result.append(i)
    return ''.join(result)

