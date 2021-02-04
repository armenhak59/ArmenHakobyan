hasak_ = input('մուտքագրեք հասակները ').split()
for i in range(len(hasak_)):
    hasak_[i] = int(hasak_[i])
max_ = max(hasak_)
stools = [max_ - hasak_[i] for i in range(len(hasak_)) ]
print(stools)
