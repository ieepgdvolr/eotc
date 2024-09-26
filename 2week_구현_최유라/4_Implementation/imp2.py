# 221021
# 실전문제2 왕실의 나이트
# 예제랑 비슷하게 x,y축 생각하면 될 거 같은데 살짝 까다롭네?
# x축 a,b,c,d,e,f,g,h
# y축 1,2,3,4,5,6,7,8
# 처음엔 무조건 2칸 이동. 그리고 1칸 이동
# 이동할 수 있는 경우의 수는 최소 2 최대 8
# >> (2,1), (2,-1), (1,2), (-1,2), (-2, 1), (-2, -1), (-1, -2), (1, -2)
# 예제 c2 = (3,2)

count = 0
c2 = (3,2)
data = [(2,1), (2,-1), (1,2), (-1,2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
for i in range(len(data)):
    # 8번 돌려서 해당하면 count 증가? 하려다가 data 정의 후 연산하는 거로 품
    x , y = 0, 0
    x = data[i][0] + c2[0]
    y = data[i][1] + c2[1]
    #print(x, y)
    if x > 0 and y > 0: # 8x8 안에 들어왔을 경우 count 증가
        count += 1
print(count)

# 책 해설 보고 깨달았다...! 아스키 코드! ord('x') 변환!
# 나는 애초에 데이터값을 내가 임의로 c2 = (3,2) 이런 식으로 넣어서 변환 생각도 안했다ㅋㅋ
# 게다가 예제 4-1 에서 푼 거처럼 x, y좌표 각각 풀었는데 책 해설은 비슷한듯 다르게 풀었다.

# 책 해설
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)