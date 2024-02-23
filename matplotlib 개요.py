# 실습

# 1. pyplot 모듈을 이용해 그리기
x = [1, 2, 3, 4, 5]
y = range(10, 60, 10)

# import 
import matplotlib.pyplot as plt

# figure의 크기를 설정 (가장 먼저)
plt.figure(figsize=(10,7)) # (가로, 세로) - 단위 : inch

# 그래프 그리기
plt.plot(x, y)

# 설정
plt.title('선 그래프 예제', fontsize = 20)
plt.xlabel('X축 값')
plt.ylabel('Y축 값')
plt.grid(True, linestyle = ':')

# 저장
plt.savefig('sample.png')
# 화면에 출력
plt.show()



# 2. 하나의 figure에 여러 그래프 그리기
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1) # figure를 2행 3열로 나누고 그 중 첫번째 것
# 그래프 그리기
plt.plot(x, y)
# 설정하기
plt.title('첫번째 그래프')

plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.title('두번째 그래프')

plt.subplot(2, 3, 3)
plt.bar(x, y)
plt.title('세번째 그래프')

plt.subplot(2, 3, 4)
plt.pie(x)
plt.title('네번째 그래프')

plt.subplot(2, 3, 5)
plt.pie(y)
plt.title('다섯째 그래프')

plt.subplot(2, 3, 6)
plt.boxplot(x)
plt.title('여섯째 그래프')

plt.tight_layout()
plt.show()



# 3. 그래프를 그릴 subplot을 설정
plt.subplot(1, 2, 1) # figure를 2행 3열로 나누고 그 중 첫번째 것
# 그래프 그리기
plt.plot(x, y)
# 설정하기
plt.title('첫번째 그래프')

plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title('두번째 그래프')

plt.subplot(2, 2, 4)
plt.bar(x, y)
plt.title('세번째 그래프')

plt.tight_layout()
plt.show()



# 4. 범례가 나오도록 처리
plt.plot(x, y, label = 'plot1')
plt.scatter(x, y, label = 'plot2')
plt.plot(y, x, label = 'plot3')

plt.legend() # 범례
plt.grid(True)
plt.show()



# 5. Figure에 하나의 axes 그리기
# plt.gca() 사용
axes = plt.gca()
# axes 객체의 메소드를 이용해 그래프 그리고 설정하기
axes.plot(x, y, label = 'line plot')
axes.scatter(x, y, label = 'scatter')
# 설정함수 - set_xxxx()
axes.set_title('제목')
axes.set_xlabel('X축')
axes.set_ylabel('Y축')
axes.grid(True)
axes.legend()

plt.show()



# 6. 하나의 Figure에 여러개의 axes 그리기
# figure.add_subplot()메소드 이용
# figure 객체 조회
fig = plt.figure(figsize = (10, 5))

# figure에 axes를 추가
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

ax1.plot(x, y)
ax2.plot(x, y)
ax3.scatter(x, y)

ax1.grid(True)
ax3.grid(True)

plt.tight_layout()
plt.show()