# Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

# A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") 
# will split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

#  abbreviate("elephant-rides are really fun!") === "e6t-r3s are r4y fun!"


import re

def abbreviate(a):
    words = re.findall('[a-zA-Z]+|\W+|[0-9]|[_]',a)      # \W non alphabes symbols
    b = []
    for word in words:
        if len(word) > 3:
            new_word = word[0] + str(len(word[1:-1])) + word[-1]
            b.append(new_word)
        else:
            b.append(word)
    return ''.join(b)
