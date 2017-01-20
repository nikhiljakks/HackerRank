def array_left_rotation(a, n, k):
 b= []
 for i in xrange(0, n) :
    rIndex = (i+k)%(n)
    #b[i] = a[rIndex]
    b.append(a[rIndex])
 return b

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
