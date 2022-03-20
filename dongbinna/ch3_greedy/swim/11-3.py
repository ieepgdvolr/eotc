s=input()

group = 1

pivot = s[0]

for num in s:
    if pivot != num:
        group += 1
        pivot = num

answer = group // 2
print(answer)

## 다른 풀이

s = input()
count0 = 0
count1 = 0

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))