import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.preprocessing import normalize

def generate_file_names():
    file_list = []
    for activities in range(19):
        for person in range(8):
            for segments in range(60):
                file_list.append('../data/' +
                                 'a' + str(activities + 1).zfill(2) + '/'
                                 'p' + str(person + 1) + '/'
                                 's' + str(segments + 1).zfill(2) + '.txt'
                                )

    return file_list

def extract_features(x):
    numrows = len(x)
    mean = np.mean(x, axis = 0)
    std = np.std(x, axis = 0)
    var = np.var(x, axis = 0)
    median = np.median(x, axis = 0)
    xmax = np.amax(x, axis = 0)
    xmin = np.amin(x, axis = 0)
    p2p = xmax - xmin
    amp = xmax - mean
    s2e = x[numrows-1,:] - x[0,:]
    features = np.concatenate([mean, std, var, median, xmax, xmin, p2p, amp, s2e])
    return features

def data_generate():
    filenames = generate_file_names()
    feature_cols = []
    for unit_label in ['T', 'RA', 'LA', 'RL', 'LL']:
        for feature in ['mean', 'std', 'var', 'median', 'xmax', 'xmin', 'p2p', 'amp', 's2e']:
            for sensor  in ['acc', 'gyro', 'mag']:
                for position in ['X', 'Y', 'Z']:
                    feature_cols.append(feature + '_' + unit_label + '_' + position + sensor)
    activity_data = pd.DataFrame(columns=feature_cols)
    data = []
    activity = []
    person = []
    for i in range(len(filenames)):
        activity.append('a' + str(i // 480 + 1).zfill(2))
        person.append('p' + str((i // 60) % 8 + 1))
        raw_data = np.genfromtxt(filenames[i], delimiter = ',', skip_header = 0)
        row = extract_features(raw_data)
        data.append(row)
    #data = scale(data, axis = 0)
    activity_data = pd.DataFrame(data, columns = feature_cols)
    activity_data['person'] = person
    activity_data['activity'] = activity
    return activity_data

data_generate()

