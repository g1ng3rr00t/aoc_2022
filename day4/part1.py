#!/usr/bin/env python3

assignment_pairs =[]

with open('input','r') as data:
    for line in data:
        assignment_pairs.append(line.strip().split(','))

counter = 0

for i in assignment_pairs:
    first = i[0].split('-')
    second = i[1].split('-')
    
    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        counter +=1
    elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        counter += 1

print(counter)

