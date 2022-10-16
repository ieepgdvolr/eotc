# 221014~16
# 05) 볼링공 고르기
n = 6
m = 3
data = [1, 3, 2, 3, 2, 3]

from itertools import *
result = list(combinations(data, 2)) # 중복 없이 2개씩 묶는 조합 생성(인덱스가 다른 건 다른 값으로 침)
print(result) # 조합 생성 후 데이터 확인
for i in range(m): # (0,0), (1,1) 등 제거하기 위해 for문
#    (i+1, i+1) in result
    while ((i+1, i+1) in result) == True: # 값이 있을 경우 제거
        result.remove((i+1, i+1)) # 값 제거

print(result) # 최종 데이터