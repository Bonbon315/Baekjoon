import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for case in range(K):
    i, j, x, y = map(int, input().split())
    ans = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            ans += matrix[a][b]
    print(ans)