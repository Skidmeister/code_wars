# Find the sum of the digits of all the numbers from 1 to N (both ends included).

# Examples
# # N = 4
# 1 + 2 + 3 + 4 = 10

# # N = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# # N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51

def compute_sum(n):
    """computes the twisted sum out of given number"""
    nums = [x for x in range(1, n+1)]
    to_summ = []
    l=[]

    for x in nums:
        if x < 10:
            to_summ.append(x)
        elif x >= 10:
            l = [int(d) for d in str(x)]
        for c in l:
            to_summ.append(c)

    return sum(to_summ)