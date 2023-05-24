# DESCRIPTION:
# Create your own mechanical dartboard that gives back your score based on the coordinates of your dart.

# Finish method:
# def get_score(x,y):
# The coordinates are `(x, y)` are always relative to the center of the board (0, 0). The unit is millimeters. If you throw your dart 5 centimeters to the left and 3 centimeters below, it is written as:
# score = get_score(-50, -30)
# Possible scores are:
# Outside of the board: `"X"`
# Bull's eye: `"DB"`
# Bull: `"SB"`
# A single number, example: `"10"`
# A triple number: `"T10"`
# A double number: `"D10"`
# A throw that ends exactly on the border of two sections results in a bounce out. You can ignore this because all the given coordinates of the tests are within the sections.
# The diameters of the circles on the dartboard are:
# Bull's eye: `12.70 mm`
# Bull: `31.8 mm`
# Triple ring inner circle: `198 mm`
# Triple ring outer circle: `214 mm`
# Double ring inner circle: `324 mm`
# Double ring outer circle: `340 mm`

import math

#prelims
bulls_eye = 12.70
bull = 31.8
triple_ring_inner=198
triple_ring_outer =214
double_ring_inner = 324
double_ring_outer=340
numbers = ['20','1','1', '18','18', '4','4', '13','13', '6','6', '10','10', '15','15','2','2',
            '17','17','3', '3','19', '19', '7','7', '16','16', '8','8', '11','11', '14','14', 
            '9','9','12', '12', '5' ,'5','20']

#code
def _which_ring(x, y):
    '''takes in coordinates and determines which ring was hit'''
    distance = math.sqrt((x**2+y**2))
    ring=''
    if distance <= bulls_eye/2:
        ring="bull's eye"
    elif distance <= bull/2:
        ring="bull"
    elif distance <= triple_ring_inner/2:
        ring = 'normal'
    elif distance <= triple_ring_outer/2:
        ring = 'triple'
    elif distance <= double_ring_inner/2:
        ring = 'normal'
    elif distance <= double_ring_outer/2:
        ring = 'double'
    elif distance > double_ring_outer/2:
        ring = 'out'

    return ring

def angle(x, y):
    if x == 0:
        if y > 0:
            return math.pi/2
        elif y < 0:
            return 3*math.pi/2
        else:
            return None
    else:
        theta = math.atan(y/x)
        if x > 0:
            return theta
        elif y >= 0:
            return math.pi + theta
        else:
            return math.pi + theta


def which_number(x,y):
    '''takes in coordinates and determines the number that was hit'''
    one_space = 2*math.pi/40
    which_space = int(angle(y,x)//one_space)
    answer = numbers[which_space]
    return answer


def get_score(x,y):
    '''main function'''
    ring = _which_ring(x,y)
    if ring =="bull's eye":
        score='DB'
    elif ring == "bull":
        score = 'SB'
    elif ring == 'out':
            score='X'
    elif ring == 'normal' or ring =='triple' or ring=='double':
        number = which_number(x,y)
        if ring == 'double':
            score = 'D'+number
        elif ring == 'triple':
            score= 'T'+number
        elif ring == 'normal':
            score = number

    return score
