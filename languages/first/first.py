# Ethan Smith
# programming langauges
# First function
import sys

# Rules for the cfg file formatting
# no spaces allowed
# `->` separates rules and what they go do ( standard)
# @ == epsilon
# `|` == a new rule
# # is used as a comment, so it can't be used except as a terminal



def isterminal(x,dict): # check if a given character is a terminal
    if x in dict:
        return False # not a terminal, a key
    return True

def first(x,cfg):
    if x not in cfg:
        return x;
    output = []
    str = cfg[x]
    for z in str:
        if isterminal(z[0],cfg): # z[0] is terminal, adding to output
            output += z[0]
        if z[0] == "@" and len(z) ==1: # z[0] is epsilon, adding
            output += "@" # add this
        if isterminal(z[0],cfg) == False:
            for t in z:
                if t != x:# don;t infinitely recurse on self 
                    output += first(t,cfg)

    return set(output)
with open("cfg.txt") as f: # I am good at file and variable names... they are always aweful :)
#with open(sys.argv[1]) as f: # testing line
    # lol
    cfg = {}
    print("Provided grammer:\n")
    for line in f.readlines():
        print(line.strip())
        if line[0] == "#": # skip lines starting in # so that I can add comments to the files to describe what the rules are
            continue
        else:
            a =line.strip().split("->")
            #print(a)
            r = a[1].split("|") # split up multiple rules
            cfg[a[0]] = r
print("\nFirsts:\n")
for key in cfg:
    print(f"First of {key} is {first(key,cfg)}") # get the first of each key in the dict
