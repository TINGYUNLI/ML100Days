import numpy as np

# HW1 --------------------------------------
# 請問下列兩種 (a1,b1) 將 Array 轉換成 List 的方式有何不同？

a1 = np.random.randint(10, size=6) # 產生特定範圍的整數(int)，參數可以放範圍

print("")
print('list (a1) : ', list(a1))
print('a1.tolist () : ', a1.tolist())

b1 = np.random.randint(10, size=6).reshape(3,2)

print('list(b1): ', list(b1))
print('b1.tolist(): ', b1.tolist())

# list(a) 只會把第一層的元素轉換成 List，多層的話只有第一層會轉；tolist() 才能達成多層的型態轉換(全部資料的型態一起轉換)。

# HW2 ------------------------------------------------------------------------------------------------------
# 請試著在程式中印出以下三個(a,b,c) NdArray 的屬性並且解釋結果？
#（屬性：ndim、shape、size、dtype、itemsize、length、type）

a = np.random.randint(10, size=6)

print("a-----------------------")
print(a)
print("")
print('ndim: ', a.ndim) # 陣列維度
print('shape: ', a.shape) #維度大小
print('size: ', a.size) # 陣列元素

print('dtype: ', a.dtype) # 陣列中的資料型態 # 一個array只會有一種dtype，規定array裡面的元素必須是相同的型態
# 例: int64，表示是64個位元長度的int，64 bit，此數除8會等於itemsize的答案

print('itemsize: ', a.itemsize) # 陣列中每個元素佔用的空間 # 例:8，表示每個元素占用 8 byte
print('length: ', len(a)) # 資料長度
print('type: ', type(a)) # 資料型態

b = np.random.randint(10, size=(3,4)) 

print("")
print("b----------------------------")
print(b)
print("")
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)
print(len(b))
print(type(b))

c = np.random.randint(10, size=(2,3,2)) 

print("")
print("c----------------------------")
print(c)
print("")
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)
print(c.itemsize)
print(len(c))
print(type(c))

# HW3---------------------------------------
# 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
print("HW3")
print("1---------------------------------------")
print(a,list(a),a.tolist(),sep="\n")
print("2-------------------------")
print(b,list(b),b.tolist(),sep="\n")
print("3-------------------------")
print(c,list(c),c.tolist(),sep="\n")

print("")
print("簡單版------------------------")
def tolist(iterable):
    if type(iterable) != np.ndarray:
        return iterable
    newlist = []
    for obj in iterable:
        newlist.append(tolist(obj))
    return list(newlist)

print(tolist(a))
print(tolist(b))
print(tolist(c))

print("")
print("複雜版------------------------")
def tolist(iterable):
    if type(iterable) != np.ndarray:
        return iterable
    return [tolist(obj) for obj in iterable]

print(tolist(a))
print(tolist(b))
print(tolist(c))