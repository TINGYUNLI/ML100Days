import numpy as np
import pandas as pd

# ex1--------------------------------------------------------------------
'''
請接下列資料依照指定規則做合併：
- 依照 fruit 欄位做合併
- 依照 index 索引做合併
'''
df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)
})

df2 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'pine'] * 2,
    'weight': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)
})
print(df1)
print("")
print(df2)

print("ans1***************************************")

print(pd.merge(df1,df2,on="fruit"))
print("")

# print(df1.join(df2)) # 錯誤

# ex2--------------------------------------------------------------------
'''
承上題，請問為什麼依照 merge 合併後有些資料不見了？
'''
'''
因為merge有預設是兩邊同時存在才會被合併，只存在一邊的資料就會不見。
'''
print("merge solution : ")
print(pd.merge(df1,df2,on="fruit",how='outer'))

'''
how 可以為'inner'、'outer'、'left'、'right'，預設為'inner'
'''

# ex3--------------------------------------------------------------------
'''
承上題，請問為什麼依照 index 合併會發生錯誤？請用程式解決。
'''
'''
因為欄位重複，導致無法正確合併。
'''
print("join index solution : ")

print("solution 1 : ")
print(df1.join(df2,lsuffix="_df1",rsuffix="_df2"))

print("")

print("solution 2 : ")
print(pd.merge(df1,df2, left_index=True, right_index=True, how='outer')
)
# 可修正重複欄位所造成的錯誤