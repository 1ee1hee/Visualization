# 실습
# 1. 파이차트
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1_1.
labels = ['사과', '배', '수박', '귤', '복숭아']
counts = [20, 10, 50, 40, 30]

plt.figure(figsize=(7, 7))

# pie(수량, 라벨)
plt.pie(counts, labels = labels,
        autopct = '%.2f%%',
        shadow = True,
        explode = [0, 0, 0.2, 0, 0.2]
        )

plt.show()

# 1_2.
plt.figure(figsize = (6, 6))

wedge, texts, autopcts = plt.pie(counts,
                                 autopct = '%.2f%%', 
                                 shadow = True,
                                 explode = [0, 0, 0.2, 0, 0.2])

# label을 범례로
plt.legend(wedge, labels, bbox_to_anchor = (1, 1), loc = 'upper left', title = '과일')

plt.show()



# 2. 파이차트 활용
df = pd.read_excel('data/webbrowser_share.xls', parse_dates = [0], index_col = 0)
pd.options.display.max_columns = 25
print(df.info())
print(df.columns)

etc = df[df.columns[6:]].sum(axis = 1)
print(etc)

web_df = df[df.columns[:6]].copy()
web_df['Etc'] = etc
print(web_df)

wedge, _, _ = plt.pie(web_df.loc['2018-08-01'], autopct = '%.2f%%', shadow = True,
                      pctdistance = 1.15,
                      textprops = {'fontsize' : 7, 'color' : 'blue', 'fontweight' : 'bold'}
                      )
plt.legend(wedge, web_df.columns, bbox_to_anchor = (1, 1), loc = 'upper left')

plt.show()



# 3. 히스토그램
data = np.random.normal(100, 10, 1000) # 평균: 100, 표준편차 : 10, 정규분포를 따르는 난수 1000개
v, cnt = np.unique(data, return_counts = True) # 고유값과 개수
print(cnt.max())

plt.hist(data, bins = 30)

plt.show()



# 4. 히스토그램 활용
df = pd.read_csv('data/tips.csv')
print(df.shape)
print(df.info())

# 4_1. total_bill의 분포
plt.hist(df['total_bill'], bins = 30)
plt.title('total_bill')
plt.show()

# 4_2. tip의 분포
plt.hist(df['tip'], bins = 30)
plt.title('tip')
plt.show()

# 4_3. 흡연여부(범주형)
result = df['smoker'].value_counts()
plt.bar(result.index, result)
plt.title('흡연여부')
plt.show()

# 4_4. 흡연여부(다른방법)
df['smoker'].value_counts().plot(kind = 'bar') # 자주 사용
plt.title('흡연여부_1')
plt.show()



# 5. 상자그래프
# 1~99사이의 정수 1000개를 1차원 배열에 묶어서 반환
data = np.random.randint(1, 100, 1000)
data[:5] = [200, 250, -50, -60, -80]
print(data.shape)

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

ax1.set_title('IQR * 1.5')
ax1.boxplot(data) # IQR * 1.5 

ax2.set_title('IQR * 3')
ax2.boxplot(data, whis = 3) # IQR * 1.5 => IQR * 3

ax3.set_title('IQR * 0.1')
ax3.boxplot(data, whis = 0.1) # IQR * 1.5 => IQR * 0.1

plt.show()



# 6. 상자 그래프 활용
# 6_1. tip의 분포를 상자그래프로 확인
tips = pd.read_csv('data/tips.csv')
print(tips.shape)

plt.boxplot(tips['tip'], labels = ['팁'])
plt.title('tip 분포')
plt.ylabel('Tip(Dollar)')
plt.grid(True)
plt.show()


# 6_2. 남녀별 tip의 분포를 하나의 boxplot에 그리기
print(tips['sex'].value_counts())

male_tip = tips.loc[tips['sex'] == 'Male', 'tip']
female_tip = tips.loc[tips['sex'] == 'Female', 'tip']

plt.boxplot([male_tip, female_tip], labels = ['남성', '여성'])
plt.title('남녀별 tip 분포')
plt.xlabel('성별')
plt.ylabel('Tip (Dollar)')
plt.show()