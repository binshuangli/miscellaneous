import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

distance=pd.read_csv("sorted_gene_locations.txt",sep="\t",header=None,names=['scaffold','feature','start','end'])
dis=np.zeros(len(distance))
for i in range(1,len(distance)):
    if (distance['scaffold'][i]==distance['scaffold'][i-1]):
        dis[i]=distance['start'][i]-distance['end'][i-1]
    else:
        dis[i]=0
distance['distance']=dis
pos_dis= distance[distance['distance']>0]
print "Mean: " , pos_dis['distance'].mean()
print "Median: " ,pos_dis['distance'].median()
print "Standard deviation: ",pos_dis['distance'].std()
print "Max distance: ",pos_dis['distance'].max()
print "Min distance: " ,pos_dis['distance'].min()
#print pos_dis['distance']
#pos_dis.to_csv("gene_distance.csv")