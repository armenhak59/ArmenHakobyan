dict_ = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
st = input('Enter Roman number, may include only "M", or "D", or "C", or "L", or "X", or "V", or "I" \n')
s_ = []
s_[:0] = st
count = 1
sum_ = 0
for i in range(len(s_)-1):
    end_char = s_.pop()
    sum_ += (count * dict_[end_char])
    if dict_[end_char] > dict_[s_[-1]]:
        count = -1
    else:
        count = 1
sum_ += (count * dict_[s_[-1]])
print(sum_)
