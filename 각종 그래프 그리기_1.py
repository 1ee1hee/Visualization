# 실습
# 1. 선 스타일
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(1, 10, num = 100)
x2 = pd.Series(x)

# plt 함수를 이용해서 선 그래프 그리기
plt.plot(x, x, marker = '.', color = 'black')
plt.plot(x, x+1, linestyle = '--')
plt.plot(x, x+2, linestyle = ':')
plt.plot(x, x+3, linestyle = '-.', linewidth = 5)
plt.show()

# 2. 선 그래프 활용
df = pd.read_csv('data/서울시 연도별 황사 경보발령 현황.csv')
print(df.shape)
print(df.info())

# '최대농도(㎍/㎥/시)' => '최대농도'
df.rename(columns = {'최대농도(㎍/㎥/시)' : '최대농도'})
df.rename(columns = {df.columns[-1] : '최대농도'}, inplace = True)

# 2_1. 연도에 따른 황사 최대 농도의 변화 흐름
plt.figure(figsize = (10, 3))
plt.plot(df['년도'], df['최대농도'], marker = '.')
plt.title('서울시 년도별 황사 최대농도의 변화흐름')
plt.xlabel('년도', fontsize = 15)
plt.ylabel('최대농도', fontsize = 15)

plt.xticks(df['년도'], labels = [str(y)+'년' for y in df['년도']], # tick 라벨의 size == ticks의 size
           rotation = 45
           ) # 눈금의 위치, Labels = ticks라벨에 사용할 문자열 리스트
plt.grid(True, linestyle = ':')

plt.show()

# 2_2. 년도에 따를 주의보 / 경보 발령횟수의 변화 ==> 하나의 subplot(axes)에 같이 그리기
plt.figure(figsize = (10, 3))

plt.plot(df['년도'], df['주의보 발령횟수'], alpha = 0.7, label = '주의보 발령횟수') # alpha = 투명도 : 0(투명) ~ 1(불투명)
plt.plot(df['년도'], df['경보 발령횟수'], alpha = 0.5, label = '경보 발령횟수')

plt.title('년도별 주의보 / 경보 발령횟수')
plt.xlabel('년도')
plt.ylabel('횟수')

plt.legend() # 범례
plt.grid(True)
plt.show()

# 3. 하나의 축을 공유하고 두개의 축을 가지는 그래프 그리기
df[['관측일수', '최대농도']].agg(['min', 'max'])

# 3_1. 년도별 관측 일수와 최대농도의 변화 흐름을 하나의 axes에 그리기
# x : 년도, y : 관측일수, 최대농도
plt.figure(figsize = (10, 3))

plt.plot(df['년도'], df['관측일수'], label = '관측일수')
plt.plot(df['년도'], df['최대농도'], label = '최대농도')

plt.title('년도별 관측 일수와 최대농도의 변화흐름')

plt.legend()
plt.show()

# 3_2. twnix()를 이용해서 x축은 같이 사용하고 y는 따로 사용하도록 처리
plt.figure(figsize = (15, 5))

ax1 = plt.gca() # 관측일수
ax2 = ax1.twinx() # ax1과 x축을 공유하는 새로운 subplot을 생성

ax1.plot(df['년도'], df['관측일수'], label = '관측일수', color = 'r')
ax2.plot(df['년도'], df['최대농도'], label = '최대농도', color = 'g')

ax1.set_title('년도에 따를 관측일수, 최대농도의 변화')
ax1.set_xlabel('년도')

ax1.set_ylabel('관측일수')
ax2.set_ylabel('최대농도')

ax1.legend(loc = 'upper left', bbox_to_anchor = (1.05, 1))
ax2.legend(loc = 'upper left', bbox_to_anchor = (1.05, 0.93))
plt.show()


# 4. legend 위치 지정
x = [1, 2, 3]
y = np.array([10, 20, 30])

plt.plot(x, y, label = 'plot1')
plt.plot(x, y+1, label = 'plot2')
plt.plot(x, y+2, label = 'plot3')
plt.plot(x, y+3, label = 'plot4')
plt.plot(x, y+4, label = 'plot5')
plt.plot(x, y+5, label = 'plot6')
plt.plot(x, y+6, label = 'plot7')
plt.plot(x, y+7, label = 'plot8')
plt.plot(x, y+8, label = 'plot9')
plt.plot(x, y+9, label = 'plot10')

