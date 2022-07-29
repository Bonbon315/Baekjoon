T = int(input())

for test_case in range(1, T+1):
    rect = list(map(int, input().split()))
    rect.sort()
    ans = 0

    if rect[0] != rect[1]:
        ans = rect[0]
    else:
        ans = rect[2]
    
    print(f'#{test_case} {ans}')

