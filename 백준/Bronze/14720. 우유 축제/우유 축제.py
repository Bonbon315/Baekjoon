import sys
input = sys.stdin.readline

N = int(input())
stores = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if stores[i] == cnt % 3:
        cnt += 1
print(cnt)