T = int(input())

for test_case in range(1, T + 1):
    word = input().rstrip()

    word = word.replace('a', '')
    word = word.replace('e', '')
    word = word.replace('i', '')
    word = word.replace('o', '')
    word = word.replace('u', '')

    print(f'#{test_case} {word}')