def fact(y):
    f = 1
    for i in range(1, y + 1):
        f *= i
    return f


num = None
while num is None:
    num = input('մուտքագրեք ոչ բացասական ամբողջ թիվ ')
    if num.isdecimal():
        num = int(num)
        if num == 0:
            print(1)
        else:
            print(fact(num))
            num = None
    else:
        num = None
    continue
