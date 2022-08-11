from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    picture[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1:
                picture[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    
    return cnt

n, m = map(int,input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

num_list = []
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            num_list.append(bfs(i,j))

if len(num_list) == 0:
    print(len(num_list))
    print(0)
else:
    print(len(num_list))
    print(max(num_list))