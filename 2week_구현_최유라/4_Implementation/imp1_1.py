# 221020
# 예제 4-1 상하좌우
# L R U D 만나는 대로 data[0] or data[1] 의 숫자 증감
# L = [0, -1]
# R = [0, 1]
# U = [-1, 0]
# D = [1, 0]
n = 5 # N x N 사각형 공간
x, y = 1, 1 # 시작지점 1,1 고정 (x,y 좌표로 설정)
data = ['L', 'R', 'R', 'U', 'R', 'R', 'R', 'U', 'D', 'D']

for i in data:
    if i == 'L': # L일 경우
        if y > 1: # 1보다 큰 경우에만 -1 할 수 있다
            y -= 1
    elif i == 'R': # R일 경우
        if y < n: # n보다 작은 경우에만 +1 할 수 있다
            y += 1
    elif i == 'U': # U일 경우
        if x > 1:
            x -= 1
    elif i == 'D': # D일 경우
        if x < n:
            x += 1

print(x, y) # 최종 좌표

# 책 해설
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)