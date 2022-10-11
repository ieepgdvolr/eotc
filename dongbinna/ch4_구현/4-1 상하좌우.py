N = int(input())
plans = input().split()

r, c = 1,1

for p in plans:
    nr, nc = r, c
    if p == 'L':
        nc -= 1
    elif p == 'R':
        nc += 1
    elif p == 'U':
        nr -= 1
    elif p == 'D':
        nr += 1
    else:
        continue
    
    # 범위 내인지 체크 => 범위 
    if 1 <= nr <= N and 1 <= nc <= N:
        r, c = nr, nc
        
print(r, c)
