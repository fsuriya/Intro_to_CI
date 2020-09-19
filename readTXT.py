import numpy as np

# dataset, label = read_txt("./HW1/Flood_dataset.txt")
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

dataset, label = read_txt("./HW1/cross.pat")

print(dataset[0])
print()
print(label[0])