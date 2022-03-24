n = int(input())

array = list(map(int, input().split()))
array.sort()

answer = 1

for i in array:
    if answer < i :
        break
    answer += i

print(answer)