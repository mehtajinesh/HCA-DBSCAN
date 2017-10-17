'''
Created by Jinesh Mehta

File Name :Initialization.py

Function : Creating hypercube points and initialize the neighbouring points for every box in the hypercube

Input Parameters: Epsilon eps

Return Values : HypercubeDict ( A dict which will have hypercube coordinates as key and its updated neighbouring poisition details.)'''
import Db
import math

def generate_hypercube(eps):

    eps_sqrt_2 = eps/round(math.sqrt(2),2)
    dataset = Db.Database()
    #for storing the min and max value in each axis
    dataset.load_data()
    pt_data = dataset.data
    #axis_end_points = [];#create list for storing min and max for each direction
    #note: the dimension does not start from 1 but it starts from 0 as pt_data[0] represents the 1st dimension
    min_value=map(min, zip(*pt_data))
    max_value=map(max, zip(*pt_data))
    for i in range(dataset.dimension):
        #required to store the boundary points
        '''current_axis_endpoints = []
        current_axis_endpoints.append((min(pt_data[i]),max(pt_data[i])))
        axis_end_points.append(current_axis_endpoints)'''
        #calculate the length of each axis and round the axis band in order to make the each band equal to eps/sqrt(2)
        axis_length=max_value[i]-min_value[i]
        axis_bands = axis_length/(eps_sqrt_2)
        number_of_bands = int(math.ceil(axis_bands))
        #generate the bands in each direction
        band = []
        for j in range(0, number_of_bands):
            band.append(round(min_value[i]+(j*(eps_sqrt_2)),2))
        dataset.bands[i]=band
    print(dataset.bands)
generate_hypercube(eps=2.82)
