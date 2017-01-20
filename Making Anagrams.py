def number_needed(a, b):
    totCount = 0
    bLoop = "".join(set(b))
    aLoop = "".join(set(a))
    for bchar in bLoop:
        delCount = 0
        if a.count(bchar) == 0:
            delCount = b.count(bchar)
            totCount += delCount
        elif a.count(bchar) != b.count(bchar):
            delCount = abs(a.count(bchar) - b.count(bchar))
            totCount += delCount
    for achar in aLoop:
        delCount = 0
        if achar not in bLoop:
            if b.count(achar) == 0:
                delCount = a.count(achar)
                totCount += delCount
            elif a.count(achar) != b.count(achar):
                delCount = abs(a.count(achar) - b.count(achar))
                totCount += delCount
    return totCount        
    #pass

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
