# Overview
# Your task is to decode a qr code. You get the qr code as 2 dimensional array, filled with numbers. 1 is for a black field and 0 for a white field. It is always a qr code of version 1 (21*21), it is always using mask 0 ((x+y)%2), it is always using byte mode and it always has error correction level H (up to 30%). The qr code won't be positioned wrong and there won't be any squares for positioning exept the three big ones in the corners.

# You should return the message inside the qr code as string.
# The QR Code will always be valid and be of version 1, meaning the decoded message will never be more than 8 characters long.

# Input/ouput
# Input: 2D array of 0 (white) and 1 (black) values
# Output: the decoded message, according to the process described below.

# Decoding a QR-code
# Here comes the explaination on how to decode a qr code. You can skip it, if you already know how it works:

# Positioning information
# First of all we have to take a look at the big three positioning fields in the corners.

# Mask information
# The bits next to the positioning fields give us information about the mask and the error correction level the qr code uses. I wrote above that it is always mask 0 and always error correction level H, so we can also ignore that stuff.

# Decoding information
# We have to build a bit sequence now. In order to do that we will use mask 0 definition which is ((x+y)%2)==0, where:

# x and y are the indexes of our 2 dimensional array (0-based)
# if the condition of our mask is true, we have to convert the pixel: black -> 0 and white -> 1
# A mask is used to prevent long sequences of identical bits so that a scanner can better recognize the code
# For each black field add 1 to our bit sequence and for each white field add 0 to our bit sequence, don't forget that many bits get converted because of mask 0.

# Let's do the first bits together:

# We start with the first pixel (in the lower right corner, where also the red arrow begins) which is black, but we have to use mask because (20+20)%2 is 0, therefore we don't add 1 to our bit sequence but 0.
# Next field is white. This time we don't use mask because (20+19)%2 isn't 0, so we add a 0 to our bit sequence.
# Next field is black. This time we don't use mask because (19+20)%2 isn't 0, so we add a 1 to our bit sequence.
# Important (!): Since we're limiting ourselves to version 1, we have to continue that process only until our bit sequence is 76 long, because the input will never be longer than eight characters.

# At the end you get a bit sequence:

# bits:      0100000000100100100001101001000011101100000100011110110000010001111011001111
# legend:    MMMMssssssss...

# - "M": mode bits (4 bits)
# - "s": size message bits (8 bits)
# - ...: message bits and error correction information
# This bit sequence is representing the following information

# First 4 bits show mode: 0100. This isn't important for us, because I told you before that we will use always byte mode in this kata.
# The following 8 bits show the length of the encoded word: 00000010. This is the binary representation of number 2, so we know our word is 2 characters long.
# The following bits are data bits followed by error correction bits (but you can ignore error correction bits, because there won't be any errors). We know our word is 2 chars long, so we take the next 16 bits (because 1 char=8 bits):
# First group of 8 bits: 01001000. This is 72 in decimal which is ascii value of "H".
# Second group of 8 bits: 01101001. This is 105 in decimal which is ascii value of "i".
# Since we don't handle in this kata error correction, we got our word/output: "Hi".

# Good luck :)

def scanner(qrcode):
    """Simplest QR code scanner"""

    bit_sequence = ''

    for x in reversed(range(9,21)):
            a = qrcode[x][20]
            b = qrcode[x][19]
            if (x+20)%2 == 0:
                if a == 1:
                    a=0
                elif a == 0:
                    a=1
            bit_sequence += str(a)
            if (x+19)%2 == 0:
                if b == 1:
                    b=0
                elif b == 0:
                    b=1
            bit_sequence += str(b)

    for x in range(9,21):
            a = qrcode[x][18]
            b = qrcode[x][17]
            if (x+18)%2 == 0:
                if a == 1:
                    a=0
                elif a == 0:
                    a=1
            bit_sequence += str(a)
            if (x+17)%2 == 0:
                if b == 1:
                    b=0
                elif b == 0:
                    b=1
            bit_sequence += str(b)

    for x in reversed(range(9,21)):
            a = qrcode[x][16]
            b = qrcode[x][15]
            if (x+16)%2 == 0:
                if a == 1:
                    a=0
                elif a == 0:
                    a=1
            bit_sequence += str(a)
            if (x+15)%2 == 0:
                if b == 1:
                    b=0
                elif b == 0:
                    b=1
            bit_sequence += str(b)

    for x in range(9,21):
        if len(bit_sequence) == 76:
            break
        a = qrcode[x][14]
        b = qrcode[x][13]
        if (x+14)%2 == 0:
            if a == 1:
                a=0
            elif a == 0:
                a=1
        bit_sequence += str(a)
        if (x+13)%2 == 0:
            if b == 1:
                b=0
            elif b == 0:
                b=1
        bit_sequence += str(b)

    print(len(bit_sequence))
    bit_sequence_l = list(bit_sequence)
    bit_sequence_l_important = bit_sequence_l[4:]
    length = int(('').join(bit_sequence_l_important[:8]), 2)
    print(length)

    word_sequence = bit_sequence[12:]
    letters_asci = []
    new_word_sequence = word_sequence[:]

    for x in range(length):
        letter = int(('').join(word_sequence[0+x*8:8+x*8]),2)
        letters_asci.append(letter)
    letters = [chr(x) for x in letters_asci]
    solved = ('').join(letters)
    solved.encode('utf-8')
    return solved