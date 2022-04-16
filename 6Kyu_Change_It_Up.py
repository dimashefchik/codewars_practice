# Create a function that takes a string as a parameter and does the following, in this order:
# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:
# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
# So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)


import string
def changer(s):
    alph = string.ascii_lowercase
    vowels = 'aeiou'
    res = ''
    for x in s:
        if x.lower() in alph:
            print(x.lower())
            letter = alph[(alph.index(x.lower()) + 1) % 26]
            if letter in vowels:
                res += letter.upper()
            else:
                res += letter
        else:
            res += x
    return res
  
  print(changer("Cat30"))
