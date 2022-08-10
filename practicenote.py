import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(5000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1] #상하좌우 오위/오아래/왼위/왼아래
dy = [0, 0, -1, 1, 1, 1, -1, -1]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(8): #델타탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx,ny) 


while True:
    w, h = map(int, input().split()) # w = y / h = x
    if w == 0 and h == 0:
        break
    
    island = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)