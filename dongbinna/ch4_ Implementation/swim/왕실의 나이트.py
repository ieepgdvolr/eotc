now = input()
x = ord(now[0]) % ord('a') + 1
y = int(now[1])

dir_list = [(2,1), (2,-1), (-2,-1), (-2,1), (1,2), (1,-2), (-1,-2), (-1,2)]
count = 0

for c, r in dir_list:
    nc, nr = x+c, y+r
    if (nc>=1 and nc<=8) and (nr>=1 and nr<=8) :
        count+=1
print(count)
