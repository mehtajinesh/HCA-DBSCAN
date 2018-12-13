# HCA-DBSCAN
Hypercube Accelerated DBSCAN

Density based clustering has proven to be very efficient and has found numerous applications across domains. The
Density-Based Spatial Clustering of Applications with Noise (DBSCAN) algorithm is capable of finding clusters of varied shapes and is
not sensitive to outliers in the data. In this paper we propose a new clustering algorithm, the HyperCube based Accelerated
DBSCAN(HCA-DBSCAN) which runs in O(n log(n)) time for lower dimensions and O(n3=2) time for higer dimensions bettering the
O(n2) complexity of the original DBSCAN algorithm without compromising on clustering accuracy. We use a combination of distance
based aggregation by overlaying the data with customized grids and use representative points to reduce the number of comparisons.
Experimental results show that the proposed algorithm achieves a significant run time speed up of upto 58.27% when compared to
other improvements that try to reduce the complexity of DBSCAN.
