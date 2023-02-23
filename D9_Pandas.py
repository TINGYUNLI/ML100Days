import pandas as pd
import numpy as np

#ex1
'''
請建立類似提供結果的 DataFrame：
#    Apples  Bananas
# 0      30       21

#             Apples  Bananas
# 2017 Sales      35       21
# 2018 Sales      41       34
'''
df = pd.DataFrame([[30,21]],columns=['Apples','Bananas'])
df2 = pd.DataFrame([[35,21],[41,34]],columns=['Apples','Bananas'],index=['2017 Sales','2018 Sales'])
print(df)
print(df2)

#ex2
'''
請問如果現在有一個 DataFrame 如下，請問資料在 Python 中可能長怎樣？
#      city  visitor weekday
# 0  Austin      139     Sun
# 1  Dallas      237     Sun
# 2  Austin      326     Mon
# 3  Dallas      456     Mon
'''
d = [['Austin',139,'Sun'],['Dallas',237,'Sun'],['Austin',326,'Mon'],['Dallas',456,'Mon']]

df3 = pd.DataFrame(d,columns=['city','visitor','weekday'])
print(df3)

#ex3
'''
假設你想知道每個 weekday 的平均 visitor 數量，可以怎麼做？
'''

for day in set(df3['weekday']):
    print(day,df3[df3['weekday']==day]['visitor'].mean())


for day in df3['weekday']:
    print(day,df3[df3['weekday']==day]['visitor'].mean())