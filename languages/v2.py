# Ethan Smith
# Programming languages Regex assignment
# 10/14/2021
import re
search_file = 'warpeace.txt'
# list contains the type of regex, the actual regex, and a count of number of times it was found
terms = [
    ["phone number",r"(1-)?\(?\d{3}\)?\s?[-\s]\d{3}-\d{4}",0], #storing the regex as raw strings so that python wont escape/interpret some of the charaters
    ["account number",r"[a-zA-Z]{2}-\d{4}-[a-zA-Z]\d{5}",0],
    ["ssn",r"\d{3}-\d{2}-\d{4}",0],
    ["date",r"(0[1-9]|1[0-2])[\/-](0[1-9]|[0-2]\d|3[0-1])[\/-](\d{4}|[1-9]\d)",0],
]
with open(search_file, 'r') as sf:
    for line in sf:
        for term in terms: # for each type of item, match the regex in each line
            matches = re.findall(term[1],line)
            for match in matches:
                term[2] += 1 # total up all the regex, ( and print where it was found )
                print(f" Found: {term[0]} in line: {line}")
for term in terms: # report the end result
    print(f"Found {term[2]} {term[0]}'s")
