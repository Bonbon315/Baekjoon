N = int(input())

result = 0
for num in range(1, N+1):
    if num < 100:
        result += 1
    else:
        if int(str(num)[0]) - int(str(num)[1]) == \
            int(str(num)[1]) - int(str(num)[2]):
            result += 1

print(result)
