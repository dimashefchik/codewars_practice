# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    s = text.split(' ')
    result = []
    print(s)
    for i in s:
        if i.isalpha():
            i = i[1:] + i[0] + 'ay'
        result.append(i)
    b = ' '.join(result)
    return b
