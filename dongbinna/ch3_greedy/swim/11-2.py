array = list(map(int, input().split()))

answer = 0

if array[0] != 0:
    answer = 1

for i in array:
    if i <= 1 or answer == 0: #1일때 더하는 것이 더 큰 숫자
        answer += i
    else:
        answer *= i

print(answer)