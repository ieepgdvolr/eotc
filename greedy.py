# 221011
# 예제 3-1 거스름돈
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 코드실행 시간 측정
from timeit import default_timer as timer
from datetime import timedelta

start = timer() # 코드시작

sum = 0
for i in range(10000000):
    sum += i


# 실전문제 1 ) 큰 수의 법칙
# 문제 이해도 못하겠네ㅎㅎㅎ

# 내가 푼 답안
nmk = [5, 8, 3] # N, M, K
data = [2, 4, 5, 4, 6] # 데이터

data.sort(reverse=True) # 데이터 정렬(큰수부터)
# print(data[0], data[1])

sumData = 0 # 더해진 답
for i in range(nmk[1]): # M만큼 for문 돌리기
    if((i+1) % (nmk[2]+1) != 0): # K만큼 제일 큰 수 더하기
        sumData += data[0]
    else: # 2번째 큰 수 더하기
        sumData += data[1]

print(sumData)

end = timer() # 코드끝

print("걸린 시간: ", end - start)  # seconds


# 책 해설
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

# while True:
#     for i in range(k): # 가장 큰 수를 k번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0: # m이 0이라면 반복문 탈출
#         break
#     result += second # 두 번째로 큰 수를 한 번 더하기
#     m -= 1 # 더할 때마다 1씩 빼기

# print(result)

# 책 해설(좀 더 간편하게)
# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력


# 221012
# 실전문제 2 ) 숫자 카드 게임

# 내가 푼 답안
import numpy as np # numpy 설치
n = 3 # 행의 개수
m = 4 # 열의 개수
arr = [[7, 5, 7, 8], [3, 3, 3, 4], [4, 4, 6, 9]] # data
arr = np.sort(arr, axis=1) # 행 기준으로 정렬
print(arr)
result = 0
for i in range(n):
    if(arr[i][0] > result): # 이전 숫자랑 비교
        result = arr[i][0] # 큰 수 담아주기
print(result) # 최종 출력

# 책 해설
# min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

#2중 반복문 구조를 이용하는 답안 예시
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력



# 실전문제 3 ) 1이 될 때까지

# 내가 푼 답안
n = 25
k = 3
result = 0
while n != 1:
    if(n % k == 0):
        n = n / k
    else:
        n = n - 1
    result += 1
print(result)

# 책 해설
# 단순하게 푸는 답안 예시
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

# 답안 예시
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
