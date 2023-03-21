import random

for i in range(10):
    if i==110:
        print('Error')
    elif i==115:
        print('Error')
    elif i==119:
        print('Error')
    else:
        p=(random.randrange(100,120,2))
        i=(random.randrange(100,120,3))
        print(p, end=' , ')
        print(i, end=' , ')
    