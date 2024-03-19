import csv
import os



def read_file(win,input_dir,types):
    dir_seq = {}
    dir_list = {}
    ID_Site_list = []
    for type in types:
        file_name = input_dir + type + '/' + type + '_pos'+ str(win)+ '_D40.csv'
        tmp_list=[]
        with open(file_name) as f:
            for line in f:
                if 'ID' in line:
                    continue
                sl = line.split(',')
                ID=sl[0].split()[0]
                site=sl[1].split()[0]
                seq=sl[2].split()[0]
                ID_site = str(ID) + '_' + str(site)
                dir_seq[ID_site] = str(seq)
                dir_list[ID_site] = [0] * file_num
                tmp_list.append(ID_site)
        ID_Site_list.append(tmp_list)
    return dir_seq, dir_list, ID_Site_list



if __name__=='__main__':
    file_num = 7
    types = ['Acetylation', 'Glycation', 'Malonylation', 'Methylation',
             'Succinylation', 'Sumoylation', 'Ubiquitination']
    input_dir = './delhomoseq40/'
    output_dir = './combine/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for win in range(3,26):
        dir_seq, dir_list, ID_Site_list=read_file(win,input_dir,types)
        for i in range(0, len(ID_Site_list)):
            tmp_list = ID_Site_list[i]
            for x in tmp_list:
                dir_list[x][i] = 1
        dir_class = {}
        class_ID = 0
        for x in dir_list.values():
            if not dir_class.__contains__(str(x)):
                dir_class[str(x)] = class_ID
                class_ID += 1
        dir_num = {}
        for x in dir_list.keys():
            s = str(dir_list.get(x))
            if dir_num.__contains__(s):
                dir_num[s] += 1
            else:
                dir_num[s] = 1
        csv_file = open(output_dir+'combine_'+str(win)+'.csv', 'w', newline='')
        writer = csv.writer(csv_file)
        for x in dir_list.keys():
            tmp = x.split('_')
            l = dir_list.get(x)
            out = []
            out.append(tmp[0])
            out.append(tmp[1])
            out.append(dir_seq.get(x))
            out.extend(l)
            out.append(dir_class.get(str(l)))
            out.append(dir_num.get(str(l)))
            writer.writerow(out)
        csv_file.close()
        print('Has done: win:',win)





