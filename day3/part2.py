#!/usr/bin/env python3

alphabet = list(range(97,123))+list(range(65,91))

counter = 0
grouped_lines=[]


with open('input','r') as data:
    blob = []
    for line in data:
        blob.append(line.strip())

    for i in range(0, (len(blob) -2), 3):
        grouped_lines.append(blob[i:i+3])

counter = 0

for i in grouped_lines:
    for x in alphabet:
        if chr(x) in i[0] and chr(x) in i[1] and chr(x) in i[2]:
            counter += (alphabet.index(x)+1)

print(counter)
