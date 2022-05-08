import os
import pandas as pd
import numpy as np
def file_name(file_dir):
    filelist = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filelist.append(root+file)
    return filelist
def isDelete(filename, loc):
    for i in range(loc.shape[0]):
        if(loc[i,1] == filename):
            if(loc[i,0] < 99):
                return True
            else:
                return False
    print(filename + "error")
    return False;


filelist = file_name("../Img/")
print(filelist)
loc = pd.read_csv("../data/data.csv")
loc = np.array(loc)
for i in range(len(filelist)):
    if not isDelete(filelist[i].split(os.path.sep)[-1], loc):
        print(filelist[i])
        os.remove(filelist[i])



