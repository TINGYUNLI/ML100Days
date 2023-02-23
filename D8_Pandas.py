import numpy as np
import pandas as pd

# ex1
'''
請問 Pandas 套件最主要的貢獻是什麼？

'''
'''
在numpy的數學運算和真實資料的使用場景中，去建立一種適合資料分析以及數學的資料結構，叫做dataframe

「將適用數學的陣列型態，封裝成適合用於資料分析的型態」

'''


#ex2
'''
根據提供的資料集，印出他們的屬性分別為何？
（屬性：shape、size、values、index、columns、dtypes、len）

'''

df = pd.read_csv("https://raw.githubusercontent.com/MachineLearningLiuMing/scikit-learn-primer-guide/master/Data.csv")
print(df)

print("-----------------------")

print("df.shape : ",df.shape)
print("df.size : ",df.size)
print("df.values : ",df.values)
print("df.index : ",df.index)
print("df.columes : ",df.columns)
print("df.dtypes : ",df.dtypes)
print("len(df) : ",len(df))
