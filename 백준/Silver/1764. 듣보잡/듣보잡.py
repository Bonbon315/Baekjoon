import sys
input = sys.stdin.readline

N, M = map(int, input().split())
notheard = []
notseen = []

for i in range(N):
    notheard.append(input().rstrip())
for i in range(M):
    notseen.append(input().rstrip())

notheardseen = sorted(list(set(notheard) & set(notseen)))
print(len(notheardseen))
for i in notheardseen:
    print(i)