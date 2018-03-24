from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
import numpy as np
import pandas as pd

length=370000
W_count_A=np.zeros(length)
W_count_T=np.zeros(length)
W_count_G=np.zeros(length)
W_count_C=np.zeros(length)
W_count_N=np.zeros(length)
WL_count_A=np.zeros(length)
WL_count_T=np.zeros(length)
WL_count_G=np.zeros(length)
WL_count_C=np.zeros(length)
WL_count_N=np.zeros(length)

for seq_record in SeqIO.parse("/Users/Jason/Documents/aphicarus/biotypes/9w_349773.fasta", "fasta"):
    for i in range(0,length):
        if seq_record.seq[i]=="A" or seq_record.seq[i]=="a":
            W_count_A[i]+=1
        elif seq_record.seq[i]=="T" or seq_record.seq[i]=="t":
            W_count_T[i]+=1
        elif seq_record.seq[i]=="G" or seq_record.seq[i]=="g":
            W_count_G[i]+=1
        elif seq_record.seq[i]=="C" or seq_record.seq[i]=="c":
            W_count_C[i]+=1
        else:
            W_count_N[i]+=1

for seq_record in SeqIO.parse("/Users/Jason/Documents/aphicarus/biotypes/14wl_349773.fasta", "fasta"):
    for i in range(0,length):
        if seq_record.seq[i]=="A" or seq_record.seq[i]=="a":
            WL_count_A[i]+=1
        elif seq_record.seq[i]=="T" or seq_record.seq[i]=="t":
            WL_count_T[i]+=1
        elif seq_record.seq[i]=="G" or seq_record.seq[i]=="g":
            WL_count_G[i]+=1
        elif seq_record.seq[i]=="C" or seq_record.seq[i]=="c":
            WL_count_C[i]+=1
        else:
            WL_count_N[i]+=1


#table=np.concatenate((W_count_A, W_count_T, W_count_G,W_count_C,W_count_N,WL_count_A, WL_count_T, WL_count_G,WL_count_C,WL_count_N),axis=0)
table=np.vstack((W_count_A[0:length],W_count_T[0:length],W_count_G[0:length],W_count_C[0:length],W_count_N[0:length],WL_count_A[0:length],WL_count_T[0:length],WL_count_G[0:length],WL_count_C[0:length],WL_count_N[0:length]))
df=pd.DataFrame(table)
dftr=df.transpose()
dftr.columns=['1','2','3','4','5','6','7','8','9','10']
'''df_W4NWL6N=dftr[dftr['5']<5][dftr['10']<7]
df_W4NWL6N.to_csv("/Users/Jason/Desktop/9w14wl_349773_data_df_W4NWL6N.csv",header=False,index=False)'''
df_W0NWL0N=dftr[dftr['5']<1][dftr['10']<1]
df_W0NWL0N.to_csv("/Users/Jason/Desktop/9w14wl_349773_data_df_W0NWL0N.csv",header=False,index=False)