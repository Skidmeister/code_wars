# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

import re

def change_word(word):
    '''moves first letter to the end and adds "ay" '''
    return word[1:]+word[0]+'ay'
	
def pig_it(sentence):
    '''uses change_word() function and applies it to a all words in a sentence'''
    words =re.findall(r"\b[a-zA-Z]+\b",sentence)
    changed_words = [change_word(w) for w in words]
    for i, word in enumerate(words):
        sentence = re.sub(r"\b" + word + r"\b", changed_words[i], sentence)
    return sentence