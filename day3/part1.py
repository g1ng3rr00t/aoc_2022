#!/usr/bin/env python3

alphabet = list(range(97,123))+list(range(65,91))
total = 0

with open('input','r') as data:
    for line in data:
        line = line.strip()
        a,b = line[:int(len(line)/2)], line[int(len(line)/2):]
        for i in alphabet:
            if chr(i) in a and chr(i) in b:
                #print(chr(i))
                total += (alphabet.index(i) + 1)

print(total)
