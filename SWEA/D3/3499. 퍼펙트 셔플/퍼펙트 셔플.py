T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(input().split())
    idx = n // 2 if n % 2 == 0 else n // 2 + 1
    cards1 = cards[0 : idx]
    cards2 = cards[idx : ]
    ans = []

    for i in range(idx):
        try:
            ans.append(cards1[i])
            ans.append(cards2[i])
        except:
            pass
    
    print(f'#{test_case} {" ".join(map(str, ans))}')