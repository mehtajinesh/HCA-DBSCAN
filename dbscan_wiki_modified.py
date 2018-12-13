import scipy.spatial as spatial
import numpy as np
import time
import sys
import decimal
import matplotlib.pyplot as plt
import pylab
import math
from itertools import product
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
start_time = time.time()
def dbscan(d,eps,min_pts):
    clusters,neighbour_pts,noise=[],[],[]
    points = np.array(d.keys())
    point_tree = spatial.cKDTree(points)
    for p in d.keys():
        if d[p]==1:
            #bitwise operator can be used if visited
            continue
        d[p]=1
        neighbour_pts=list(map(tuple,point_tree.data[point_tree.query_ball_point(p,eps)]))
        if len(neighbour_pts)<min_pts:
            noise.append(p)
        else:
            c=[]
            c=exp_cluster(p,neighbour_pts,c,eps,min_pts,d,clusters,point_tree)
            clusters.append(c)
    print("--- %s seconds in dbscan---" % (time.time() - start_time))
    print ([len(i) for i in clusters])
    res=merge_cluster(clusters,eps)
            
def exp_cluster(pt,nghbr_pts,cluster,eps,min_pts,data,c,point_tree):
    cluster.append(pt)
    for p in nghbr_pts:
        if data[p]==0:
            #same as above scenrio
            data[p]=1
            temp_nghbr_pts=list(map(tuple,point_tree.data[point_tree.query_ball_point(p,eps)]))
            if len(temp_nghbr_pts)>= min_pts:
                nghbr_pts.extend(temp_nghbr_pts)
            if p not in [j for i in c for j in i]:
                cluster.append(p)
    print("--- %s seconds in exp_cluster---" % (time.time() - start_time))
    return cluster

def merge_cluster(clusters,eps):
    p=False
    i=0
    while(i<len(clusters)-1):
        j=i+1
        while(j<len(clusters)):
            
            temp=np.array(clusters[i])
            temp_tree=spatial.cKDTree(temp)
            z=temp_tree.query(clusters[j],distance_upper_bound=eps)
            if(not np.all(np.isinf(z[0]))):
                clusters[i].extend(clusters[j])
                del clusters[j]
                p=True
                break
            j=j+1
            if(p):
                break
        i=i+1
    if(p):
        return merge_cluster(clusters,eps)
    return clusters
        
#open the dataset
file_name="spherical_6_2_modified.csv"
i=open(file_name)
lines=i.read().strip().split('\n')
i.close()
#initialize the list in which your dataset will be stored in the form of list
dataset={}
coord=[]
dim_size=2#int(sys.argv[1])
epsilon=1.8#float(sys.argv[2])
min_points=4.0#float(sys.argv[3])
for i in range(dim_size):
    coord.append([])
for i in lines:
    line=i.rstrip().split(',')
    temp=[]
    #extract x and y coordinates
    for j in line:
        temp.append(j.strip())
    print temp
    #convert to float if the input is not numeric type
    for i in range(dim_size):
        temp[i]=float(temp[i])

        coord[i].append(temp[i])
    #can't use list as keys so converting to tuple
    temp=tuple(temp)
    print len(dataset)
    #default not visited that's why 0
    dataset[temp]=0
print len(dataset)
length_input=len(dataset)
dbscan(dataset,epsilon,min_points)
print("--- %s seconds ---" % (time.time() - start_time))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(coord[0], coord[1], cmap=plt.hot())
plt.show()
