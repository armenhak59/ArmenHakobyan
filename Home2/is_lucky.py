mutq = input('տոմսի համարը ')
n = len(mutq)
while ((n % 2) != 0 ):
    print('մուտքագրեք զույգ թվանշաններով թիվ')
    mutq = input('տոմսի համարը ')
    n = len(mutq)
tiv = int(mutq)
n //= 2
m = 10 ** n
first_part = tiv // m
second_part = tiv % m
first = str(first_part)
sum_first = sum([int(i) for i in first])
second = str(second_part)
sum_second = sum([int(i) for i in second])
if sum_first == sum_second:
    print('Yes')
else:
    print('NO')
