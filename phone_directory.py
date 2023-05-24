# John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and the address.

# Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with non-alpha-numeric characters (except inside phone number and name).

# Examples of John's phone book lines:

# "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"

# " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

# "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"

# Could you help John with a program that, given the lines of his phone book and a phone number num returns a string for this number : "Phone => num, Name => name, Address => adress"

# Examples:
# s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

# phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
# It can happen that there are many people for a phone number num, then return : "Error => Too many people: num"

# or it can happen that the number num is not in the phone book, in that case return: "Error => Not found: num"

# Notes
# Codewars stdout doesn't print part of a string when between < and >

# You can see other examples in the test cases.

import re

def phone(strng, num):
    
    splitted = strng.strip().split('\n')
    
    #patterns
    number_pattern = r'[\d]{1,2}-[\d]{3}-[\d]{3}-[\d]{4}'
    name_pattern = r'<.+>'
    adress_code_pattern = r'\w+-\d+'
    street_pattern = r'[a-zA-Z0-9\.]+'
    trash_pattern = r'[^a-zA-Z0-9\s\._-]'
    underscore = r'_'
    
    #counter to check how many times the number exists in the list
    number_presence = 0
    
    for line in splitted:
        span = re.search(number_pattern, line).span()
        number_test = line[span[0]:span[1]]
        if number_test != num:
            continue
        number = line[span[0]:span[1]]
        number_presence +=1
        part_1 = line[0:span[0]]
        part_2 = line[span[1]:]
        no_number_line = part_1+';'+part_2

        name_span = re.search(name_pattern, no_number_line).span()
        name=no_number_line[name_span[0]+1:name_span[1]-1]

        part_a = no_number_line[0:name_span[0]]
        part_b = no_number_line[name_span[1]:]
        no_name_line = part_a +';'+part_b

        while re.search(trash_pattern, no_name_line):

            trash = re.search(trash_pattern, no_name_line)
            part_10 = no_name_line[:trash.start()]
            part_11 = no_name_line[trash.end():]
            no_name_line= part_10+part_11


        no_name_line=no_name_line.strip()
        space = re.search(r'\s{2,}', no_name_line)

        if space:
            part_12 = no_name_line[:space.start()]
            part_13 = no_name_line[space.end():]
            no_name_line=part_12+' '+part_13


        undrscr = re.search(underscore, no_name_line)
        if undrscr:
            p_1 = no_name_line[:undrscr.start()]
            p_2 = no_name_line[undrscr.end():]
            no_name_line = p_1+' '+p_2
        no_name_line = no_name_line.strip()
        
    if number_presence == 0:
        return f"Error => Not found: {num}"
    elif number_presence >=2:
        return f"Error => Too many people: {num}"
    else:
        return f'Phone => {number}, Name => {name}, Address => {no_name_line}'