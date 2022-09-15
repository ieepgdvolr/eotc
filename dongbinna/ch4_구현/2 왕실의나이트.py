now = input()
r = int(now[1])
c = ord(now[0]) - 96

steps = [(1, -2), (-1, -2), (1, 2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

count = 0

for step in steps:
    nr = r + step[0]
    nc = c + step[1]
    if 1 <= nr <= 8 and 1<= nc <= 8:
        count += 1

print(count)

