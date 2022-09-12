def mult3(x, cnt):
    if len(x) > 1:
        cnt += 1
        num = 0
        for i in x:
            num += int(i)
        mult3(str(num), cnt)
    else:
        if int(x) % 3:
            print(cnt)
            print('NO')
        else:
            print(cnt)
            print('YES')


X = input()
cnt = 0
mult3(X, cnt)
