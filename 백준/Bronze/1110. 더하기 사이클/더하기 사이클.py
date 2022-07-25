N = int(input())
N = str(N)

if int(N) < 10:
    temp = '0'
    temp += N
    N = temp

answer = N
result = 0
while True:
    temp = str(int(N[0]) + int(N[1]))
    newN = N[1]
    newN += temp[len(temp)-1]
    N = newN
    
    result += 1
    if N == answer:
        break
    

print(result)