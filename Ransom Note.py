
from collections import defaultdict

def ransom_note(magazine, ransom):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word]+=1
    for word in ransom: 
        if dicty[word]==0 : return 'No' 
        dicty[word]-=1
    return 'Yes'

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
print answer    
