def prime(y):
    for i in range(2, y):
        if y % i == 0:
            return 'No'
    return 'Yes'


num = None
while num is None or '0':
    num = input('մուտքագրեք բնական թիվ ')
    if num == '':
        exit()
    if num == '1':
        print('1-ը պարզ թիվ չէ')
    if num.isdecimal() and int(num) > 1:
        num = int(num)
        print(prime(num))
        num = None
    else:
        num = None
