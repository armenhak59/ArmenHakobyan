mutq = input('մուտքագրեք թվերը ')
tver = mutq.split()
el_qanak = len(tver)
tver1 = []
Mul = []
# print(el_qanak)
for i in range(el_qanak-1):
    tver1.append(int(tver[i]))
    Mul.append(int(tver[i]) * int(tver[i+1]))
print (Mul)
max = False
for i in range(len(Mul)):
    if max < Mul[i]:
        max = Mul[i]
print (max)