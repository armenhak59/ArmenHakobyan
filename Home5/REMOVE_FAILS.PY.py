list_ = {
    'Aram': 44,
    'Avet': 75,
    'Ani': 66,
    'Mick': 55,
    'Sofi': 44,
    'Gaya': 80,
    'Goga': 90,
    'Bela': 67
}
print(list_)
l1 = []
for m in list_:
    if list_[m] < 60:
        l1.append(m)
        # del list_[m]
for m in l1:
    del list_[m]
print(list_)
