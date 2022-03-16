N, M = map(int, input().split())
answer = 0

for i in range(N):
    arrays = list(map(int, input().split()))
    answer = max(answer, min(arrays))

    if answer == 10000 :
        break

print(answer)
