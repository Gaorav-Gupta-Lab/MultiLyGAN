import csv
import os
import numpy as np
import pandas as pd


def get_remained_feature_index(pcc_mat,th=0.5):
    n = len(pcc_mat)
    remain = np.ones(n)
    res= []
    for i in range(n):
        if remain[i] == 0:
            continue
        for j in range(i+1,n):
            if remain[j] ==0:
                continue
            if np.isnan(pcc_mat[i][j]):
                remain[j]=0
            if np.abs(pcc_mat[i][j])>th:
                remain[j]=0
    for i in range(n):
        if remain[i]==1:
            res.append(i)
    return res

def filter_0var(feature_df):
    var = np.var(feature_df,axis=0)
    res = []
    for i in range(len(var)):
        if not var[i]==0:
            res.append(i)
    df = feature_df.loc[:,res]
    return df




if __name__=='__main__':
    input_dir = './all_features/'
    output_dir = './PCC_filtered_res_0.5/'
    th = 0.5
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    dim = []
    for win in range(10,11):
        file_name = input_dir+'all_features_'+str(win)+'.csv'
        res_name = output_dir+'PCC_'+str(win)+'.csv'
        df = pd.read_csv(file_name,header=None)
        n_col = df.shape[1]
        # df.columns = range(n_col)
        feature_df = df.loc[:,range(4,n_col)]
        feature_df.columns = range(feature_df.shape[1])
        feature_df = filter_0var(feature_df)
        sample_df = df.loc[:,range(0,4)]
        pcc_matrix = np.corrcoef(feature_df, rowvar=False)
        pd.DataFrame(pcc_matrix).to_csv('test.csv')
        ind = get_remained_feature_index(pcc_matrix, th=0.5)
        feature_df.columns = range(feature_df.shape[1])
        filtered_df = feature_df.loc[:,ind]
        res_df = pd.concat([sample_df,filtered_df],axis=1)
        dim.append([win, res_df.shape[0], n_col-4, res_df.shape[1] - 4])
        res_df.to_csv(res_name, index=None, header=None)
        print(dim[-1])
    dim_df = pd.DataFrame(dim, columns=['win', 'samples', 'before_pcc', 'after_pcc'])
    dim_df.to_csv('dim_pcc_0.5_3_10.csv')

