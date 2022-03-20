
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, map(input().split())))
    min_value = 100001
    for d in data:
        min_value = min(min_value, d)

    result = max(min_value, result)


