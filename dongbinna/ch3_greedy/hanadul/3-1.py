# 돈
n = int(input())
# 잔돈
changes =  [500,100,50,10]
count = 0

for coin in changes :
    # 갯수
    count += n//coin
    # 남은돈
    n = n%coin
    
print(count)

 
