data=input()

temp = data[0]
zero= 0
one = 0
for i in range(1,len(data)):
    if temp == data[i] :
        temp = data[i]
    else :
        if temp == '0':
            zero +=1
        else :
            one += 1
        temp = data[i]

print(min(zero,one))