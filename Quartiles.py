# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math
count = input()
list1 = list( map (int, (input()).split(" ")))
list1.sort()
median2 = statistics.median(list1)

if (len(list1)%2 == 0):
    list2 = list1[:(int (len(list1)/2))]
    list3 = list1[(int (len(list1)/2)) :]
    median1 = statistics.median(list2)
    median3 = statistics.median(list3)
else:
    list2 = list1[:math.floor(len(list1)/2)]
    list3 = list1[math.ceil(len(list1)/2):]
    median1 = statistics.median(list2)
    median3 = statistics.median(list3)
print (int (median1))
print (int (median2))
print (int (median3))             
