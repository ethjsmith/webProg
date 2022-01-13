# Ethan Smith CS 4550 Programming languages

# first we need da tree or something
# step one is to parse (haha ) the output file from the lexer
def readin(fname):
    tokens = []
    with open(fname) as f:
        for line in f.readlines():
            t = line.split("Value: ")

            tokens.append((t[0][6:-2],t[1][:-1])) # this is janky, and hackish
    return tokens

print(readin("output.txt"))

def expr(tokens):

    x = "our parse tree lol" # placeholder for parse tree
    valid = False

    if valid:
         return x
    else:
        return valid


def parse(tokens):
    print("parses")

def parseNumber():
    print("TODO")

def parseKeyword():
    print("TODO")

def parseIdentifier():
    print("TODO")

def parseOperator():
    print("TODO")

def parseAssignment():
    print("TODO")

def parseComment():
    print("TODO")

def parseString():
    print("TODO")

def parseEnd():
    print("TODO")
# Some pseudocode

# it seems like I need to start with a bunch of rules? so ill think about that
#
# OUR token types are
# Nymber, keyword, Identifier, Operator, Assignment, Comment, String, and END
#
# With these rules Ill have ambiguity for certain I think

# expr -> [expr] [end]
# expr -> [expr][operator][number]
# expr -> [identifer][assignment][expr] # but wait can assignment be operator as well?
# expr -> [number] | [string] # if we get to the bottom ?
#
# operator -> something that allows order of operation but also [+][-][*][/]
# expr -> [keyword][expr]
#
# do I just skip comments ? like ignore them, they don't exist? except for the purpose of ending a line ?
#
#
