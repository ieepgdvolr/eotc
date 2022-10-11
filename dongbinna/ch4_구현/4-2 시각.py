N = int(input())

if 0 <= N <= 23 :    
    count = 0
    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                string = str(h)+str(m)+str(s)
                if "3" in string:
                    count += 1
print(count)
