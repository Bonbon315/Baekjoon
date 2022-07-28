def d(n):
    digits = []
    for i in str(n):
        digits.append(int(i))
    return n + sum(digits)

numbers = set(range(1, 10001))
dnum = set()

for i in range(1, 10001):
    dnum.add(d(i))

selfnum = sorted(numbers - dnum)
for i in selfnum:
    print(i)