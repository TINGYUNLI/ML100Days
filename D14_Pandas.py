import numpy as np
import pandas as pd


# ex1-----------------------------------------------------------------------------
'''
比較下列兩個讀入的 df 有什麼不同？為什麼造成的？
'''

df1 = pd.read_csv('https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv')
print(df1)

df2 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv',
    keep_default_na=True,
    na_values=['na', '--']
)
print(df2)


'''
兩者的差別在空白質上的呈現方式有差異，第二的dataframe用NaN來代替原本的na、--
'''

# ex2-----------------------------------------------------------------------------
'''
請將 Dcard API 取得所有的看板資訊轉換成 DataFrame，並且依照熱門程度排序後存成一個 csv 的檔案。
'''
import requests
r = requests.get('https://www.dcard.tw/service/api/v2/forums')
response = r.text

import json
data = json.loads(response)

print(data)

df = pd.DataFrame(data)
df = df.sort_values(by = 'subscriptionCount', ascending = False)
df.to_csv('./Dcard.csv')
print(df)
