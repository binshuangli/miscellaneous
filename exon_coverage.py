import pandas as pd
import numpy as np
depth=pd.read_csv("~/Desktop/GL349647_exons_locations.txt",sep="\t",header=None,names=['scaffold','location','depth'])
exon=pd.read_csv('~/Desktop/GL349647.WM.depth.xls',sep="\t",header=None,names=['scaffold','start','end'])
avg=np.zeros(len(exon))


for i in range(0,len(exon)):
    avg[i]=np.mean(depth[(depth['scaffold']==exon['scaffold'][i])&(depth['location']>=exon['start'][i])&(depth['location']<=exon['end'][i])]['depth'])
exon['average_depth']=avg
exon.to_csv("GL349647.WM_exon_avg_depth.csv¡±) 


'''

#print np.mean(depth.ix[depth[depth['scaffold']==exon['scaffold'][1]]['location'][exon['start'][1]:exon['end'][1]+1]]['depth'])
#print depth.ix[depth[depth['scaffold']==exon['scaffold'][1]]['location']>=exon['start'][1])&(depth[depth['scaffold']==exon['scaffold'][1]]['location']<=exon['end'][1]]
#print depth.ix[depth[depth['scaffold']==exon['scaffold'][2]]['location'][exon['start'][2]:exon['end'][2]+1]]['depth']
#print depth
#print exon
print depth[(depth['scaffold']==exon['scaffold'][1])&(depth['location']>=exon['start'][1])&(depth['location']<=exon['end'][1])]
'''