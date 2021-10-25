#1. 파이썬 pip를 활용하여 numpy와 pandas 라이브러리를 설치한다.
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import data.fish_api as f

#3. 로드한 도미와 빙어 데이터를 x축은 length, y축은 weight로 하여 matplot으로 시각화한다.
plt.scatter(f.bream_length, f.bream_weight)
plt.scatter(f.smelt_length,f.smelt_weight)
plt.xlabel("length")
plt.ylabel("weight")
plt.show()