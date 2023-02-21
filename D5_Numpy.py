import numpy as np

# HW1
'''
產生一個 1-11 的一維陣列，並且把 3-6 由正數變成負數。
'''

a=np.arange(11)+1
a[(3<=a)&(a<7)]*=-1
print(a)


# HW2
'''
試著從一個隨機陣列中，找出比 0.5 大的數有幾個？
'''
print("-------------------------------------")

b=np.random.rand(3,6)
print(b)
print("")
print("篩選後 : ",b[b>0.5])
print("篩選總個數 : ",b[b>0.5].size)
