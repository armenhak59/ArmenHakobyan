mutq = input('մուտք ')
mlist = [m for m in mutq if m != ' ']
mset = set(mlist)
if len(mlist) > len(mset):
    print('No')
else:
    print('Yes')
