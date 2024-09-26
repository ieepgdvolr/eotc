# 221013
# 01) 모험가 길드
from timeit import default_timer as timer
from datetime import timedelta

start = timer() # 코드시작

sum = 0
for i in range(10000000):
    sum += i

#####
n = 5 # N명의 모험가
data = [2, 3, 1, 2, 2] # 공포도 X data
data.sort(reverse=True) # 공포도가 높은 순으로 정렬

result = 0 # 그룹 수

while n != 0: # 그룹이 없는 모험가가 없을 때까지 while 문 돌리기
    if n < 1 :
        break
    print(data[0])
    n -= data[0] # 가장 큰 수만큼 그룹 묶기
    for i in range(data[0]): # 그룹이 만들어지는 인원
        del data[0] # 그룹이 만들어진 인원은 리스트에서 제거
        print(data)
    result += 1 # 그룹 수 추가

print(result)
#####

end = timer() # 코드끝

print("걸린 시간: ", end - start)  # seconds


# 책 해설
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)