import numpy as np

# HW1
'''
請問下列程式碼，運算結果分別為何？
'''
a = np.array( [20,30,40,50] )
b = np.array( [1,2,3,4] ) 
c = 1
d = np.array( [1] )
e = np.array( [1,2] ) 

print("HW1-----------------------")
print(a + a)
print(a + b)
print(a + c)
print(a + d)
# print(a + e) # 廣播效果會失效



# HW2
'''
如何在不用迴圈的情況下計算 (A+B)*(-A/2) ？那用迴圈怎麼做？
'''
print("HW2-----------------------")

A=np.ones(3)
B=np.ones(3)*2
print(A)
print(B)
print((A+B)*(-A/2))



# HW3
'''
請問如何計算「1x6 的單位矩陣」和「6x1 的單位矩陣」的內積和外積？
'''
print("HW3-----------------------")

C=np.ones((1,6))
D=np.ones((6,1))
# np.ones((shape, dtype, order))

print(C)
print(D)
print(C*D) # 內積，就是普通乘法
print(C@D) # 外積，使用「@」