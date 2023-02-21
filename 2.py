import numpy as np

a = np.random.randint(10, size=(3,4)) 

'''
a.dtype : 陣列中的資料型態，一個array只會有一種dtype，規定array裡面的元素必須是相同的型態
例: int64，表示是64個位元長度的int，64 bit，此數除8會等於itemsize的答案

a.itemsize : 陣列中每個元素佔用的空間，例:8，表示每個元素占用 8 byte

'''

print(a.dtype)
print(a.itemsize)
print(a.dtype == "int32") # true
print(a.dtype is "int32") # false #型態不同
print(a.dtype is np.int32) # false #型態不同

a1="1" 
print(a1 is "1")

'''
== 僅判斷內容是否相同
is 會判斷內容&型態是否相同
'''
print(a.dtype == np.int32) # true
print(a.dtype == "int32") # true
print(a.dtype is np.dtype("int32")) # true



