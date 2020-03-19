from collections import Counter
from typing import NamedTuple
import numpy as np
import math as m
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt
import random
import typing


def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, winners_count = votes.most_common(1)[0]
    num_winners = len([count for count in votes.values() if count == winners_count])
    if num_winners == 1:
        return winner
    else:
        return raw_majority_vote(labels[:-1])
    return winner

def distance (row, w):
    v = np.array(row[0:4])
    w = np.array(w[0:4])
    u = np.subtract(v, w)
    distance = np.sqrt(np.dot(u, u))
    return distance

def split_data(df_iris, rlt):
    length_test = rlt * (df_iris.size/7)
    length_test = int(length_test)
    df_iris_train = df_iris.loc[:length_test, :]
    df_iris_test = df_iris.loc[length_test + 1:, :]
    return df_iris_train, df_iris_test

def knn_classify(k, labeled_points, new_point):
    # Sortiere die annotierten Punkte aufsteigend nach Distanz
    new_point = list(new_point)
    labeled_points['distance'] = labeled_points.apply(distance, axis=1, args=[new_point])
    labeled_points_sorted = labeled_points.sort_values(['distance'])

    # Finde die Annotation der k nächsten Punkte
    k_nearest_labels = [label for label in labeled_points_sorted.iloc[:k, 4]]
    # Und lasse sie abstimmen
    return raw_majority_vote(k_nearest_labels)

# 
data = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

with open('iris.csv', 'w') as f:
    f.write(data.text)

df_iris = pd.read_csv('iris.csv', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
df_iris.loc[:, 'class'] = df_iris.loc[:, 'class'].str.replace(r'Iris-', '')

metrics = list(df_iris.columns)
pairs = []
markers = {'setosa' : '+', 'versicolor' : 'x', 'virginica' : 'o'}

# fig, ax = plt.subplots(4, 4)

# for i in range(3):
#     for j in range(i+1, 4):
#         for key in markers:
#             ax[i][j].scatter(df_iris.loc[df_iris['class'] == key, metrics[i]], \
#                 df_iris.loc[df_iris['class'] == key, metrics[j]], marker = markers[key])


# plt.show()

random.seed(12)
df_iris = df_iris.sample(frac = 1).reset_index(drop=True)
df_iris['predicted'] = np.nan
df_iris['distance'] = np.nan
df_iris_train, df_iris_test = split_data(df_iris, 0.7)
print(df_iris_test)
print(df_iris_train)

for index, row in df_iris_test.iterrows():
    predicted = knn_classify(5, df_iris_train, row.values)
    actual = row['class']
    if predicted != actual:
        print(f'predicted: {predicted}\tactual:{actual}')