# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
# ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.
Example
"test" ---> "grfg")
"Test" ---> "Grfg")

import string
def rot13(message):
    aplphabet = string.ascii_lowercase
    aplphabet_up = string.ascii_uppercase
    result = []
    for letter in message:
        if letter in aplphabet:
            number = aplphabet.index(letter) + 13
            if number > len(aplphabet)-1:
                number = number - len(aplphabet)
            result.append(aplphabet[number])
        elif letter in aplphabet_up:
            number = aplphabet_up.index(letter)  + 13
            if number > len(aplphabet_up)-1:
                number = number - len(aplphabet_up)
            result.append(aplphabet_up[number])
        else:
            result.append(letter)
    return ''.join(result)
