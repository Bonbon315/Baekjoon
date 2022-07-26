T = int(input())

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]

for i in range(T):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    print(f'#{i+1} ', end='')
    if int(month) in month31:
        print(f'{year}/{month}/{day}') if 0 < int(day) < 32 else print(-1)
    elif int(month) in month30:
        print(f'{year}/{month}/{day}') if 0 < int(day) < 31 else print(-1)
    elif int(month) == 2:
        print(f'{year}/{month}/{day}') if 0 < int(day) < 29 else print(-1)
    else:
        print(-1)