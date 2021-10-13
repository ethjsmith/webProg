import re

# search_file = input("What file do you want to search? ")
search_file = 'warpeace.txt'
#search_term = input("What are you looking for? ")

# return when you find a match, count of matches, count of each section match
        # Phone numbers in the forms:
        # ###-###-####
        # 1-###-###-####
        # (###) ###-####
        # Account numbers:
        # AA-####-A#####
        # SSN:
        # ###-##-####
        # Dates:
        # ##/##/#### (in the form of MM/DD/YYYY)
        # ##-##-#### (in the form of MM-DD-YYYY)
        # ##/##/## (in the form of MM/DD/YY)
        # ##-##-## (in the form of MM-DD-YY)

# A data structure to surpass metal gear, should be easily prgrammatically iterable
terms = {
   "phone number":[
        r"\d{3}-\d{3}-\d{4}",
        r"1-\d{3}-\d{3}-\d{4}",
        r"\(\d{3}\)\S\d{3}-\d{4}",
    ],
    "account number":[
        r"[a-zA-Z]{2}-\d[4]-[a-zA-Z]\d[5]" # is this even right ??
    ],
    "ssn":[
        r"\d{3}-\d{2}-\d{4}"
    ],
    "date":[ # these are more complicated than I originally suspected, matching only valid dates instead of 00/00/0230
        r"(0[1-9]|1[0-2])\/(0[1-9]|[0-2]\d|3[0-1])\/\d{3}[1-9]", # MM/DD/YYYY
        r"(0[1-9]|1[0-2])-(0[1-9][0-2]\d|3[0-1])-\d{3}[1-9]", # MM-DD-YY
        r"(0[1-9]|1[0-2])\/(0[1-9][0-2]\d|3[0-1])\/\d[1-9]",
        r"(0[1-9]|1[0-2])-(0[1-9][0-2]\d|3[0-1])-\d[1-9]",
    ],
}
results = {"phone number":[0,0,0],"account number":[0],"ssn":[0],"date":[0,0,0,0]}
with open(search_file, 'r') as sf:
    for line in sf:
        for k in terms.keys():
            #print(f"searching for {k}")
            for ind,x in enumerate(terms[k]): # using enumerate to get the index as well, so that the count can be added to the results dict
                z =re.findall(x,line) # don't need to compile, because if you call findall with a string, it just compiles the string for you... thanks python
                for a in z: # for each match
                    results[k][ind] += 1
                    print(f" found : {a} (on {k},{ind}) at {line}")
#print(terms)
print(results)
    # b = False
    # i = 0
    # reg_ex = re.compile(search_term)
    # for line in sf:
    #     # m = re.search(reg_ex, line)
    #     m = re.findall(reg_ex, line)
    #     if m:
    #         print("\nFound it!")
    #         print(line.strip())
    #         # print(m.group(0))
    #         for item in m:
    #             print(item)
    #             i += 1
    #         b = True
    # if not b:
    #     print("Didn't find it.")
    # else:
    #     print(f"Found {i} instances.")
