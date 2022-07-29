T = int(input())

for test_case in range(T):
    number = int(input())
    score = list(map(int, input().split()))
    cnt = [0] * 101
    
    for i in score:
        cnt[i] += 1
    
    most = 0
    ans = 0

    for k in range(1, len(cnt)):
        if ans <= cnt[k]:
            ans = cnt[k]
            most = k
    
    print(f'#{number} {most}')