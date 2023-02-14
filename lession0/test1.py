import numpy as np
import json

def load_data():
    datafile = './work/housing.data'
    data = np.fromfile(datafile, sep=' ')

    print(data.shape)

    feature_names = [ 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE','DIS', 
                    'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV' ]

    feature_num = len(feature_names)

    data = data.reshape([data.shape[0] // feature_num, feature_num])

    print(data.shape[0])

    print(data)


    ratio = 0.8

    offset = int(data.shape[0] * ratio)

    training_data = data[:offset]

    maximums, minimums, avgs = training_data.max(axis = 0), training_data.min(axis = 0), training_data.sum(axis = 0) / training_data.shape[0]


    for i in range(feature_num):
        # print("输出一行", maximums, minimums, maximums[i], minimums[i], "\n")
        print("输出data", data[:, i], (data[:, i] - minimums[i]), (maximums[i] - minimums[i]))
        data[:, i] = (data[:, i] - minimums[i]) / (maximums[i] - minimums[i])
        print(data[:, i])
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data, test_data
