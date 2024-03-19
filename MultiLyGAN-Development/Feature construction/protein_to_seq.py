import csv
import os

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


def save_split(dir,id,seq):
    file=open(dir, 'w', newline='')
    file.write('>'+id+' '+str(len(seq))+'\n'+seq)
    file.close()


def save_split_csv(dir,data):
    csv_file = open(dir, 'w', newline='')
    writer = csv.writer(csv_file)
    for i in range(len(data)):
        writer.writerow(data[i])
    csv_file.close()


def save_seq(id,site,seq,dir,win):
    tmp=''
    final_dir = dir+'/seq_'+str(win)
    if not os.path.exists(final_dir):
        os.mkdir(final_dir)
    for i in range(len(seq)):
        if seq[i]=='X':
            continue
        else:
            tmp+=seq[i]
    else:
        save_split(final_dir+'/'+id+'_'+site+'.seq',id,tmp)

def save_all_seq(dir,data):
    file=open(dir,'w',newline='')
    for i in range(len(data)):
        id = data[i][0]
        site = data[i][1]
        seq = data[i][2]
        tmp=''
        for i in range(len(seq)):
            if seq[i] == 'X':
                continue
            else:
                tmp += seq[i]
        # file.write('>' + id+'_'+site + ' ' + str(len(tmp)) + '\n' + tmp+'\n')
        file.write('>' + id + ' ' + str(len(tmp)) + '\n' + tmp + '\n')
    file.close()


def save_file_list(dir,data):
    file = open(dir+'file_list.txt', 'w', newline='')
    for i in range(len(data)):
        id=data[i][0]
        site=data[i][1]
        file.write(id+'_'+site+' '+dir+id+'_'+site+'.seq\n')
    file.close()

if __name__=='__main__':
    input_dir = './combine_filtered/'
    output_dir = './all_seq/'
    for win in range(3,26):
        dir = output_dir+ str(win)
        if not os.path.exists(dir):
            os.mkdir(dir)
        ID,Site,Seq=readcsvfile(input_dir+'combine_filtered'+str(win)+'.csv')
        Normal=[]
        for i in range(len(ID)):#用来生成每个蛋白质序列单独保存的文件的函数
            id = ID[i]
            site = Site[i]
            seq=Seq[i]
            Normal.append([id,site,seq])
            save_seq(id,site,seq,dir,win)
        save_all_seq(dir+'/total_'+str(win)+'.seq',Normal)#用来生成所有蛋白质都保存在一个文件中的文件函数
        print('Have done for win:',win)

