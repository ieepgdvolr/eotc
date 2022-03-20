n = int(input())
array = list(map(int, input().split()))
array.sort()

need, count, group = 0,0,0

for i in array:
    count += 1
    if i > need:
        need = i
    if need == count:
        group += 1
        count, need = 0,0

print(group)

# n = 2
# array = [2,3]
# group = 0