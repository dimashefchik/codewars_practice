# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    result = []
    if len(s) % 2 != 0:
        s = s + '_'
    for i in range(0,len(s),2):
        print(i)
        result.append(s[i:i+2])
    return result