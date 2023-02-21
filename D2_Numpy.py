import numpy as np

#  HW1
'''
請問 type(...) 跟 a.dtype 這兩個語法有什麼不同？
'''

print("HW1-------------------------")

a = np.random.randint(10, size=6) 

print('type(a): ', type(a))
print('a.dtype: ', a.dtype)

'''
type(a) 是回傳 a 變數的型態；a.dtype 是回傳 a 陣列中元素的資料型態。
'''

# HW2
# 請撰寫一個判斷 a 的元素是否等於指定資料型態的函式

print("HW2-------------------------")

def is_dtype(a, t):
    return a.dtype is np.dtype(t)

# a = np.random.randint(10, size=6) 

print(is_dtype(a, 'int')) # True
print(is_dtype(a, np.int)) # True
print(is_dtype(a, np.dtype('int'))) # True


# HW3
'''
承上題，請判斷下列三種寫法為何不正確？
'''

print("HW3-------------------------")

def is_dtype(a, t):
    return a.dtype is t

def is_dtype(a, t):
    return type(a) == np.dtype(t)

def is_dtype(a, t):
    return type(a) is np.dtype(t)

print(type(a.dtype))
print(type(a))
print(a.dtype)
'''
type() 是檢查變數的型態，而不是元素的型態； is 相對 == 更嚴格，一定要型態正確才會回傳 True。
'''
