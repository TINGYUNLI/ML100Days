import numpy as np

# ex1
'''
請問下列這三種方法有什麼不同？
print(a.sum())
print(np.sum(a))
print(sum(a))
'''

'''
a.sum()和 np.sum(a) 為 ndArray 專用函式，兩者差別為一個定義在 array下、一個定義在 np 下。
sum() 為 python 內建的函式，所有型態皆可用

'''



# ex2
'''
請對一個 5x5 的隨機矩陣作正規化的操作。
# 正規化 : 把一個array全部都轉換成0~1之間
'''

a=np.random.random((5,5))
print(a)

a=(a-a.min())/(a.max()-a.min())
print(a)


# ex3
'''
請建立一個長度等於 10 的正整數向量，並且將其中的最大值改成 -1。
'''
print("------------------------------------")

b=np.random.random(10)
print(b)
b1=np.random.rand(10)
print(b1)

b2=np.random.randint(10)
print(b2)
print("**************************")
b3=np.random.randint(10,size=5)
print(b3)
print(b3.argmax()) # 最大值的位置
print(b3[b3.argmax()]) # 最大值本人
print("**************************")

b[b.argmax()]=-1
print(b)