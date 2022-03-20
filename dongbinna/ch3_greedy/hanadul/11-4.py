n=int(input())
coin = list(map(int,input().split()))
coin.sort()
sum = 1

# total = 0
# for _ in coin:
#     total += _

for i in coin:
    # if min(coin) != 0:
    #     break       ------ 비교의 맨 처음이 결국 1이라서 필요없는..
    if sum < i:
        break
    else:
        sum += i
print(sum)    