import numpy as np
import pandas as pd

'''
作業目標 :

熟悉索引與欄位設定、使用樞紐建立新資料

作業重點 :

多維度索引、欄位是有順序性的須注意，使用樞紐建立資料需要注意參數
index : 新資料的索引名稱
columns : 新資料的欄位名稱
values :新資料的值名稱

題目 : 運用下列分數資料重新建構資料，將索引(index)依序改為sex、class、student_id，
欄位依序改成chinese_score、english_score、math_score
'''
score_df = pd.DataFrame([[1,50,80,70,'boy',1],[2,60,45,50,'boy',2],
                         [3,98,43,55,'boy',1],[4,70,69,89,'boy',2],
                         [5,56,79,60,'girl',1],[6,60,68,55,'girl',2],
                         [7,45,70,77,'girl',1],[8,55,77,76,'girl',2],
                         [9,25,57,60,'girl',1],[10,88,40,43,'girl',3],
                         [11,25,60,45,'boy',3],[12,80,60,23,'boy',3],
                         [13,20,90,66,'girl',3],[14,50,50,50,'girl',3],
                         [15,89,67,77,'girl',3]],
                         columns=['student_id','math_score','english_score','chinese_score','sex','class'])

print(score_df)

print("1***********************************************")
df = score_df.melt(id_vars=['sex','class','student_id']) # 不被轉換的欄位
print(df)

'''
被轉換的欄位名稱 : variable
被轉換的欄位名稱對應值 : value
'''

df1 = df.pivot_table(index=['sex','class','student_id'],columns='variable',values='value')

print("2***********************************************")
print(df1)
