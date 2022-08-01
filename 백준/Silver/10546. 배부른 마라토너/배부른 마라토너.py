import sys
input = sys.stdin.readline

N = int(input())
runners = dict()
for i in range(N):
    runner = input().rstrip()
    if runner in runners:
        runners[runner] += 1
    else:
        runners[runner] = 1

for i in range(N-1):
    runner = input().rstrip()
    runners[runner] -= 1

for i in runners:
    if runners[i] > 0:
        print(i)
        break