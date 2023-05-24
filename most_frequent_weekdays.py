# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

# You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

# Input: Year as an int.

# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

# Preconditions:

# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.
# Examples (input -> output):
# * 2427 -> ['Friday']
# * 2185 -> ['Saturday']
# * 2860 -> ['Thursday', 'Friday']

import calendar
from collections import Counter

def most_frequent_days(year):
    """finds the most frequent days in a year and reaturns a list of these days"""
    c = calendar.Calendar(0)
    days =[]
    y = c.yeardatescalendar(year, width=3)
    for x in y:
        for a in x:
            for b in a:
                for d in b:
                    if d.year == year:
                        days.append(d.weekday())
                    else:
                        continue

    counter = Counter(days)
    cmc=counter.most_common(2)
    #it will always be either 1 or 2 days
    dayz = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    result = []
    top_1_date = cmc[0][0]
    top_2_date = cmc[1][0]
    top_1 = cmc[0][1]
    top_2 = cmc[1][1]
    
    if top_1 > top_2:
        result.append(dayz[top_1_date])
    elif top_1 == top_2:
        result.append(dayz[top_1_date])
        result.append(dayz[top_2_date])

    if result == ['Sunday','Monday']:
        #the only instance where I have to switch the sequence
        result.reverse()
    return result