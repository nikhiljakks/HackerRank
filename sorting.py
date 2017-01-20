#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
swapCount = 0
for i in xrange(0, n-1):
    isswap = 0
    for j in xrange(1,n-i):
        if (a[j] < a[j-1]):
            isswap = 1
            swapCount += 1
            temp = a[j-1]
            a[j-1] = a[j]
            a[j] = temp
    if (isswap == 0):
            break

print "Array is sorted in %s swaps." %str(swapCount)
print "First Element:", str(a[0])
print "Last Element:", str(a[-1])