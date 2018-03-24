from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
import numpy as np
import pandas as pd
from Bio import AlignIO

'''
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
'''

handle = open("/Users/Jason/Documents/aphicarus/biotypes/9w_349773.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
    print(record.id)
    print(record.seq)
