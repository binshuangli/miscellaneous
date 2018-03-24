import pandas as pd
import numpy as np
depth=pd.read_csv("GL349773_exons_locations.txt",sep="\t",header=None,names=['scaffold','location','depth'])
exon=pd.read_csv('bt_GL349773.WLM_mapped.sorted.depth.xls',sep="\t",header=None,names=['scaffold','start','end'])
avg=np.zeros(len(exon))


for i in range(0,len(exon)):
    avg[i]=np.mean(depth[(depth['scaffold']==exon['scaffold'][i])&(depth['location']>=exon['start'][i])&(depth['location']<=exon['end'][i])]['depth'])
exon['average_depth']=avg
exon.to_csv("GL349773.WLM_exon_avg_depth.csv”)