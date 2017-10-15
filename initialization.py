'''
Created by Jinesh Mehta

File Name :Initialization.py

Function : Creating hypercube points and initialize the neighbouring points for every box in the hypercube

Input Parameters: Epsilon eps

Return Values : HypercubeDict ( A dict which will have hypercube coordinates as key and its updated neighbouring poisition details.)'''
import Database
def generate_hypercube(eps):
    dataset = Database()
    #for storing the min and max value in each axis
    pt_data = dataset.data
    axis_end_points = [];#create list for storing min and max for each direction
    #note: the dimension does not start from 1 but it starts from 0 as pt_data[0] represents the 1st dimension
    for i in range(0,len(dataset.dim)):
        #required to store the boundary points
        '''current_axis_endpoints = []
        current_axis_endpoints.append((min(pt_data[i]),max(pt_data[i])))
        axis_end_points.append(current_axis_endpoints)'''
        #calculate the length of each axis and round the axis band in order to make the each band equal to eps/sqrt(2)
        axis_length=max(pt_data[i])-min(pt_data[i])
        axis_bands = axis_length/(eps/pow(2,1/2))
        number_of_bands = round(axis_bands,0)
        #generate the bands in each direction
        band = []
        for j in range(0, number_of_bands):
            band.append(min(pt_data[i])+(j*(eps/pow(2,1/2))))
            dataset.bands[i]=band
        #create hypercube coordinates using respective bands in each direction
        for j in range(i+1,len(dataset.dim):
