T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    avg_income = sum(income) / N

    cnt = 0
    for i in income:
        if i <= avg_income:
            cnt += 1
    print(f'#{test_case} {cnt}')
