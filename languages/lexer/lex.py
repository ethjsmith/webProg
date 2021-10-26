# or this assignment, you will need to implement a lexer. The task of the lexer is to read an
# input string and extract tokens out of the input string. Each token extracted must have a type
# and a value. The input code can be your own code or you can use the sample code that is
# provided with the assignment files.


# Your lexer must be able to at least extract the following tokens:

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

def getTokens(l):
    # lexes a single line
    for char in l:
        # look for various types of things



with open("file.txt") as f: # maybe you can pass the filename to the lexer?
    for line in f.readlines():
        print(line)
