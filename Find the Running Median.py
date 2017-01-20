# Enter your code here. Read input from STDIN. Print output to STDOUT
import bisect
count = int(raw_input())
ordLst = []
ordLstMed = 0
def getMedian(ordLst):
    if (len(ordLst)%2 == 0 ):
        return (ordLst[len(ordLst)/2] + ordLst[(len(ordLst)/2) - 1])/2.0
    else:
        return ordLst[int(len(ordLst)/2)]
for i in xrange(count):
    if (len(ordLst) == 0 ):
        ordLst.append(int(raw_input()))
        ordLstMed = ordLst[0]
    else:
        newVal = int(raw_input())
        bisect.insort_right(ordLst, newVal )
    print getMedian(ordLst)

