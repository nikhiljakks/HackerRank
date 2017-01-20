import sys


n = int(raw_input().strip())
a = []
diag1 = 0
diag2 = 0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
for i in xrange(n):
     diag1 += (a[i])[i]
     diag2 += (a[i])[n-i-1]
print abs(diag1-diag2)