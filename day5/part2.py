#!/usr/bin/env python3

main = []
indices = [1,5,9,13,17,21,25,29,33]
#indices = [1,5,9]
#for i in range(3):
for i in range(9):
    main.append([])

with open('input','r') as data:
    for line in data:
        if 'move' not in line and len(line) > 4:
            for i in indices:
                if line[i].isalnum() == True:
                    main[indices.index(i)].append(line[i])
                else:
                    pass
for i in main:
    i.reverse()

#print(i)


with open('input','r') as data:
    for line in data:
        if 'move' in line:
            commands = line.strip().split(' ')
            amount = int(commands[1])
            start = int(commands[3]) -1
            end = int(commands[5]) - 1
            boxen = []

            for i in range(amount):
#               main[end].append(main[start].pop())
                boxen.append(main[start].pop())
            boxen.reverse()
            main[end].extend(boxen)

for i in main:
    print(i)
