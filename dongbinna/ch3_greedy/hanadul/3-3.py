m,n = map(int,input().split())
answer = 0
for i in range(m):
    temp = list(map(int,input().split()))
    answer = max(answer, min(temp))
   
print(answer)    