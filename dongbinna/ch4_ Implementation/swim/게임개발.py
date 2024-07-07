N, M = map(int, input().split())
dx, dy, d = map(int, input().split())

game_map = []

for _ in range(N):
    game_map.append(list(map(int, input().split())))


d = [3,2,1,0]
l = [2,1,0,3]

nx = [0,1,0,-1]
ny = [-1,0,1,0]

visited = []
visited.append((dx, dy))

while True:
    # change direction 
    for nd, nl in zip(d,l):
        if (dx+nx[nl], dy+ny[nl]) not in visited:
            if game_map[dx+nx[nl]][dy+ny[nl]] != 1:
                dx = dx+nx[nl]
                dy = dy+ny[nl]
                d = nd
                visited.append((dx,dy))
        else:
            continue
            
    if game_map[dx-nx[d]][dy-ny[d]] != 1 and (dx-nx[d], dy-ny[d]) not in visited:
        dx = dx-nx[nl]
        dy = dy-ny[nl]
        visited.append((dx, dy))
    else:
        break

print(len(visited))
