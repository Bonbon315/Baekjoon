import sys
input = sys.stdin.readline


T = int(input())

for i in range(T):
    p = list(input())
    cnt = 0
    for k in p:
        if k == '(':
            cnt += 1
        if k == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')