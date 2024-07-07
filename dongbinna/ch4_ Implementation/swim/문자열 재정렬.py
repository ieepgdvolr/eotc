s = input()
new_s = []
nums = 0
answer = ''
for i in s:
    if i >= 'A' and i <= 'Z':
        new_s.append(i)
    else:
        nums += int(i)
        
new_s.sort()
# 숫자가 하나도 없을 경우도 생각해야한다
# 그러므로

if nums != 0:
    answer = ''.join(new_s) + str(nums)
print(answer)
