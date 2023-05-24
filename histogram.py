# Background
# A 6-sided die is rolled a number of times and the results are plotted as a character-based histogram.

# Example:

#     10
#     #
#     #
# 7   #
# #   #
# #   #     5
# #   #     #
# # 3 #     #
# # # #     #
# # # # 1   #
# # # # #   #
# -----------
# 1 2 3 4 5 6
# Task
# You will be passed all the dice roll results, and your task is to write the code to return a string representing a histogram, so that when it is printed it has the same format as the example.

# Notes
# There are no trailing spaces on the lines
# All lines (including the last) end with a newline \n
# A count is displayed above each bar (unless the count is 0)
# The number of rolls may vary but is always less than 100

def histogram(rolls):
    """makes a histogram out of a list"""

    kreski = '-----------\n'
    liczby = '1 2 3 4 5 6\n'

    #creating a horizontal matrix
    maxx = max(rolls)
    matrix =[]
    for x in rolls:
        l=[]
        for a in range(x):
            l.append('#')
        if x != 0:
            l.append(str(x))
        else:
            l.append(' ')
        for b in range(maxx-x):
            l.append(' ')
        matrix.append(l)

    #flipping the matrix
    flipped_matrix =[]
    for x in range(1,maxx+2):
        line=[]
        for l in matrix:        
            popped = l.pop(-1)            
            line.append(popped)            
        flipped_matrix.append(line)

    final_string=''
    for i in flipped_matrix:
        w = ''
        for q in i:
            if len(q) == 2:
                w +=q
            elif len(q) == 1:
                w+=q
                w+=' '
        z = w.rstrip()
        z +='\n'
        final_string+=z
    final_string+=kreski
    final_string+=liczby

    return final_string
    