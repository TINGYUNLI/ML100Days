import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
1. 將每個class中男性和女性的平均存活率用長形圖可視化
'''
df=sns.load_dataset("titanic")
# df.info()

sns.barplot(x='sex',y='survived',hue='class',data=df)
plt.show()

'''
2. 瞭解性別在各艙等存活率的分布
'''
g=sns.FacetGrid(df,col='pclass')
g.map(sns.barplot,"sex","survived",order=['female','male'])
plt.show()

'''
3. 繪製堆疊條形圖，x軸代表依據艙等分成男性及女性，y軸代表人數，
其中藍色代表死亡人數，橘色代表存活人數
'''
survived=df.groupby(['pclass','sex']).survived.sum()
print(survived)

survived_counts=pd.crosstab([df.pclass,df.sex],df.survived)
print(survived_counts)

survived_counts.plot.bar(stacked=True) # survived堆疊在同一條
# survived_counts.plot.bar()
plt.show()

'''
4. 瞭解性別在各艙等的存活率的分布 (PS: 跟第一次做 Face.Grid 有何不同??)
'''

g1=sns.FaceGrid(df,col='sex')
g1.map(sns.barplot,'pclass','survived',order=[1,2,3])
plt.show()
# 以性別切分子圖，計算艙等和存活的關係
# 第一次是以艙等切分子圖，計算性別和存活的關係