import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.preprocessing import normalize
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder
from sklearn.semi_supervised import LabelPropagation

# Read data and get x y values
data = pd.read_csv('../data.csv')
x = data.iloc[:, 1:406]
y = data.iloc[:, -1].values

ohe = LabelEncoder()
y = ohe.fit_transform(y)

lp = LabelPropagation()

unlabelled_percentage = [90, 80, 70, 60, 50]
accuracies = []
labelled_percentage = []

for i in ul:
    unlab = i/100
    total_act = y.shape[0]/19
    remove = (unlab * y.shape[0])/19
    lab = total_act-remove
    
    for a in range(19):
        ac1 = a * total_act
        ac2 = (a+1) * total_act
        s = int(lab + ac1)
        e = int(ac2)
    
        labels = y
        
        labels[s:e] = -1
    
    
    lp.fit(x, labels)   
    print('For ', i, '% unlabelled score is ', lp.score(x, y))
    accuracies.append(lp.score(x, y))
    labelled_percentage.append(1 - unlab)

