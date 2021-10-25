import numpy as np
import pandas as pd
import sqlalchemy as db
from data.fish_api import test_input, train_target, test_target, train_input

# print(f.test_input)
# print(f.test_input[:,0])  #test_input_length
# print(f.test_input[:,1])  #test_input_weight

def getTrainData():
    train_length = np.ndarray.flatten(train_input[:,0])
    #print(arr1)
    train_weight = np.ndarray.flatten(train_input[:,1])
    #print(arr2)
    train_fishs = np.column_stack((train_target,train_length, train_weight))
    #print(fishs)
    train_dataFrame = pd.DataFrame(train_fishs, columns=[ "target","train_length", "train_weight"])
    #print(train_dataFrame)
    return train_dataFrame


def getTestData():
    test_length = np.ndarray.flatten(test_input[:,0])
    #print(arr1)
    test_weight = np.ndarray.flatten(test_input[:,1])
    #print(arr2)
    test_fishs = np.column_stack(( test_target, test_length, test_weight))
    #print(fishs)
    test_dataFrame = pd.DataFrame(test_fishs, columns=["target","test_length", "test_weight"])
    #print(test_dataFrame)
    return test_dataFrame

