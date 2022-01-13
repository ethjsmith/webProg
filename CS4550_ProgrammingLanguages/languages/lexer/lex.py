# Ethan Smith CS 4550 programming languages

import re

def printtoken(t): # prints out the token in the format presented by the assignment
# also writes it to a file, because that seems like a requirement according to the submission page ?
    out = f"Type: {t[0]} \tValue: {t[1]}"
    with open("output.txt", "a") as f:
        f.write(out + "\n")
        print(out)
# here are a bunch of functions that each check if a selected segment is of their type using regex
def isIdentifier(s): # this is like a variable ? I don't know how to make it match that ... unquoted string not matched by keyword I guess
    if (re.match(r"^[a-z][a-z\d]*$",s)):
        #print(f" Found Identifier :{s}")
        return ["Identifier",s]
    else:
        return 0
def isNumber(s):
    if (re.match(r"^\d+\.?\d*$",s)): # numbers can be decimal or just a regular number
        #print(f" Found number :{s}")
        return ["Number",s]
    else:
        return 0

def isOperator(s): # there are other operators that are multicharacter too I think like comparasion ==
    if (re.match(r"^([\+\*\-\/\(\)><!%]|[\<\>=!]=|\|\||\&\&)$",s)):
        #print(f" Found operator :{s}")
        return ["Operator",s]
    else:
        return 0
def isAssignment(s):
    if (re.match(r"^=$",s)): # I don't know of any other assignment operators that aren't just shortcuts like +=
        #print(f" Found assignment :{s}")
        return ["Assignment",s]
    else:
        return 0
def isComment(s): # Comments function like strings, in that they can be closed with another # sign
    if (re.match(r"^[#].*$",s)):
        #print(f" Found comment :{s}")
        return ["Comment",s]
    else:
        return 0
def isString(s):# Anything that is surrounded by quotes
    if (re.match(r"^\".*\"$",s)):
        #print(f" Found String :{s}")
        return ["String",s]
    else:
        return 0
def isKeyword(s):
    if (re.match(r"^[A-Z]+$",s)): # In this languages' syntax Keywords are UPPER case, identifiers are lower
        #print(f" Found keyword :{s}")
        return ["Keyword",s]
    else:
        return 0
def isEnd(s): # I don't really like an endline character, but ill keep it in case it makes the parsing easier

    if (re.match(r"^;$",s)):
        return ["Endline",s]
    else:
        return 0
def callall(s):
    if s == "": # this skips empty tokens like when an end of line is included.
        return -1
    # checks every token against a string
    num = isNumber(s)
    key = isKeyword(s)
    id = isIdentifier(s)
    op = isOperator(s)
    asi = isAssignment(s)
    com = isComment(s)
    str = isString(s)
    end = isEnd(s)

    found = False # this checks if a token type was found, if not it is tagged as not found
    for token in (num,key,id,op,asi,com,str,end):
        if token:
            printtoken(token)
            found = True
    if not found: # if the token is an error/ invalid identifier... an example would be an unclosed string, or a number with multiple dots
        #print(f"Type: ERROR \tValue{s}")
        printtoken(["ERROR",{s}])
def parseLine(l):
    full = ""
    str = False
    for c in l: # step through each character in the line
        full += c # full sequence we're checking
        if c == "\"" or (c =="#" and str == False): # checks if we're leaving a string or comment, and checks it type
            if str:
                str = False
                callall(full)
                full=""
            else:
                str = True
        if c ==" " and str == False: # hits a space, which is the delimiter between tokens
            a = full.rstrip() # stip newline character
            callall(a)
            full = ""
    a = full.strip() # run once more after the loop ends to clear the last thing in the buffer*
    callall(a)
    print()

open("output.txt", "w").close() # wipes out anything in an old file from a previous run 
with open("file.txt") as f: # reads the file, and steps through each line
    for line in f.readlines():
        parseLine(line)
