# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

import re

def increment_string(string):
    """adds one to string without number at the end or adds one to the number"""
    l = list(string)
    try:
        end_numbers=[]
        while True:
            try:
                last = int(l[-1])
                popped = l.pop()
                end_numbers.append(popped)
            except ValueError:
                break
            except IndexError:
                break
        
        end_numbers.reverse()

        #determine the length of the digitis at the end, will be handy later
        length = len(end_numbers)

        nums = ('').join(end_numbers)

        #for the case of only zeros which cannot be stripped use regex
        only_zeros = re.search('^0*$', nums)
        if only_zeros:
            n = 1
        else:
            n = int(nums.lstrip('0'))+1
        c = str(n).zfill(length)
        x = ('').join(l)
        final = x+c
    except ValueError:
        final = string+'1'
    
    return final