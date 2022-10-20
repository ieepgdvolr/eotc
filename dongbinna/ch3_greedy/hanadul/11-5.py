#볼링공 고르기
n,m = map(int,input().split())
data = list(map(int,input().split()))

ball=[]

for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        if data[i] != data[j]:
            ball.append([data[i],data[j]])

print(len(ball))