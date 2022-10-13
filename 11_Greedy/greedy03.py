# 221013
# 03) 문자열 뒤집기
from timeit import default_timer as timer
from datetime import timedelta

start = timer() # 코드시작

sum = 0
for i in range(10000000):
    sum += i

#####
result = 0
print(result)
#####

end = timer() # 코드끝

print("걸린 시간: ", end - start)  # seconds