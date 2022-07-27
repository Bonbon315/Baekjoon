N = int(input())
big = []
for i in range(N):
    big.append(list(map(int, input().split())))

for i in big:
    result = 1
    for k in big:
        if i[0] < k[0] and i[1] < k[1]:
            result += 1
    print(result, end=' ')
