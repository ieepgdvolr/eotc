# 221021
# 07 ) 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

# data = int(input()) # 데이터 받아오기
data = 1234
n = list(map(int,str(data))) # 리스트로 숫자 하나씩 담기
x, y = 0, 0 # 앞자리, 뒷자리 합 담을 변수
for i in range(len(n)):
    if i < len(n)/2:
        x += n[i]
    else:
        y += n[i]

if x == y: # 앞, 뒤 합이 같을 경우 LUCKY
    print('LUCKY')
else: # 아닐 경우 READY
    print('READY')

# 책 해설
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")