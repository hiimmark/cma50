# Mark Ma
# Ghidorah 
# SoftDev
# K05 -- Read from file, populate dictionary, select random person
# 2024-09-16
# time spent: 0.2 

from random import randint

data = open("krewes.txt", "r").readline().strip()
l = data.split("@@@")[:-1]
krewes = {}
friends = {}
krewes[4] = []
krewes[5] = []
for y in l:
    x = y.split("$$$")
    krewes[int(x[0])].append([x[1], x[2]])

rand_period = randint(4, 5)
rand_index = randint(0, len(krewes[rand_period]) - 1)
rand_item = krewes[rand_period][rand_index]
person = rand_item[0]
pet = rand_item[1]
print(f'period: {rand_period}, person: {person}, pet: {pet}')
