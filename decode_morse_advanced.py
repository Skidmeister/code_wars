# In this kata you have to write a Morse code decoder for wired electrical telegraph.
# Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

# When transmitting the Morse code, the international standard specifies that:

# "Dot" – is 1 time unit long.
# "Dash" – is 3 time units long.
# Pause between dots and dashes in a character – is 1 time unit long.
# Pause between characters inside a word – is 3 time units long.
# Pause between words – is 7 time units long.
# However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

# For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.

# For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

# 1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

# As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

# That said, your task is to implement two functions:

# Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
# 2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

# The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).


# Eg:
#   morseCodes(".--") //to access the morse translation of ".--"
# All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

# Good luck!

import re
def decode_bits(bits):
    code = _delete_front_end_zeros(bits)
    timeunit = _find_timeunit(code)
    morseCode = _do_decoding(code, timeunit)
    return morseCode

def _find_timeunit(clean_bits):
    """finds one timeunit"""
    find = re.split("0+", clean_bits)
    find2 = re.findall("0+", clean_bits)
    flag = True
    shortest = 'nico'
    for x in (find + find2):
        if flag:
            shortest = x 
            flag = False
        elif flag == False:
            if len(x) < len(shortest):
                shortest = x
    timeunit = len(shortest)
    return timeunit

#split the message into ones and zeros and create a list of translated shit
#if space between dots and dashes - continue


def _do_decoding(clean_bits, timeunit):
    """does acutal decoding by changing numbers to dots and dashes"""
    find = re.split("0+",clean_bits)
    find2 = re.findall("0+", clean_bits)
    find2.append('koniec')
    message = []
    for x in range(len(find)):
        message.append(find[x])
        message.append(find2[x])

    koniec = message.pop()
    morse_message = []
    for i in message:
        if '1' in i:
            if len(i) == timeunit:
                morse_message.append('.')
            elif len(i) == 3*timeunit:
                morse_message.append('-')
        if '0' in i:
            if len(i) == timeunit:
                continue
            elif len(i) == 3*timeunit:
                morse_message.append(' ')
            elif len(i) == 7*timeunit:
                morse_message.append('   ')
    morse_mess = ('').join(morse_message)
    return morse_mess

  #finding out the number of one signal
def _delete_front_end_zeros(bits):
    l = []
    for char in bits:
        l.append(char)
    score = 0
    while True:
        element = int(l.pop())
        score+=element
        if score == 1:
            l.append(str(element))
            break
        else:
            continue
    score = 0
    while True:
        element = int(l.pop(0))
        score+=element
        if score == 1:
            l.insert(0, str(element))
            break 
        else:
            continue
    code = ('').join(l)
    return code

def decode_morse(morseCode):
    stripped_code = morseCode.strip()
    words = stripped_code.split('   ')
    decoded_words = []
    for word in words:
        decoded_letters = []
        letters = word.split(' ')
        for letter in letters:
            decoded_letter = MORSE_CODE[letter]
            decoded_letters.append(decoded_letter)
        decoded_word = ('').join(decoded_letters)
        decoded_words.append(decoded_word)
    decoded_message = (' ').join(decoded_words)
    return decoded_message

    letters_spaces_l = stripped_code.split(' ')
    decoded_letters_spaces = []
    for x in letters_spaces_l:
        if x in MORSE_CODE.keys():
            decoded_letter = MORSE_CODE[x]
        elif x == (' '):
            decoded_letter = ' '
        decoded_letters_spaces.append(decoded_letter)
    
    string = ('').join(decoded_letters_spaces).upper()
        
    return string