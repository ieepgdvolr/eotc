score = input()

n = len(score) // 2
left = score[:n]
right = score[n:]

l,r = 0,0

for i in range(n):
    l += int(left[i])
    r += int(right[i])
    
if l == r:
    print('LUCKY')
else:
    print('READY')
