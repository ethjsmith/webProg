import re
search_file = 'warpeace.txt'
# A data structure to surpass metal gear, should be easily prgrammatically iterable
terms = {
   "phone number":[
        #r"\d{3}-\d{3}-\d{4}", # ###-###-####
        #r"1-\d{3}-\d{3}-\d{4}", # 1-###-###-####
        #r"\(\d{3}\)\s\d{3}-\d{4}", # (###) ###-####

        r"(1-)?\(?\d{3}\)?\s?[-\s]\d{3}-\d{4}" # this assumes that parenthese are balanced

    ],
    "account number":[
        r"[a-zA-Z]{2}-\d{4}-[a-zA-Z]\d{5}" # AA-####-A#####
    ],
    "ssn":[
        r"\d{3}-\d{2}-\d{4}" # ###-##-####
    ],
    "date":[ # these are more complicated than I originally suspected, matching only valid dates instead of 00/00/0230
        # r"(0[1-9]|1[0-2])\/(0[1-9]|[0-2]\d|3[0-1])\/\d{3}[1-9]", # MM/DD/YYYY
        # r"(0[1-9]|1[0-2])-(0[1-9][0-2]\d|3[0-1])-\d{3}[1-9]", # MM-DD-YYYY
        # r"(0[1-9]|1[0-2])\/(0[1-9][0-2]\d|3[0-1])\/\d[1-9]", # MM/DD/YY
        # r"(0[1-9]|1[0-2])-(0[1-9][0-2]\d|3[0-1])-\d[1-9]", # MM-DD-YY

        r"(0[1-9]|1[0-2])[\/-](0[1-9]|[0-2]\d|3[0-1])[\/-](\d{4}|[1-9]\d)"
    ],
}
# Another data structure to contain the results of each search
results = {"phone number":[0,0,0],"account number":[0],"ssn":[0],"date":[0,0,0,0]}
with open(search_file, 'r') as sf:
    for line in sf:
        for k in terms.keys(): # step through the dictionary by key
            #print(f"searching for {k}")
            for ind,x in enumerate(terms[k]): # using enumerate to get the index as well, so that the count can be added to the results dict
                z =re.findall(x,line) # don't need to compile, because if you call findall with a string, it just compiles the string for you... thanks python
                for a in z: # for each match
                    results[k][ind] += 1
                    print(f" found : {a} (using {k}'s rule:{ind}) in the line \"{line}\"")
print(results) # the dict shows the breakdown of which rule got matched, and the next line tallies the totals for each category
for k in results.keys():
    count = 0
    for i in results[k]:
        count += i
    print(f"There were {count} matches for {k}")
