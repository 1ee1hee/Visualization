# 실습 
# 1. 막대그래프
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1_1.
s = pd.Series([100, 70, 90, 130, 50], index = ['사과', '배', '귤', '수박', '복숭아'])
s.plot(kind = 'bar', title = '과일 수량', xlabel = '과일종류', ylabel = '개수', figsize = (6, 5), rot = 45)
plt.show()