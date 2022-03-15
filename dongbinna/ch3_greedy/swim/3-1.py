N = int(input())
coins = [500, 100, 50, 10]
k = 0
count = 0

while N > 0 and k < len(coins):
    count += N // coins[k]
    N %= coins[k]
    k += 1

print(count)