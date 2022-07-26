P, K = map(int, input().split())
cnt = 1
for i in range(K, P+1):
    if i == P:
        print(cnt)
    cnt += 1
