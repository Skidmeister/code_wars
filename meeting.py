# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same first name too.

# Notes
# You can see another examples in the "Sample tests".

def meeting(s):
    guests = s.split(";")
    
    print(guests)
    correct =[]
    ziel = ""
    for g in guests:
        l = g.split(':')
        l.reverse()
        a = (', ').join(l).upper()
        correct.append(a)
        
    correct.sort()
    print(correct)
    for x in correct:
        ziel+=f"({x})"

    return ziel
