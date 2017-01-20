#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    stack = []
    opens = ['[', '{', '(']
    closes = [']', '}', ')']
    dict1 = {a:b for a,b in zip(opens, closes)}
    result = 'YES'
    for i in s:
        if (i in opens):
            stack.append(i)
            latest = i
        elif (i in closes):
            if (not stack or dict1[stack[-1]] != i):
                result = 'NO'
            else:
                stack.pop()
    if (stack):
        result = 'NO'
    print (result)
                
            