
import gc

a = [1,2]    # [1,2] -> #1212-> a , b
b = [1,2]


# re - 2


del a  # 1

del b # 0

# [1,2] - 0 memory reference counting in gc 



a = [1,2,3]  # 1
k = [4,5,6]  # 1

a.append(k)
k.append(a)

print(a)
print(k)# 1


del a 
del k 
print(k) # 1

