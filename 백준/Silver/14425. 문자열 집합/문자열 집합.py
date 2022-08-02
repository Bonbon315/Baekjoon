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
for k in words:
    if k in set(S):
        cnt += 1
print(cnt)