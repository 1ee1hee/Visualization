# 실습 
# 1. 막대그래프
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

s = pd.Series([100, 70, 90, 130, 50], index = ['사과', '배', '귤', '수박', '복숭아'])
s.plot(kind = 'bar', title = '과일 수량', xlabel = '과일종류', ylabel = '개수', figsize = (6, 5), rot = 45)
plt.show()


# 2. 막대 그래프 활용
tips = pd.read_csv('data/tips.csv')

# 2_1. 요일별 테이블 수
cnt_result = tips['day'].value_counts()
print(cnt_result)

cnt_result.plot(kind='bar', title='요일별 테이블수', xlabel='요일', ylabel='테이블수', grid=True, rot=0)
plt.show()

# 2_2. 흡연여부에 따른 테이블 수
tips['smoker'].value_counts().plot(kind='barh', figsize=(5, 3), title='흡연여부에 따른 테이블수',
                                   color=['green', 'red']
                                   )
plt.show()

# 2_3. 두개의 분류 별로 그리기
agg_df = tips.pivot_table(index='smoker', columns='sex', values='tip', aggfunc='count')
print(agg_df)

agg_df.plot(kind='bar', title='흡연여부/성별 테이블수', xlabel='흡연여부', ylabel='테이블수', rot=0)
plt.show()

# 2_4. 요일 / 성별 손님의 총수
result = tips.pivot_table(index='sex', columns='day', values='size', aggfunc='sum')
print(result)

result.plot(kind='bar', stacked=True, rot=0)
plt.legend(bbox_to_anchor = (1, 1), loc = 'upper left', title = 'day')
plt.show()

# 2_5. 요일 / 성별 손님의 총수(각각 그리기)
result.plot(kind='bar', subplots=True, figsize=(6, 10))
plt.show()

# 2_6. 요일별 매출액 비교
tips.groupby('day')['total_bill'].sum().plot(kind='bar', title='요일별 매출액 비교', rot=0)
plt.show()



# 3. 파이차트
# 3_1.
print(tips['day'].value_counts())
tips['day'].value_counts().plot(kind='pie', autopct='%.2f%%', explode=[0, 0, 0, 0.2], shadow = True)
plt.show()

# 3_2.
tips.groupby('time')['tip'].mean().plot.pie(autopct='%.2f%%', shadow= True, explode = [0, 0.2])
plt.show()




# 4. 히스토그램, KDE(밀도 그래프)
# 4_1. 히스토그램
tips['tip'].plot.hist(bins = 20)
plt.show()

# 4_2. KDE
tips['tip'].plot(kind='kde')
plt.show()

# 4_3.
tips[['total_bill', 'tip']].plot(kind='hist', bins=30, alpha=0.7)
plt.show()

# 4_4.
tips[['total_bill', 'tip']].plot(kind='kde')
plt.show()




# 5. Boxplot(상자그래프)
# 5_1.
tips['total_bill'].plot(kind='box', whis = 3)
plt.show()

# 5_2.
tips[['tip', 'total_bill']].plot(kind = 'box', figsize = (5, 5))
plt.show()




# 6. scatter plot(산점도)
tips.plot(kind='scatter', x='total_bill', y='tip')
plt.show()
print(tips[['total_bill', 'tip']].corr()) # 상관관계 파악




# 7. line plot
df = pd.read_excel('data/강수량.xlsx', engine = 'openpyxl')
df = df.set_index('계절').T
print(df['봄'])

# 7_1. x : index, y : value
df['봄'].plot(figsize = (10, 4), xlabel = '년도', ylabel = '강수량')
plt.show()

# 7_2. 컬럼별로 선 그래프 그리기
df.plot(figsize = (15, 4))
plt.show()

# 7_3. 봄 겨울 그래프 그리기
df[['봄', '겨울']].plot()
plt.legend(bbox_to_anchor = (1, 1), loc = 'upper left', title = '계절')
plt.show()