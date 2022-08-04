import sys
input = sys.stdin.readline

fullpiece = [1, 1, 2, 2, 2, 8]
curpiece = list(map(int, input().split()))

for i in range(6):
    print(fullpiece[i] - curpiece[i], end=' ')