#pip3 install mariadb SQLAlchemy
#pip3 install numpy
#pip3 install pandas
#pip3 install matplotlib

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from data_insert import getTrainData, getTestData

#9.  train_target, train_length, train_weight 형태로 pandas에 저장한 뒤 MariaDB로 저장한다.
#- 테이블명 train
#10. test_target, test_length, test_weight 형태로 pandas에 저장한 뒤 MariaDB로 저장한다.
#- 테이블명 test

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")

def insertTrain():
    fishs = getTrainData()
    fishs.to_sql("train",engine,index=False,if_exists="replace")

def insertTest():
    fishs = getTestData()
    fishs.to_sql("test",engine,index=False,if_exists="replace")

insertTrain()
insertTest()