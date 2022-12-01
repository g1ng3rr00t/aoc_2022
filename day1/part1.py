#!/usr/bin/env python3

# Some info we might need

high_score = 0

number_of_elves = 0

current_score = 0

with open('input','r') as frog:
    for line in frog:
        ## Not newline
        if line != "\n":
            current_score += int(line.strip())
        ## Newline
        else:
            ## print("newline")
            ## Compare current score to high score, replace high score if larger
            if current_score > high_score:
                high_score = current_score
                current_score = 0
            ## reset current_score, continue
            else:
                current_score = 0
print(high_score)
