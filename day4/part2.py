#!/usr/bin/env python3

assignment_pairs =[]

with open('input','r') as data:
    for line in data:
        assignment_pairs.append(line.strip().split(','))

counter = 0

for i in assignment_pairs:
    first = i[0].split('-')
    second = i[1].split('-')
    
    for x in range(int(first[0]),int(first[1])+1):
        if x in range(int(second[0]),int(second[1])+1):
            counter += 1
            break

print(counter)

