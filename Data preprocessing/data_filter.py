import csv
import pandas as pd
import os
import numpy as np


def read_file(win,input_dir):
    file_name = input_dir+ '/combine_'+ str(win)+ '.csv'
    tmp_data = pd.read_csv(file_name,header=None)
    return tmp_data



if __name__=='__main__':
    file_num = 7
    types = ['Acetylation', 'Glycation', 'Malonylation', 'Methylation',
             'Succinylation', 'Sumoylation', 'Ubiquitination']
    input_dir = './combine/'
    output_dir = './combine_filtered/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for win in range(3,26):
        tmp_data=read_file(win,input_dir)
        res_data= []
        for i in range(tmp_data.shape[0]):
            id = tmp_data.iloc[i,0]
            site = tmp_data.iloc[i,1]
            seq = tmp_data.iloc[i,2]
            type_class = np.array(tmp_data.iloc[i,3:10])
            if ('X' in seq) or ('B' in seq) or ('J' in seq) or ('0' in seq) or ('U' in seq) or ('Z' in seq):
                continue
            if np.sum(type_class)!=1:
                continue
            label = np.argmax(type_class)+1
            res_data.append([id, site, seq, label])
        res_df = pd.DataFrame(res_data)
        res_df.to_csv(output_dir+'combine_filtered'+str(win)+'.csv', header=None, index=None)
        print('Has done: win:', win)




