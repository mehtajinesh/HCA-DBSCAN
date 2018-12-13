import math
import numpy
import random
import time
start_time = time.time()
def distance(center,inp,length,dim_size):
    d=[]
    j=0
    while(j<length):
        #using euclidian distance
        total=0
        for i in range(dim_size):
            total=total+math.pow((center[i]-inp[j][i]),2)           
        temp=round(math.sqrt(total),2)
        d.append(temp)
        j=j+1
    return d

def core(point,distance_matrix,epsilon,min_points):
    count=0
    for i in range(len(distance_matrix)):
        if distance_matrix[point][i]<=epsilon:
            count=count+1
        else:
            pass
    if count>=min_points:
        return True
    else:
        return False

def expand(dis_matrix,point,p,threshold,m):
    temp=dis_matrix[numpy.ix_([point])]
    for i in range(p):
        if(temp.item(i)<=threshold):
            cluster.append(i)
            if core(i,dis_matrix,threshold,m):
                expand(dis_matrix,i,p,threshold,m)
                    
#open the dataset
file_name="/media/jineshmehta/4A10880E10880365/Python27/iris (copy).txt"
i=open(file_name)
lines=i.read().strip().split('\n')
i.close()
#initialize the list in which your dataset will be stored in the form of list
dataset=[]
dim_size=int(input("enter the dim_size:"))
for i in lines:
    line=i.rstrip().split(' ')
    temp=[]
    #extract x and y coordinates
    for j in line:
        temp.append(j.strip())
    print temp
    #convert to float if the input is not numeric type
    for i in range(dim_size):
        temp[i]=float(temp[i])
    dataset.append(temp)
print dataset
    
'''length_input=len(dataset)
distance_matrix=[]
for c in dataset:
    #pass each point into distance function to get the distance in variable 'd' and append it to distance matrix
    d=distance(c,dataset,length_input,dim_size)
    distance_matrix.append(d)
print distance_matrix
epsilon=float(input("enter the epsilon value:"))
min_points=float(input("enter the min. points:"))
cluster=[]
point=0
for i in range(length_input):
    if(core(point,distance_matrix,epsilon,min_points)):
        print point,"is core point."
    else:
        print point,"is not core point."'''
'''not core i.e. either outlier or boundary'''
'''point=point+1'''
