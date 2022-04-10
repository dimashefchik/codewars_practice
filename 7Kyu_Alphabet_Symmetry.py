# Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. 
# Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.
# Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,
# solve(["abode","ABc","xyzD"]) = [4, 3, 1]

import string

def solve(arr):
    if len(arr) >= 1:
        al = string.ascii_lowercase
        result = []
        for item in arr:
            res = 0
            for letter in range(0,len(item)):
                if item.lower()[letter] == al[letter%26]:
                    res += 1
            result.append(res)
        return result
    else:
        return []
