# 실습
# Seaborn : matplotlib를 기반으로 다양한 테마와 그래프를 제공하는 파이썬 시각화 패키지
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
print(type(tips))
print(tips)


# rugplot, kdeplot, displot
# 1차원 연속형 값들의 분포를 시각화 하는 그래프
# 1. rugplot : 각 데이터들의 위치를 보여준다
plt.figure(figsize = (4, 3))

sns.rugplot(x = 'total_bill', data = tips)
plt.title('Total bill의 분포')
plt.show()


# 2. kdeplot : 부드러운 곡선 형태, 확률밀도추정
sns.kdeplot(x = 'total_bill', data = tips)
plt.show()


# 3. displot() : rugplot, kdeplot을 같이 그릴 수 있다.
# 3_1. rugplot, kdeplot 같이 그리기
sns.displot(data = tips, x = 'total_bill', bins = 30,
            rug = True, 
            kde = True)
plt.show()

# 3_2. 그룹으로 나누어 그리기
sns.displot(x = 'total_bill', hue = 'smoker', data = tips)
plt.show()



# boxplot(), violinplot(), swamplot()
# 연속형 데이터들(양적 데이터)들의 분포를 확인하는 그래프를 그린다
# 범주별로 연속형 데이터의 분포를 비교할 수 있다
# 4. boxplot
# 4_1.
plt.subplot(1, 2, 1)
sns.boxplot(x = 'total_bill', data = tips)

plt.subplot(1, 2, 2)
sns.boxplot(y = 'tip', data = tips)

plt.show()

# 4_2.
fig = plt.figure(figsize = (10, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# x : 연속형, y : 범주형
sns.boxplot(x = 'total_bill',
            y = 'smoker', hue = 'sex',
            data = tips, ax = ax1)
sns.boxplot(y = 'tip', x = 'smoker', hue = 'time', data = tips, ax = ax2)

ax1.legend(bbox_to_anchor = (0, 1), loc = 'upper right', title = 'sex')

plt.show()


# 5. violin plot
# boxplot 위에 분포 밀도를 좌우 대칭으로 덮어쓰는 방식
# 데이터 분포를 표현 -> boxplot 보다 좀더 정확한 데이터의 분포 확인

plt.figure(figsize = (10, 5))
plt.subplot(1, 2, 1)
sns.violinplot(data = tips, x = 'tip')

plt.subplot(1, 2, 2)

sns.violinplot(data = tips, y = 'tip', x = 'day', hue = 'smoker')

plt.show()


# 6. swarmplot
# 실제 값들을 점으로 찍는다
# boxplot이나 violin plot을 보완
# 가운데 분류를 기준으로 분포, 실제 값이 있는 위치에 점을 찍어 좀 더 정확함
plt.figure(figsize = (10, 7))
plt.subplot(1, 2, 1)
sns.boxplot(y = 'tip', data = tips)
sns.swarmplot(y = 'tip', data = tips, color = 'orange')

plt.subplot(1, 2, 2)
sns.boxplot(x = 'tip', data = tips, color = 'r')
sns.swarmplot(x = 'tip', data = tips)

plt.show()


# 7. countplot
# 막대그래프를 그리는 함수
# 범주형 변수의 고유값의 개수 표시
# matplotlib의 bar()

# 7_1. 요일별
sns.countplot(data = tips, x = 'day')
plt.show()

# 7_2. 요일별_1
sns.countplot(data = tips, y = 'day')
plt.show()

# 7_3. 흡연/비흡연자 개수
sns.countplot(x = 'smoker', data = tips)
plt.show()

# 7_4. 흡연 / 비흡연자 개수 요일별로 나눠서 시각화
sns.countplot(x = 'smoker', hue = 'day', data = tips,
              dodge = False, # 수평 누적 막대 여부 : 기본 -> True
              alpha = 0.3)
plt.show()



# 8. scatterplot, lmplot, joinplot, pairplot
# 산점도를 그림
# 8_1 . scatterplot
sns.set_palette('Set1') 

sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', alpha = 0.5)
plt.show()

# 8_2. 
sns.scatterplot(data = tips, x = 'total_bill', y = 'tip',
            hue = 'smoker', 
            palette = 'Set1')
plt.show()



# 9. lmplot
# 선형회귀 적합선을 포함한 산점도를 그린다
# 9_1.
sns.lmplot(data = tips, x = 'total_bill', y = 'tip') # 오차 표현 가능
plt.show()

# 9_2.
sns.lmplot(data = tips, x = 'total_bill', y = 'tip', hue = 'smoker')
plt.show()



# 10. jointplot
# scatter plot과 각 변수의 히스토그램을 같이 그림
# pandas DataFrame만 사용 가능
sns.jointplot(x = 'total_bill', y = 'tip', data = tips)
plt.show()



# 11. pairplot
# 다차원 데이터들 간의 산점도를 보여준다
# 데이터프레임을 인수로 받아 그리드 형태로 각 변수간의 산점도를 그림
# 같은 변수가 만나는 대각선 영역에는 해당 데이터의 히스토그램을 그림
# 수치형 데이터들만 가지고 보여줌
# 데이터가 많을 때 시간이 오래걸림 -> 필요한 데이터만 추출해서 사용
sns.pairplot(tips)
plt.show()



# 12. heatmap
# 값들에 비례해서 색깔을 다르게 해 2차원 자료로 시각화
sns.heatmap(tips.corr(), annot = True, fmt = '.3f', cmap = 'Blues')
plt.show()



# 13. lineplot
# 선그래프
# 시간의 흐름에 따른 값의 변화를 보여주는데 유용

import pandas as pd
import numpy as np

# 13_1.
index = pd.date_range('2023/01/01', freq='MS', periods=10)
values = np.random.randint(1, 100, size = (10, 3))
df = pd.DataFrame(values, index = index, columns = ['no1', 'no2', 'no3'])
print(df)

plt.figure(figsize = (10, 3))
sns.lineplot(data = df, y = 'no1', x = df.index)
sns.lineplot(data = df, y = 'no2', x = df.index)
sns.lineplot(data = df, y = 'no3', x = df.index)

plt.legend(['NO1', 'NO2', 'NO3'])
plt.show()

# 13_2.
df['cate'] = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'C']
print(df)

plt.figure(figsize = (10, 4))
sns.lineplot(data = df, x = df.index, y = 'no1', hue = 'cate')
plt.show()