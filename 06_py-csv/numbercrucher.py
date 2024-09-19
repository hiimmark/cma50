# Mark Ma
# Ghidorah 
# SoftDev
# K06 -- Read from csv, populate dictionary, select random occupation with given percentage chance
# 2024-09-20
# time spent: 0.3 

import random

f = open("occupations.csv", "r").read()
f = f.split("\n")[1:-1]
total = float(f[-1].split(',')[-1]) # the total percentage of the whole thing
f = f[0:-1] # get rid of the last column with the total

occupations = {} # {occupation: percentage}
for x in f:
    y = x.split(',')
    occupations[(",".join(y[:-1])).replace('"','')] = float(y[-1])

def select_random():
    perc = random.uniform(0, total)
    for key, values in occupations.items():
        if perc - values <= 0:
            return key
        perc -= values
    return null

'''
## tester
mp = {}
for i in range(1000):
    chosen = select_random()
    if chosen not in mp:
        mp[chosen] = 0
    mp[chosen] += 1

print(mp)
'''

print(select_random())

