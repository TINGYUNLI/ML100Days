import pandas as pd
import numpy as np

#ex1----------------------------------------------------------------------
'''
請問下列四種不同的 DataFrame 選取結果有什麼差異？

df.loc[ '2013-01-01', 'A'] # 結果為數值型態
df.loc[ '2013-01-01', ['A', 'B'] ] # 結果為series
df.loc[ '2013-01-01':'2013-01-02', 'A' ] # 結果為series
df.loc[ '2013-01-01':'2013-01-05', 'A':'C'] # 結果為dataframe
'''
'''
取出的資料型態不同
'''


#ex2----------------------------------------------------------------------
'''
請根據提供的資料，選擇出下列的要求：
# - select the first 3 rows.
# - select the odd rows. (index = 1, 3, 5)
# - select the last 2 columns.
# - select the even columns. (index = 0, 2, 4)
'''
df = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])

print(df)
print("***ANS2***")
print(df[0:3])
print(df[1::2]) # 間隔2個
print(df.iloc[:,-2:]) # 橫列沒有限制，直行從第-2行到最後1行
print(df.iloc[:,0::2])
print("********")
print(df[2::])
                  


#ex3----------------------------------------------------------------------
'''
請根據提供的資料，選擇出下列的要求：
# - 1. filtered by first column > 20?
# - 2. filtered by first column + second column > 50
# - 3. filtered by first column < 30 or second column > 30
# - 4. filtered by total sum of row > 100
'''
df1 = pd.DataFrame(np.random.randint(10,40,60).reshape(-1,4))

print(df1)

print("***ANS2***")
print("")
print(df1[1]) # 顯示第1直行
print(df1[0]>20) # 顯示第0行中大於20的布林值
print(df1[df1[0]>20]) # 顯示第0行中大於20的實際值(整個表)
print("")

print(df1[df1[0]+df1[1]>50])
print("")

print(df1[ (df1[0]<30) | (df1[1]>30) ])
print("")

print(df1[df1.sum(axis=1)>100]) # 每筆資料橫項總和相加大於100


