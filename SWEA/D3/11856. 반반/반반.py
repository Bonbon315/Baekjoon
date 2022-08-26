T = int(input())

for test_case in range(1, T + 1):
    word = list(input().rstrip())
    worddic = dict()
    half = True
    for i in word:
        if i not in worddic:
            worddic[i] = 1
        else:
            worddic[i] += 1
    
    if len(worddic) == 2:
        for k, v in worddic.items():
            if v != 2:
                half = False
    else:
        half = False

    if half:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')