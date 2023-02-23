import numpy as np
import timeit

# ex1 --------------------------------------------------------------

'''
請比較對一個 100 x 100 * 100 的陣列，使用不同方法對每一個元素 +1 的時間比較。
'''
print("---------------------ex1---------------------------")

# 方法1:迴圈 -------------------------------------------------------
'''
z=np.random.randint(0,10,12).reshape(3,2,2)
print(z)
print("-----------------")
for i in z :
    for j in i : 
        for k in j:
            j=j+1
            break
        
print("-----------------")
print(z)
'''

z=np.random.randint(0,100,1000000).reshape(100,100,100)

def one():
    for i in z :
        for j in i : 
            for k in j : 
                j=j+1
                break
# 不改寫原本陣列值

t1=timeit.timeit(one,number=10)
print("t1 : ",t1)


# 方法2:flat -------------------------------------------------------


def two():
    for i in z.flat:
        i=i+1
# 不改寫原本陣列值

t2=timeit.timeit(two,number=10)
print("t2 : ",t2)


# 方法3:nditer -------------------------------------------------------


def three():
    for i in np.nditer(z):
        i=i+1

t3=timeit.timeit(three,number=10)
print("t3 : ",t3)



# ex2 --------------------------------------------------------------

'''
如何從一個陣列中，找出出現頻率最高的數值與位置？
'''
print("---------------------ex2---------------------------")

y=np.random.randint(0,10,20)
print(y)

rint=(np.bincount(y).argmax())
print(rint)
x = y == rint
print("x:",x)
x_index=np.where(x)
print(x_index)


# ex3

'''
如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
'''
print("---------------------ex3---------------------------")

a=np.random.randint(10,size=6)

print(a.tolist())
print(list(a))

b=np.random.randint(10,size=(3,4))

print(b.tolist())
print(list(b))

c=np.random.randint(10,size=(2,3,2))

print(c.tolist())
print(list(c))

print("********************************")

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

