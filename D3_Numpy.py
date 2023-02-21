import numpy as np

# HW1
'''
請比較 np.zeros 和 np.empty 產生出來的陣列有何差異？為什麼要設計兩種方法？
'''
print("HW1-------------------------")

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
#print(np.empty((2, 3)))
print(np.empty((3, 4)))

'''
np.zeros((2, 3)) 會產生真正的 0；np.empty((2, 3)) 會產生一個近似於 0 的陣列。
np.empty 可以用於只是想要初始化，但之後就會數值覆寫過的形況。
'''


# HW2
'''
在不用「整數亂數方法」的限制下，如何將包含小數的轉換整數？請將給定的 a 陣列當中的元素變成去掉小數變成整數。
'''
print("HW2-------------------------")

a = np.random.rand(3, 4) # 3橫列，4直行 # 產出0~1之間的隨機變數
a = a * 100 # 將0~1之間的隨機變數，分別進2位

print(a)

print(a.round()) # 四捨五入
# print(round(a)) : ndarray不適用
print(np.round(a))

'''
print(" 比較(普通浮點數) : ")
z=1.758999
# print(z.round()) : 浮點數不適用
print(round(z)) # 四捨五入
print(round(z,2)) # 取到小數點後2位

print(" 比較(普通列表) : ")
x=[1.555,2.111,3.9]
# print(x.round()) : 列表不適用
# print(round(x)) : 列表不適用
'''

# HW3
'''
承上題，怎樣可以限制整數的範圍介於 m - n 之間？請將給定的 a 陣列當中的元素的範圍調整成 m - n 之間。
'''
print("HW3-------------------------")

m = 20
n = 40

aa = np.random.rand(2, 3)
a1 = np.random.rand(2, 3) * (n - m) # 得到結果，最多不會超過最大數和最小數之間的差距
b1 = a1

print(aa)
print(b1)
print(b1%1) # 取出變數的小數部分
print(a1 - b1 % 1) # 減去小數部分，相當於無條件捨去
print((a1 - b1 % 1) + m) # 最多不會超過最大數和最小數之間差距的結果，再加上最小數，得到之最後結果最多不會超過最大數
