K = int(input())

money = []

for i in range(K):
    temp = int(input())
    if temp == 0:
        money.pop()
    else: money.append(temp)

print(sum(money))