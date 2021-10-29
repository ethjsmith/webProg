# or this assignment, you will need to implement a lexer. The task of the lexer is to read an
# input string and extract tokens out of the input string. Each token extracted must have a type
# and a value. The input code can be your own code or you can use the sample code that is
# provided with the assignment files.


# Your lexer must be able to at least extract the following tokens:
#+-*/% == != > < >= <= ! || &&
# Identifiers
# Numbers
# Operators (including assignment operators)
# Assignment operator/s
# Comments (you can just let your lexer ignore them or have them a token of type comment)
# Strings
# Keywords (need to include description)
# End of statement (you can choose any character or end of line to signal the end of statement)


# you can add more to it if you would like
# You must read the code from a file
# For each extracted token, you need a type and a value
# Description is only included for keywords
# You can use any programming language to code your lexer

# funny meme: language with no symbols, gotta type everything as words


import re

def printtoken(t): # prints out the token in the format presented by the assignment
    print(f"Type: {t[0]} \tValue: {t[1]}")
def isIdentifier(s): # this is like a variable ? I don't know how to make it match that ... unquoted string not matched by keyword I guess
    if (re.match(r"^[a-z][a-z\d]*$",s)):
        #print(f" Found Identifier :{s}")
        return ["Identifier",s]
    else:
        return 0
def isNumber(s):
    #if (re.match(r"\d+\.?\d*",s)):
    if (re.match(r"^\d+\.?\d*$",s)): # trim the newline character LOL
        #print(f" Found number :{s}")
        return ["Number",s]
    else:
        return 0

def isOperator(s): # there are other operators that are multicharacter too I think like comparasion ==
    if (re.match(r"^([\+\*\-\/><!%]|[\<\>=!]=|\|\||\&\&)$",s)):
        #print(f" Found operator :{s}")
        return ["Operator",s]
    else:
        return 0
def isAssignment(s):
    if (re.match(r"^=$",s)): # ez?
        #print(f" Found assignment :{s}")
        return ["Assignment",s]
    else:
        return 0
def isComment(s): # two comments  ?
    if (re.match(r"^[#].*$",s)):
        #print(f" Found comment :{s}")
        return ["Comment",s]
    else:
        return 0
def isString(s):# this probably doesn't work
    if (re.match(r"^\".*\"$",s)):
        #print(f" Found String :{s}")
        return ["String",s]
    else:
        return 0
def isKeyword(s): # I guess this just matches all the specific keywords in the language?
    if (re.match(r"^[A-Z]+$",s)): # Keywords are UPPER case, identifiers are lower
        #print(f" Found keyword :{s}")
        return ["Keyword",s]
    else:
        return 0
def isEnd(s): # should I make a character at the end? I don't personally like that, but it's easier ...

    if (re.match(r"^;$",s)):
        #print(f" Found endline :{s[:-1]}") # trim endline character when printing, because this is janky af
        return ["Endline",s]
    else:
        return 0
def callall(s): # checks every token against a string
    if s == "":
        return -1
    num = isNumber(s)
    key = isKeyword(s)
    #if not num and not key:
    id = isIdentifier(s)

    op = isOperator(s)
    asi = isAssignment(s)
    com = isComment(s)
    str = isString(s)

    end = isEnd(s)
    # print(locals())
    # for var in locals():
    #     if var and var != "s":
    #         print(f"NICE::: {var[0]}")
    found = False
    for token in (num,key,id,op,asi,com,str,end):
        if token:
            printtoken(token)
            found = True
    if not found: # if the token is an error
        print(f"Type: ERROR \tValue{s}")
def parseLine(l):
    full = ""
    str = False
    for c in l:
        full += c # full sequence we're checking
        if c == "\"" or (c =="#" and str == False):
            if str:
                str = False
                callall(full)
                full=""
            else:
                str = True
        if c ==" " and str == False:
            #isNumber(full)
            a = full.rstrip()
            callall(a)
            full = ""
        #print(full)
    a = full.strip()
    callall(a)
    print()


with open("file.txt") as f: # maybe you can pass the filename to the lexer?
    for line in f.readlines():
        #print(line)
        parseLine(line)
