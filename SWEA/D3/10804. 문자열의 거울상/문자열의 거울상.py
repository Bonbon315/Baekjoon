T = int(input())
original = ['b', 'd', 'p', 'q']
mirror = ['d', 'b', 'q', 'p']
for test_case in range(1, T+1):
    word = input()
    word = word[::-1]
    ans = ''
    for i in word:
        ans += mirror[original.index(i)]
    print(f'#{test_case} {ans}')