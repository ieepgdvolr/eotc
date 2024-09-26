
# 코드실행 시간 측정
from timeit import default_timer as timer
from datetime import timedelta

start = timer() # 코드시작

sum = 0
for i in range(10000000):
    sum += i


# 코드


end = timer() # 코드끝

print("걸린 시간: ", end - start)  # seconds