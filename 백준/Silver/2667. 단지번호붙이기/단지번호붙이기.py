import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 0 
    global cnt
    cnt += 1
    for i in range(4): 
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx,ny)


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
ans = 0
anslist = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            anslist.append(cnt)
            ans += 1
anslist.sort()
print(ans)
for i in range(ans):
    print(anslist[i])