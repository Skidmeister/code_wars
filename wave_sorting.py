# A list of integers is sorted in “Wave” order if alternate items are not less than their immediate neighbors (thus the other alternate items are not greater than their immediate neighbors).

# Thus, the array [4, 1, 7, 5, 6, 2, 3] is in Wave order because 4 >= 1, then 1 <= 7, then 7 >= 5, then 5 <= 6, then 6 >= 2, and finally 2 <= 3.

# The wave-sorted lists has to begin with an element not less than the next, so [1, 4, 5, 3] is not sorted in Wave because 1 < 4

# Your task is to implement a function that takes a list of integers and sorts it into wave order in place; your function shouldn't return anything.

# Note:

# The resulting array shouldn't necessarily match anyone in the tests, a function just checks if the array is now wave sorted.

def wave_sort(a):
    """sorts a list into a wave"""
    wave =[]
    a.sort()
    if len(a) %2 == 1:
        part_1 = a[len(a)//2:]
        part_2 = a[:len(a)//2]
        _shuffle(part_1, part_2, wave)
        last_pop = part_1.pop()
        wave.append(last_pop)
    elif len(a) % 2 == 0:
        part_1 = a[len(a)//2:]
        part_2 = a[:len(a)//2]
        _shuffle(part_1, part_2, wave)

    a.clear()
    for x in wave:
        a.append(x)


def _shuffle(part_1, part_2, wave):
    """from a sorted divided into 2 list, shuffles big with small numbers"""
    while part_2:
        popped_1 = part_1.pop(0)
        wave.append(popped_1)
        popped_2 = part_2.pop(0)
        wave.append(popped_2)