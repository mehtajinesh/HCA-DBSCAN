import scipy.spatial as spatial
import numpy as np
import time
import sys
start_time = time.time()
def dbscan(d,eps,min_pts):
    clusters=[]
    neighbour_pts=[]
    noise=[]
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

                
def FindRegion(point,eps,d):
    other_dis_from_point={}
    for b in d.keys():
        dst = distance.euclidean(point,b)
        other_dis_from_point[b]=dst
    for k in other_dis_from_point.keys():
        if other_dis_from_point[k]>eps:
            del other_dis_from_point[k]
    print("--- %s seconds in findregion ---" % (time.time() - start_time))
    return other_dis_from_point.keys()
            
    
#open the dataset
file_name="/media/jineshmehta/4A10880E10880365/Python27/iris (copy).txt"
i=open(file_name)
lines=i.read().strip().split('\n')
i.close()
#initialize the list in which your dataset will be stored in the form of list
dataset={}
dim_size=int(sys.argv[1])
epsilon=float(sys.argv[2])
min_points=float(sys.argv[3])
for i in lines:
    line=i.rstrip().split(' ')
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
