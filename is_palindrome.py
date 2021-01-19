mutq = input('մուտքագրեք բառը ')
n = len(mutq)
n //= 2
half = mutq[:n+1]
second = mutq[-1:n-1:-1]
if half == second:
    print('YES')
else:
    print('NO')
