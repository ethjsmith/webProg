# Ethan Smith

#Create a program that will accept an arbitrary CFG as input and that will output FOLLOW sets for all non-terminals in the grammar.
#The program should read from an input file and output to the console (screen). Submit a zip file that includes your program and input files.

# FIRST Rules:
# 1) FIRST(x) = {x} if x is a terminal
# 2) FIRST(ε) = {ε}
# 3) If <x> → <y>α is a production rule, then add FIRST(<y>) – {ε} to
# FIRST(<x>)
# 4) If <x> → <y>0<y>1<y>2...<y>i<y>i+1...<y>k and ε ∈ FIRST(<y>0) and ε ∈ FIRST(<y>1)
# and ε ∈ FIRST(<y>2) and ... and ε ∈ FIRST(<y>i), then add FIRST(<y>i+1) – {ε} to
# FIRST(<x>)
# 5) If <x> → <y>0<y>1<y>2...<y>k and ε ∈ FIRST(<y>0) and ε ∈ FIRST(<y>1) and ε ∈
# FIRST(<y>2) and ... and ε ∈ FIRST(<y>k), then add ε to FIRST(<x>)

# FOLLOW Rules:
# 1) If <s> is the starting symbol of the grammar, then add $ to FOLLOW(S)
# 2) If <y> → α<x>, then add FOLLOW(<y>) to FOLLOW(<x>),
#    If <x> is right-most symbol in prod rule, add FOLLOW(<y>) to FOLLOW(<x>)
# 3) If <y> → α<x><z>0<z>1<z>2...<z>k and ε ∈ FIRST(<z>0) and ε ∈ FIRST(<z>1) and ε
# ∈ FIRST(<z>2) and ... and ε ∈ FIRST(<z>k), then add FOLLOW(<y>) to FOLLOW(<x>),
#    If everything after <x> can go to ε, then add FOLLOW(<y>) to FOLLOW(<x>)
# 4) If <y> → α<x><z>0<z>1<z>2...<z>k, then add FIRST(<z>0) – {ε} to FOLLOW(<x>)
# 5) If <y> → α<x><z>0<z>1<z>2...<z>i<z>i+1...<z>k and ε ∈ FIRST(<z>0) and ε ∈
# FIRST(<z>1) and ε ∈ FIRST(<z>2)and ... and ε ∈ FIRST(<z>i), then add FIRST(<z>i+1)
# – {ε} to FOLLOW(<x>)

import sys
from first import *
allfollows = {}
f = {}
def isterminal(x,dict): # check if a given character is a terminal
    #print(f"x:{x}, dict:{dict}")
    if x in dict:
        return False # not a terminal, a key
    return True # terminal

def changing(current,prev): # checks if there are still changes happening to the follow set
    if current == prev:
        return False
    return True

    return a

# does the actual change of the set of follows 
def morph(rule,result):

    if rule in result: # if our rule is contained in the right hand side of a rule,
        found = False
        br = False
        for letter in result:
            print(letter)
            if letter == rule:
                found = True
            if found:
                br = True
                # here we are following our symbol, so now we apply rules.
                #print(letter)
                fn = first(letter,cfg)
                if "@" in fn:
                    br = False
                    fn.remove("@")
                if rule not in follows:
                    f[rule] = fn
                else:
                    f[rule] += fn
            if br:
                break


def fol(cfg,firsts):
    follows = {}
    for rule in cfg.keys():
        if rule == "S": # yeah boy
            f[rule] = "$"
            continue
        for result in cfg.items():
            #print(f"{result} is a {type(result)}")
            if type(result) == list or type(result) == tuple:
                for entry in result:
                    morph(rule,entry)
                # this is where it gets fucked
            else:
                morph(rule,result)

        for result in cfg.items():
            if type(result) == list or type(result) == tuple:
                for entry in result:
                    if entry[-1] in f[rule]:
                        f[rule].add("$")
            else:
                if result[-1] in f[rule]:
                    f[rule].add("$")

    print(follows)


fname = "cfg.txt"

cfg = formatCfg(fname)
print(f"CFG:{cfg}")
firsts = getallFirsts(fname) # use firsts function to get firsts of all characters
print(f"firsts:{firsts}")

follows = {}
#z = fo(cfg,firsts)
zz = fol(cfg,firsts)
#print(f"output:{z}")
print(f)
