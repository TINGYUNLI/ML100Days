import numpy as np
import pandas as pd

'''
作業目標 : 熟悉分組計算

作業重點 : 分組計算也可以加入apply自定義的函數

題目 : 運用下列分數資料分析 

找出全年級各科成績最高分與最低分？
找出數學班平均最高的班級？
分析全校女生與男生國文平均差幾分？

'''

score_df1 = pd.DataFrame([[1,50,80,70,'boy',1], 
              [2,60,45,50,'boy',2],
              [3,98,43,55,'boy',1],
              [4,70,69,89,'boy',2],
              [5,56,79,60,'girl',1],
              [6,60,68,55,'girl',2],
              [7,45,70,77,'girl',1],
              [8,55,77,76,'girl',2],
              [9,25,57,60,'girl',1],
              [10,88,40,43,'girl',3],
              [11,25,60,45,'boy',3],
              [12,80,60,23,'boy',3],
              [13,20,90,66,'girl',3],
              [14,50,50,50,'girl',3],
              [15,89,67,77,'girl',3]],
              columns=['student_id','math_score','english_score','chinese_score','sex','class'])

# print(score_df1)

score_df = score_df1.set_index('student_id')
print(score_df)

# 找出全年級各科成績最高分與最低分？--------------------------------------------------
print("找出全年級各科成績最高分與最低分？")

score_df_1 = score_df[["math_score","english_score","chinese_score"]].agg(["max","min"])
print(score_df_1)

# 找出數學班平均最高的班級？---------------------------------------------------------
print("找出數學班平均最高的班級？")

score_df_2 = score_df[["math_score","class"]].groupby(['class']).mean()

print("class : ",score_df_2.idxmax(),'\n','score :　',score_df_2.max())

# 分析全校女生與男生國文平均差幾分？-------------------------------------------------
print("分析全校女生與男生國文平均差幾分？")

score_df_3 = score_df[['chinese_score','sex']].groupby('sex').mean()
print(score_df_3)

print(score_df_3.loc['boy']-score_df_3.loc['girl'])
print(score_df_3.iloc[0]-score_df_3.iloc[1])
print(score_df_3['chinese_score'][0]-score_df_3['chinese_score'][1])

print(score_df_3.max()-score_df_3.min())
print(score_df_3.idxmax())