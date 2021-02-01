def prime(y):
    global ind
    prime_numbers = [2]
    k1 = 0
    for i in range(2, y+1):
        for j in prime_numbers:
            ind = True
            if i % j == 0:
                ind = False
                break
        if ind:
            prime_numbers.append(i)
            k1 += 1
    print(prime_numbers[-1])
    if i == prime_numbers[-1]:
        return k1, 'Yes'
    else:
        return k1, 'No'


num = None
while num is None or '0':
    num = input('մուտքագրեք բնական թիվ ')
    if num == '':
        exit()
    if num == '1':
        print('1-ը պարզ թիվ չէ')
    if num.isdecimal() and int(num) > 1:
        num = int(num)
        k = prime(num)
        if k[1] == 'No':
            print(num, f'ը պարզ չէ, մինչև {num} կա {k[0]} հատ պարզ թիվ')
        else:
            print(f'{num} ը պարզ թիվ է և մինչև {num} կա {k[0]} հատ պարզ թիվ')
    num = None
