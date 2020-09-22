import preData
import numpy
import random

from preData import data_cross

data, label = preData.read_txt("./HW1/Flood_dataset.txt")
# dataset, label = readTXT.read_txt("./HW1/cross.pat")
data_norm = preData.norm(data)
label_norm = preData.norm(label)
data_train, label_train, data_test, label_test = preData.data_cross(data_norm, label_norm,0)
print(data_train[0])
print(label_train[0])
# for i in range(10):
#     print(label_norm[i])