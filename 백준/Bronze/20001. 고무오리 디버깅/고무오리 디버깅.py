duck = input()
cnt = 0

while duck != '고무오리 디버깅 끝':
    duck = input()
    if duck == '문제':
        cnt += 1
    elif duck == '고무오리':
        if cnt > 0:
            cnt -= 1
        else:
            cnt += 2

if cnt > 0:
    print('힝구')
else:
    print('고무오리야 사랑해')