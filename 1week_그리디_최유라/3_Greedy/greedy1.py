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


