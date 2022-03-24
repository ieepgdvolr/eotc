n, m = map(int, input().split())

array = map(int, input().split())

weight = [0] * (m+1)
answer = 0

for i in array:
    weight[i] += 1

for i in range(m+1):
    for j in range(i+1, m+1):
        answer += weight[i] * weight[j]

print(answer)