import os
import pandas as pd
import numpy as np
from ImageFog.AHE import *
from ImageFog.MinChannel import *
from ImageFog.SSR import *
def file_name(file_dir):
    filelist = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filelist.append(root+file)
    return filelist



filelist = file_name("./data/data_beta_0.1/1/")
sum = 0;
for i in range(len(filelist)):
    sum = sum + M_SSR(filelist[i])
    print(sum)
