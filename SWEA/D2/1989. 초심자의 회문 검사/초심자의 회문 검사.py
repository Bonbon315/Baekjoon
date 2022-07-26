T = int(input())
for test_case in range(1, T + 1):
    word = input()
    reverseword = word[::-1]
    
    if word == reverseword:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
