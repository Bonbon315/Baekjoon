import sys
input = sys.stdin.readline

while True:
    sent = input().rstrip()
    cnt = 0
    if sent == '#':
        break
    for i in sent:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)