#!/usr/bin/env python3

with open('input','r') as data:
    daters = data.read().strip()

for i in range(4,len(daters)):
    try:
        buffer =[]
        for x in range(4):
            if daters[i-x] not in buffer:
                buffer.append(daters[i-x])
            else:
                break
        if len(buffer) == 4:
            print(buffer)
            print(i)
            break
        else:
            buffer=[]
    except:
        pass
