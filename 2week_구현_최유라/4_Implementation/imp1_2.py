# 221021
# 예제 4-2 시각
# for문으로 시(0-23)>분(0-59)>초(0-59) 돌려서 풀어보려고 함.
n = 6
count = 0 # 3의 개수
for i in range(n+1): #시
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k): # 3이 있을 경우
                count += 1 # count 수 증가

print(count)

# 책 해설
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)