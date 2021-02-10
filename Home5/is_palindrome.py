def pal(str_):
    if len(str_) == 0 or len(str_) == 1:
        return 'Yes'
    else:
        if str_[0] != str_[-1]:
            return 'No'
        else:
            str_ = str_[1: len(str_) - 1]
            return pal(str_)


st_ = input('Enter a string ')
res_ = pal(st_)
print(res_)
