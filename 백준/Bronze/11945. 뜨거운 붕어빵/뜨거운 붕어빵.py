import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bread = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    bread[i] = bread[i][::-1]
    print(*bread[i], sep='')
