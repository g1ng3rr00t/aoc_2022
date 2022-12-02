#!/usr/bin/env python3

### Rock = X = A = 1
### Paper = Y = B = 2
### Scissors = Z = C = 3

win_conditions = [['B','Z'],['C','X'],['A','Y']]
draw_conditions = [['A','X'],['B','Y'],['C','Z']]
plays = []
score = 0

with open('input','r') as data:
    for line in data:
        plays.append(line.strip())


for i in plays:
    round_score = 0
    round = i.split()
    match round[1]:
        case 'X':
            round_score += 1
        case 'Y':
            round_score += 2
        case 'Z':
            round_score += 3
    if round in win_conditions:
        round_score += 6
    if round in draw_conditions:
        round_score += 3
    score += round_score

print(score)
