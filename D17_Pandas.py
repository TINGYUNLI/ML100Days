import numpy as np
import pandas as pd

'''
題目：運下列時間序列資料做運算

index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)

1. 將所有轉為周資料
2. 將周資料的值取平均
'''

index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)
print(series)
a=series.to_period('W')
print(series.to_period('W'))
'''
顯示連續12周，周一和週日的日期和週數
'''
print(series.resample('W').mean())
print(series.resample('W',convention='s').mean())
print(a.mean()) # 答案不同
print(series.resample('W',convention='s').asfreq()) # 只顯示週日