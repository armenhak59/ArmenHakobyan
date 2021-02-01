num = None
sum_ = 0
while num is not None or '0':
    num = input('մուտքագրեք բնական թիվ ')
    if num == '':
        exit()
    if num.isdecimal():
        num = int(num)
        while num >= 10:
            sum_ = 0
            while num // 10 != 0:
                sum_ += num % 10
                num = num // 10
            sum_ += num
            num = sum_
        sum_ = num
    else:
        num = None
        sum_ = 0
    if sum_ != 0:
        print(sum_)
