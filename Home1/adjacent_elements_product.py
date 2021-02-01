inp = input('մուտքագրեք թվերը ')
inp_sp = inp.split()
el_qanak = len(inp_sp)
tiv = []
Mul = [int(inp_sp[0]) * int(inp_sp[1])]
for i in range(1, el_qanak-1):
    tiv.append(int(inp_sp[i]))
    Mul.append(int(inp_sp[i]) * int(inp_sp[i + 1]))
print(Mul)
max_ = Mul[0]
for i in range(len(Mul)):
    if max_ < Mul[i]:
        max_ = Mul[i]
print(max_)
