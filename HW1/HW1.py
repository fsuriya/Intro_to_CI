import preData

def preProcess(dataSelect):
    if(dataSelect == 1):
        dataset, label = preData.read_txt("./HW1/Flood_dataset.txt")
    elif(dataSelect == 2):
        dataset, label = preData.read_txt("./HW1/cross.pat")
    data_norm = preData.norm(dataset)
    label_norm = preData.norm(label)

    return data_norm, label_norm

def feedforward():
    return 0

def MLP():
    return 0

########################### Main ###########################
layer = 1
maxNode = 15
epoch = 1000
MLP(1, layer, maxNode, epoch)

data_norm, label_norm = preProcess(1)


data_train, label_train, data_test, label_test = preData.data_cross(data_norm, label_norm,0)

