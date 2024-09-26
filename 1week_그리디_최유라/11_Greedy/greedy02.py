# 221013
# 02 ) 곱하기 혹은 더하기
from timeit import default_timer as timer
from datetime import timedelta

start = timer() # 코드시작

sum = 0
for i in range(10000000):
    sum += i

#####
s = '30045' # 문자열 s
print(list(s)) # 문자열 리스트로 하나씩 담기

result = 0
for i in range(len(list(s))):
    a = int(list(s)[i]) # String to int
    if(a == 0 or result == 0): # 문자가 0 이거나 총합이 0 일 때는 더하기
        result += a
    else: # 그 외에는 곱하기
        result *= a

print(result)
#####

end = timer() # 코드끝

print("걸린 시간: ", end - start)  # seconds
