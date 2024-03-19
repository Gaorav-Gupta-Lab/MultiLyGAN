import csv
import os
import numpy as np
import pandas as pd


if __name__=='__main__':
    input_dir = './'
    output_dir = './all_features/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    file_dir = ['combine_filtered','AAIndex','CKspace','PWM','ReduceAlphabet',
                'FoldAmyloid','Binary','PC_PseAAC','SC_PseAAC','SPIDER']
    dim = []
    column= ['win', 'samples', 'file_dim', 'feature_dim','AAIndex','CKspace','PWM','ReduceAlphabet',
                'FoldAmyloid','Binary','PC_PseAAC','SC_PseAAC','SPIDER']
    for win in range(3,22):
        one_win_dim = []
        df_list = []
        for i in range(len(file_dir)):
            if i == 0:
                file_name = input_dir+file_dir[i]+'/'+file_dir[i]+str(win)+'.csv'
            else:
                file_name = input_dir + file_dir[i] + '/' + file_dir[i] + '_' + str(win) + '.csv'
            tmp_df = pd.read_csv(file_name,header=None)
            one_win_dim.append(tmp_df.shape[1])
            df_list.append(tmp_df)
        res = pd.concat(df_list,axis=1)
        res_name = output_dir+'all_features_'+str(win)+'.csv'
        res.to_csv(res_name,index=None, header=None)
        info_dim = [win, res.shape[0],res.shape[1],res.shape[1]-4]
        info_dim.extend(one_win_dim[1:])
        dim.append(info_dim)
        print(dim[-1])
    dim_df = pd.DataFrame(dim,columns=column)
    dim_df.to_csv('dim_count_3_21.csv')

