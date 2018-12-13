import csv
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
file = open("iris_data.csv",'r')
lines = csv.reader(file,delimiter='\n')
values =[]
labels=[]
for row_str in lines:
    entry=[]
    row_str = row_str[0].split(',')
    row=[]
    for r in row_str[:-1]:
        row.append(float(r))
    values.append(row)
    labels.append(row_str[-1])




# #############################################################################
# Generate sample data

# #############################################################################
# Compute DBSCAN
eps_range=[]
for i in range(1,50):
    eps_range.append(i*0.1)
for eps in eps_range:
    for min_pts in range(0,10):
        X = np.array(values)
        db = DBSCAN(eps=eps, min_samples=min_pts).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        label = db.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(label)) - (1 if -1 in label else 0)

        
        if(n_clusters_ == 4):
            print('Estimated number of clusters: %d' % n_clusters_)
            print("Eps value :"+str(eps)+" min_pts: "+str(min_pts))
# #############################################################################
# Plot result
'''import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(label)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (label == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
'''
