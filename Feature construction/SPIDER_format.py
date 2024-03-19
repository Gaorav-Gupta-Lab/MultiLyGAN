import csv
import os
import numpy as np
import pandas as pd




if __name__=='__main__':
    input_label_dir ='./combine_filtered/'
    input_data_dir = './'
    output_dir = './SPIDER/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for win in range(21,22):
        res_name = output_dir + 'SPIDER_' + str(win) + '.csv'
        res_data = []
        count = 0
        label_file_name = input_label_dir+'combine_filtered'+str(win)+'.csv'
        data_dir = input_data_dir + str(win)+'/'
        label_data = pd.read_csv(label_file_name,header=None)
        for i in range(label_data.shape[0]):
            tmp_id = label_data.iloc[i,0]
            tmp_site = label_data.iloc[i,1]
            file_name = data_dir+str(tmp_id)+'_'+str(tmp_site)+'.i1'
            if not os.path.exists(file_name):
                file_name = data_dir + str(tmp_id) + '_' + str(tmp_site) + '.i0'
            one_sample = np.array([])
            with open(file_name) as f:
                test = 0
                line = f.readline()
                while line:
                    if '#' not in line:
                        tmp_value = line.strip().split()
                        tmp_value = np.array(tmp_value[-19:len(tmp_value)]).astype('float')
                        one_sample = np.append(one_sample,tmp_value)
                        test += 1
                    line = f.readline()
                f.close()
            count +=1
            if not test == 2*win+1:
                print('Error for',str(win),data_dir)
            res_data.append(one_sample)
        print(win, 'count:', count)
        df = pd.DataFrame(res_data)
        df.to_csv(res_name, index=None, header=None)