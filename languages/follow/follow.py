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

#Create a program that will accept an arbitrary CFG as input and that will output FOLLOW sets for all non-terminals in the grammar.
#The program should read from an input file and output to the console (screen). Submit a zip file that includes your program and input files.



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
def isterminal(x,dict): # check if a given character is a terminal
    print(f"x:{x}, dict:{dict}")
    if x in dict:
        return False # not a terminal, a key
    return True # terminal

def changing(current,prev): # checks if there are still changes happening to the follow set
    if current == prev:
        return False
    return True

def gfollow(cfg,firsts):
    all = {}
    all[list(cfg.keys())[0]] = "$" # rule 01
    for k in cfg.keys():
        if not isterminal(cfg[k][:-1],cfg): # rule 02
            all[cfg[k][:-1]] = all[k]
        else: # rule 03 maybe : ) ?
            if "@" in firsts[cfg[k][:-1]]:
                t = firsts[cfg[k][:-1]]
                t.remove("@")
                all[cfg[k][:-2]] = t + all[k]
            else:
                all[cfg[k][:-2]] = firsts[cfg[k][:-1]]


def follow(key,cfg,firsts):
    # apply follow rules to cfg
    f = []
    # if key is the first symbol, add $ to it's follow
    # 1 I don't know how to check this... Ill hard code it LOL

    if key == "S" or key == "s":
        f.append("$") #EOL
        allfollows[key]  = allfollows[key] + ["$"]
    # 2 if a rule ends in a nonterminal <x> add the follow(rule) to follow(x)
    if not isterminal(cfg[key][:-1],cfg): # this doesn't work actually
        f = follow(cfg[key][:-1],cfg,firsts)

    for rule in cfg[key]:
        if not isterminal(rule[:-1]):
            allfollows[rule[:-1]] += allfollows[key]

    # 3 if in a rule, everything after <x> can go to epsilon, add follow(rule) to follow(x)
    if isterminal(cfg[key][:-1],cfg):
        for char in reversed(cfg[key]):
            print("x")
    return -1

    # 4 if y -> <x>z then add first(<x>z)-@ to follow(?)

    # 5 if in the above case, <x>z has epsilon, continue, adding new ones on there ? idk this one

# 1) FOLLOW(S) = { $ }   // where S is the starting Non-Terminal
#
# 2) If A -> pBq is a production, where p, B and q are any grammar symbols,
#    then everything in FIRST(q)  except Є is in FOLLOW(B).
#
# 3) If A->pB is a production, then everything in FOLLOW(A) is in FOLLOW(B).
#
# 4) If A->pBq is a production and FIRST(q) contains Є,
#    then FOLLOW(B) contains { FIRST(q) – Є } U FOLLOW(A)

# https://www.gatevidyalay.com/first-and-follow-compiler-design/
# this seems to have a good ruleset explaination ?

fname = "cfg.txt"

cfg = formatCfg(fname)
print(f"CFG:{cfg}")
firsts = getallFirsts(fname) # use firsts function to get firsts of all characters
print(f"firsts:{firsts}")

follows = {}
for key in cfg:
    follows[key] = gfollow(cfg,firsts)
    print(f"Follow of {key} is {gfollow(cfg,firsts)}") # get the first of each key in the dict

#return follows # neat
