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

