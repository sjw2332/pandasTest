import numpy as np
from numpy.core.fromnumeric import reshape
import pandas as pd
from matplotlib import pyplot as plt
import data.fish_api as f



#훈련 데이터를 x축은 length, y축은 weight로 하여 matplot으로 시각화한다.
plt.scatter(f.train_input[:,0], f.train_input[:,1])
plt.scatter(f.test_input[:,0], f.test_input[:,1])

plt.xlabel("length")
plt.ylabel("weight")
plt.show()
