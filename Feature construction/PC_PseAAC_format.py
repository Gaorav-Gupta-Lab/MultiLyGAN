import csv
import os
import numpy as np
import pandas as pd



def all_files(path, file_type):
    f_list = []

    def files_list(father_path):
        sub_path = os.listdir(father_path)
        for sp in sub_path:
            full_sub_path = os.path.join(father_path, sp)
            if os.path.isfile(full_sub_path):
                file_name, post_name = os.path.splitext(full_sub_path)
                if post_name == file_type:
                    f_list.append(file_name + post_name)
            else:
                files_list(full_sub_path)

    files_list(path)
    return f_list

def sort_file(f_list):
    dict_file = {}
    for x in f_list:
        name = x.split('/')[-1].split('.')[0]
        tmp_win = np.int(name.split('_')[0])
        count = np.int(name.split('_')[1])
        if tmp_win in dict_file.keys():
            dict_file[tmp_win].append(count)
        else:
            dict_file[tmp_win] = [count]
    for win in dict_file.keys():
        dict_file[win].sort()
    return dict_file


def readcsvfile(filename): #读文件
    ID=[] #id
    Site=[] #site
    Seq=[] #seq
    with open(filename) as f:
        for line in f:
            sl=line.split(',')
            ID.append(sl[0].split()[0])
            Site.append(sl[1].split('.')[0])
            Seq.append(sl[2].split()[0])
    return ID,Site,Seq


if __name__=='__main__':
    input_dir = './PC_data/'
    output_dir = './PC_PseAAC/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    file_list = all_files(input_dir,'.txt')
    dict_file = sort_file(file_list)
    for win in dict_file.keys():
        res_name = output_dir + 'PC_PseAAC_'+str(win)+'.csv'
        res_data =[]
        count = 0
        for i in dict_file[win]:
            file_name = input_dir + str(win)+'_'+str(i)+'.txt'
            with open(file_name) as f:
                line = f.readline()
                while '>' not in line:
                    line = f.readline()
                while line:
                    if '>' in line:
                        line = f.readline()
                        tmp_value = np.array(line.strip().split(','))
                        tmp_value = tmp_value.astype('float')
                        res_data.append(tmp_value)
                        count += 1
                        line = f.readline()
                        line = f.readline()
                    else:
                        line = f.readline()
                f.close()
        print(win, 'count:',count)
        df = pd.DataFrame(res_data)
        df.to_csv(res_name, index=None, header=None)

