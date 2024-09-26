# 221021 & 221023
# 08 ) 문자열 재정렬
# chr A-Z(65-90) 0-9(48-57)
data = 'AJKDLSI412K4JSJ9D'
# my_list = list(data)
# print(my_list)

number = 0
result = []
# list.sort()
# print(list)

# for i in range(len(list)):
#     list2 = int(ord(list[i]))
#     if list2 < 65:
#         number += int(list[i])
#         list.remove(list[i])
# >> 처음엔 이렇게 문자/숫자 구분해서 list에서 문자 제거하는 방식으로 해봄
# 결국 이 방법으로는 결과도출 못해냄

# 빼는 거 말고 list에 새로 더하는 방법(append)으로 방식 바꿈
for i in data:
    # print(ord(i))
    if ord(i) < 65:
        number += int(i)
    else:
        result.append(i)
# print(number)
# print(result)

result.sort()
# print(result)
result.append(number)
# print(result)
# 확인한다고 무수히 찍어댄 print ㅋㅋㅋㅋㅋㅋ

# print(' '.join(str(s) for s in result)) # A B C K K 13
# 처음에 ^ 이렇게 찍으니까 띄어쓰기가 나오더라. 그래서 ' ' 에서 ''로 바꿈 *join은 리스트를 문자열로 바꿔주는 거
print(''.join(str(s) for s in result)) # ABCKK13 최종출력


# 책 해설
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))