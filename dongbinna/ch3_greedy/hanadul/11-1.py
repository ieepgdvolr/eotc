import sys

input = sys.stdin.readline

#사람
n = int(input())
x = list(map(int,input().split()))

x.sort()

group = 0
count = 0

for i in x:
    group += 1
    if group >= i:
        count += 1
        group = 0

print(count)     
