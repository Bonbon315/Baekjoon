import sys
input = sys.stdin.readline
n = int(input())
ans = 0

for i in range(n, 1, -1):
    save = True
    for j in str(i):
        if j != '4' and j != '7':
            save = False
            break
    if save:
        ans = i
        break

print(ans)