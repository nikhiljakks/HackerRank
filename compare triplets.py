import sys


a0,a1,a2 = raw_input().strip().split(' ')
list1 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
list2 = [int(b0),int(b1),int(b2)]

a= 0
b= 0

for i in xrange (0,3):
    if (list1[i] > list2[i]):
        a += 1
    elif (list1[i] < list2[i]):
        b += 1

print "%s %s" % (a, b)
