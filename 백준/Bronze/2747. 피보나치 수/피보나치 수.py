def fib(n):
    num, nextnum = 0, 1
    for _ in range(n):
        num, nextnum = nextnum, num + nextnum
    return num
    

n = int(input())
print(fib(n))
