str = input()
data = []

for _ in range(len(str)):
    data.append(int(str[_]))

answer = data.pop(0)

for i in data :
    if i <= 1 or answer <= 1:
        answer += i
    else :
        answer *= i
        
print(answer)