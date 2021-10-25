import numpy as np
import pandas as pd


#2. 파이썬을 활용하여 fish csv 파일을 로드한다.
bream_length = pd.read_csv('C:/workspace/pythonwork/pandas_test/data/bream_length.csv',delimiter='\t',header=None)
bream_length = bream_length.to_numpy()
bream_weight = pd.read_csv('C:/workspace/pythonwork/pandas_test/data/bream_weight.csv',delimiter='\t',header=None)
bream_weight = bream_weight.to_numpy()
smelt_length = pd.read_csv('C:/workspace/pythonwork/pandas_test/data/smelt_length.csv',delimiter='\t',header=None)
smelt_length = smelt_length.to_numpy()
smelt_weight = pd.read_csv('C:/workspace/pythonwork/pandas_test/data/smelt_weight.csv',delimiter='\t',header=None)
smelt_weight = smelt_weight.to_numpy()



#4. 도미와 빙어 데이터를 1차원 배열 length, weight로 합친 뒤 2차원 배열로 만들고 shape을 확인할 수 있다.
bream = np.hstack((bream_length,bream_weight))
#print(bream.shape)
smelt = np.hstack((smelt_length,smelt_weight))
#print(smelt.shape)
fish_data = np.concatenate((bream,smelt))
#print(fish_data)


#5. 도미와 빙어를 구분할 수 있게 도미를 찾는 타겟 데이터를 만든다.
#  도미 – 1, 빙어 – 0 으로 구분!!

fish_target =  np.concatenate((np.ones(35),np.zeros(14)))



# 6. shuffle을 이용하여 데이터를 섞는다.
np.random.seed(10)
np.random.shuffle(fish_data)
np.random.seed(10)
np.random.shuffle(fish_target)

index = np.arange(49)
np.random.seed(10)
np.random.shuffle(index)

#7. 테스트 데이터와 훈련 데이터로 구분한다. 
train_input = fish_data[index[:25]]
train_target = fish_target[index[:25]]

test_input = fish_data[index[25:]]
test_target = fish_target[index[25:]]


