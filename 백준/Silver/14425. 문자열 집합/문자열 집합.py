import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = []
words = []
for i in range(N):
    S.append(input().rstrip())
for i in range(M):
    words.append(input().rstrip())
cnt = 0
S = set(S)
for k in words:
    if k in S:
        cnt += 1
print(cnt)