class Database:
    def __init__(self,dimension_size=4,minimum_points=3):
        self.data=[]
        self.dimension=dimension_size
        self.min_points=minimum_points
        self.bands=[]
    def euclidean(x, y):
        sumSq = 0.0
        # add up the squared differences
        for i in range(len(x)):
            sumSq += (x[i] - y[i]) ** 2
        # take the square root of the result
        return sumSq ** 0.5

    def load_data(self):
        filepath = open("C:\\Users\\Jinesh\\Downloads\\iris_data.csv")
        lines = filepath.read().strip().split('\n')
        filepath.close()
        for i in range(self.dimension):
            self.bands.append([])
        print(self.bands)
        for i in lines:
            line = i.rstrip().split(',')
            # convert to float if the input is not numeric type
            for i in range(self.dimension):
                line[i] = round(float(line[i]))
            self.data.append(tuple(line))
        self.data.sort(key=lambda x: x[0])#sorting the list using x axis
        print(self.data)
        return
