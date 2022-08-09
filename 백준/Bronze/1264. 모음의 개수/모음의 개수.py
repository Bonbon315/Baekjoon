while True:
    sent = input()
    cnt = 0
    if sent == '#':
        break
    for i in sent:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)