from posixpath import split


#배열크기n, 더할횟수m, 연속할k
n,m,k = map(int,input().split())
numbers = list(map(int, input().split()))

numbers.sort() # asc
first = numbers[n-1]
second = numbers[n-2]
answer = 0

# while m > 0:
#     for i in range(k):
#         answer += first #k번까지
#         m -= 1
#     if m > 0 :
#         answer += second
#         m -= 1
# print(answer)

# ---

count = m//(k+1)*k + m%(k+1)
answer += first * count
answer += second * (m-count)

print(answer)




