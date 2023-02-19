import numpy as np
a = np.arange(15).reshape(3, 5)

print(a)
# HW1
print('list(a): ', list(a)) #只會把第一層的元素轉換成List
print('tolist(): ', a.tolist()) #全部資料的型態一起轉換

# HW2
print('ndim: ', a.ndim) # 陣列維度
print('shape: ', a.shape) #維度大小
print('size: ', a.size) #陣列元素
print('dtype: ', a.dtype) #陣列中的資料型態
print('itemsize: ', a.itemsize) #陣列中元素佔的空間
print('length: ', len(a)) #資料長度
print('type: ', type(a)) #資料型態

# HW3
a = np.random.randint(10, size=6)
b = np.random.randint(10, size=(3,4))
c = np.random.randint(10, size=(2,3,2))
def tolist(iterable):
    return iterable.tolist()
print(tolist(a))
print(tolist(b))
print(tolist(c))