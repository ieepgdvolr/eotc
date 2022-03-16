N, K = map(int, input().split())

count = 0

while N > 1:

    if N % K == 0:
        N = N // K
    else:
        N -= 1

    count += 1

print(count)

# N <= 100000 이므로 이 문제에서는 효율성을 통과하지만
# 범위가 1억이 넘고, N이 K로 나누어 떨어지는 숫자가 아니라면
# -> K로 나눠 떨어지는 숫자가 되도록 한번에 계산하는 것이 좋다

n, k = map(int, input().split())

answer = 0

while True:
    if n >= k:
        remainder = n % k
        n -= remainder
        answer += remainder

        n //= k
        answer += 1

    else :
        break

if n > 1 :
    answer += (n-1)

print(answer)



