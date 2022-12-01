#!/usr/bin/env python3

## Lets do this smarter than part 1 and actually use some sort of data structure instead of being a goblin

calories = []
current_score = 0

with open('input','r') as frog:
    for line in frog:
        if line != "\n":
            current_score += int(line.strip())
        else:
            calories.append(current_score)
            current_score = 0
calories.sort(reverse=True)
## print(calories)

print(calories[0]+calories[1]+calories[2])
