#!/usr/bin/env python3

## Rock = A = 1
## Paper = B = 2
## Scissors = C = 3

## X = lose = 0
## Y = draw = 3
## Z = win = 6
score = 0
plays = []
lose_conditions = {'A':3,'B':1,'C':2}
draw_conditions = {'A':1,'B':2,'C':3}
win_conditions = {'A':2,'B':3,'C':1}

with open('input','r') as data:
    for line in data:
        plays.append(line.strip())

for i in plays:
    round_score = 0
    round = i.split()
    match round[1]:
        case 'X':
            round_score += lose_conditions[round[0]]
        case 'Y':
            round_score += 3
            round_score += draw_conditions[round[0]]
        case 'Z':
            round_score += 6
            round_score += win_conditions[round[0]]
    score += round_score
print(score)
