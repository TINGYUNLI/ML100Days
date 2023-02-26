import numpy as np
import pandas as pd

# ex1----------------------------------------------------------------
'''
根據題目給的 DataFrame 完成下列操作：
- 計算每個不同種類 animal 的 age 的平均數
- 將資料依照 Age 欄位由小到大排序，再依照 visits 欄位由大到小排序
- 將 priority 欄位中的 yes 和 no 字串，換成是布林值 的 True 和 False
'''
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)

print(df)
print("")

print(df.groupby('animal').age.mean())
print("")

sort = df.sort_values(by = ['age','visits'],ascending = [True, False])
print(sort)
print("")

df['priority'] = df['priority'].replace(['yes','no'],[True, False])
print(df)


# ex2----------------------------------------------------------------
'''
一個包含兩個欄位的 DataFrame，將每個數字減去
* 1) 該欄位的平均數
* 2) 該筆資料平均數
'''
df1=pd.DataFrame(np.random.random(size=(5,3)))
print("ex2-------------------------------------------")
print(df1)
print("行MEAN : \n",df1.mean()) # 每一直行的平均值
print(df1-df1.mean())

print("列MEAN : \n",df1.mean(axis=1)) # 每一橫列的平均值
print(df1-df1.mean(axis=1))


# ex3----------------------------------------------------------------
'''
承上題，請問：
* 1) 哪一比的資料總合最小
* 2) 哪一欄位的資料總合最小
'''
print("ex3-------------------------------------------")
print("")

print("橫列總和最小 : \n",df1.sum(axis=1).idxmin()) # 顯示第幾列總和最小
print("直行總和最小 : \n",df1.sum().idxmin()) # 顯示第幾行總和最小