plt.legend(bbox_to_anchor = (1, 1), loc = 'upper left',
           ncol = 3, shadow = True)
plt.show()



# 5. 산점도
x = range(1, 1001, 50)
y = range(1001, 1, -50)
y2 = range(1, 1001, 50)
print(len(x), len(y))

plt.scatter(x, y, marker = ',')
plt.scatter(x, y2, marker = '*', s = 60)

plt.legend(['A라벨', 'B라벨'])
plt.show()



# 6. 산점도 활용
df = pd.read_csv('data/diamonds.csv')
print(df.shape)
print(df.info())

# 캐럿(carat)과 가격(price)간의 상관관계 시각화
plt.figure(figsize=(10, 7))
plt.scatter(df['carat'], df['price'], alpha = 0.1) # x : 원인, y : 결과

plt.title('캐럿과 가격간의 상관관계')

plt.xlabel('캐럿')
plt.ylabel('가격')

plt.show()

# 상관계수 계산
print(df[['carat', 'price']].corr())
# 상관계수 (절대값 기준)
"""
- 1 ~ 0.7 : 아주 강한 상관관계
- 0.7 ~ 0.3 : 강한 상관관계
- 0.3 ~ 0.1 : 약한 상관관계
- 0.1 ~ 0 : 관계없다
"""



# 7. 막대그래프
fruits = ['사과', '배', '귤']
counts = [150, 70, 200]

plt.figure(figsize = (16, 5))
plt.subplot(1, 2, 1)
plt.bar(fruits, counts, width = 0.6) # width : 막대의 두께 : 0 ~ 1

# plt.text(x좌표, y좌표, '출력할 텍스트')
for x, y in enumerate(counts):
    plt.text(x - 0.02, y, str(y))
    
plt.title('과일 개수')
plt.xlabel('과일')
plt.ylabel('수량')

# y축의 값의 범위를 변경
plt.ylim(0, 250)
plt.grid(True, linestyle = ':')

plt.subplot(1, 2, 2)
plt.barh(fruits, counts, height = 0.5) # height : 막대의 두께

plt.title('과일 개수') # subplot(axes)의 title을 설정
plt.xlabel('수량')
plt.ylabel('과일')

plt.xlim(0, 250) # x축의 값의 범위를 지정

plt.suptitle('막대그래프', fontsize = 20) # figure의 title을 설정
plt.grid(True, linestyle = ':')
plt.tight_layout()
plt.show()


# 8. 막대 그래프 활용
df = pd.read_excel('data/강수량.xlsx', engine = 'openpyxl')

df.set_index('계절', inplace = True)

# 8_1. 2009년 계절별 강수량을 막대그래프로 비교
plt.bar(df.index, df[2009])
plt.title('2009년 계절별 강수량')

# 막대에 강수량을 출력
for x, y in enumerate(df[2009]):
    plt.text(x - 0.1, y + 5, str(y))

plt.ylim(0, 850)

plt.ylabel('강수량')
plt.xlabel('계절')
plt.show()


# 8_2. 여름 년도별 강수량의 변화 => 주관심사 : 변화 흐름 => line plot
plt.figure(figsize = (10, 4))

plt.plot(df.columns, df.loc['여름'], color = 'r')
plt.bar(df.columns, df.loc['여름'])

for x, y in zip(df.columns, df.loc['여름']):
    plt.text(x - 0.2, y + 10, str(y))
    
plt.ylim(0, 1200)

plt.show()

print(df.index) # x
print(df[2010], df[2011]) # y
print(len(df.index))


# 8_3. 2010, 2011 년도 계절별 강수량을 확인 => 누적 막대 그래프
width = 0.3
x = np.arange(len(df.index))

plt.bar(x - width/2, df[2010], width = width, label = '2010')
plt.bar(x + width/2, df[2011], width = width, label = '2011')

plt.xticks(x, labels = df.index) # x: 눈금의 위치값. label : 눈금 라벨

plt.legend()
plt.show()


# 8_4. 2010, 2011, 2012 년도 계절별 강수량 확인
df[[2010, 2011, 2012]].plot(kind = 'bar', width = 0.8) # 굵기 변경가능
plt.show()