array = list(map(int, input().split()))

answer = 0

if array[0] != 0:
    answer = 1

for i in array:
    if i == 0 or answer == 0:
        answer += i
    else:
        answer *= i

print(answer)