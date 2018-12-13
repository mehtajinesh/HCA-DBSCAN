import scipy.spatial as spatial
from scipy.spatial import distance
import numpy as np
import time
import sys
start_time = time.time()
def dbscan(d,eps,min_pts):
    clusters,neighbour_pts,noise=[],[],[]
    points = np.array(d.keys())
    point_tree = spatial.cKDTree(points)
    for p in d.keys():
        if d[p]==1:
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
    print len(clusters)
    res=merge_cluster(clusters,eps)
            
def exp_cluster(pt,nghbr_pts,cluster,eps,min_pts,data,c,point_tree):
    cluster.append(pt)
    for p in nghbr_pts:
        if data[p]==0:
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
            l1=np.asarray(clusters[i])
            c1=np.mean(l1)
            print c1
            l2=np.asarray(clusters[j])
            c2=np.mean(l2)
            print c2
            if distance.euclidean(c1,c2) <= (3*eps):
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
file_name="soybean-small - soybean-small.csv"
i=open(file_name)
lines=i.read().strip().split('\n')
i.close()
#initialize the list in which your dataset will be stored in the form of list
dataset={}
dim_size=int(sys.argv[1])
epsilon=float(sys.argv[2])
min_points=float(sys.argv[3])
for i in lines:
    line=i.rstrip().split(',')
    temp=[]
    #extract x and y coordinates
    for j in line:
        temp.append(j.strip())
    #print temp
    #convert to float if the input is not numeric type
    for i in range(dim_size):
        temp[i]=float(temp[i])
    #can't use list as keys so converting to tuple
    temp=tuple(temp)
    #default not visited that's why 0
    dataset[temp]=0
length_input=len(dataset)
dbscan(dataset,epsilon,min_points)
print("--- %s seconds ---" % (time.time() - start_time))
