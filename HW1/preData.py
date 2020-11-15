import random
import numpy as np

def read_txt(file):
    f=open(file, "r")
    if(file[-3:] == 'txt'):
        contents =f.readlines()

        dataset = np.zeros((len(contents)-2,len(contents[2].split('\t'))-1))
        label = np.zeros((len(contents)-2))

        for i in range(len(contents)-2):
            x = contents[i+2].split("\t")
            for j in range(len(x)):
                if j != len(x) - 1 :
                    dataset[i][j] = float(x[j])
                else :
                    label[i] = float(x[j][:-1])
    else :
        contents =f.readlines()
        n_data = int(len(contents)/3)
        dataset = np.zeros((n_data,2))
        label = np.zeros((n_data,2))
        j = 0
        count = 0
        for i in range(len(contents)):
            if(j == 1):
                dataset[count][0] = float(contents[i].split()[0])
                dataset[count][1] = float(contents[i].split()[1])
            if(j == 2):
                label[count][0] = int(contents[i].split()[0])
                label[count][1] = int(contents[i].split()[1])
                count = count + 1
                j = -1
            j += 1
            
    return dataset,label

def norm(data_in):
    data = data_in.copy()
    datanorm = (data - data.min())/(data.max() - data.min())

    return datanorm

def data_cross(data, label, epoch):
    data_train = []
    data_test = []
    data_temp = []

    for i in range(len(data)):
        if(i%10 != epoch%10):
            data_temp = []
            data_temp.append(data[i])
            data_temp.append(label[i])
            data_train.append(data_temp)
        else:
            data_temp = []
            data_temp.append(data[i])
            data_temp.append(label[i])
            data_test.append(data_temp)

    random.shuffle(data_train)
    random.shuffle(data_test)
    
    data_trainn = []
    label_train = []
    data_testt = []
    label_test = []

    for i in range(len(data_train)):
        data_trainn.append(data_train[i][0])
        label_train.append(data_train[i][1])

    for i in range(len(data_test)):
        data_testt.append(data_test[i][0])
        label_test.append(data_test[i][1])

    return data_trainn, label_train, data_testt, label_test