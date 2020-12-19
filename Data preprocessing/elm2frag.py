import numpy as np
import pandas as pd
import os


def read_one_file(file_name):
    dict_id_site = {}
    dict_id_seq = {}
    with open(file_name,'r') as f:
        for line in f:
            if 'Uniprot Accession' in line:
                continue
            line_split = line.split('\t')
            tmp_ID = line_split[1]
            tmp_site = np.int(line_split[2])
            tmp_seq = line_split[4]
            if tmp_ID in dict_id_site.keys():
                dict_id_site[tmp_ID].append(tmp_site)
            else:
                dict_id_site[tmp_ID] = [tmp_site]
                dict_id_seq[tmp_ID] = tmp_seq
    f.close()
    return dict_id_site, dict_id_seq


def cut_all_frag(seq, site, min_win=3,max_win=25,na_fill='X'):
    n = len(seq)
    left_cut = ''
    right_cut = '' # contain the center "K"
    if site - max_win < 0:
        cut = seq[0:site]
        fill_s = na_fill*(max_win-site)
        left_cut = fill_s+cut
    else:
        left_cut = seq[site-max_win:site]
    if site+max_win > n-1:
        cut = seq[site:n]
        fill_s = na_fill*(site+max_win+1-n)
        right_cut =cut + fill_s
    else:
        right_cut = seq[site:site+max_win+1]
    final_cut = left_cut + right_cut

    all_cuts = []
    # print('test:print all cuts')
    for i in range(min_win,max_win+1):
        diff = max_win-i
        tmp_left_cut = left_cut[diff:max_win]
        tmp_right_cut = right_cut[0:i+1]
        tmp_cut = tmp_left_cut + tmp_right_cut
        # print(tmp_cut)
        all_cuts.append(tmp_cut)
    return all_cuts




def get_frag(dict_id_site,dict_id_seq, min_win = 3, max_win = 25):
    dict_pos_seq={}
    dict_neg_seq={}
    for ID in dict_id_site:
        site_list = dict_id_site[ID]
        tmp_seq = dict_id_seq[ID]
        for i in range(len(tmp_seq)):
            if tmp_seq[i]=='K':
                all_cuts = cut_all_frag(tmp_seq, i, min_win, max_win)
                if i+1 in site_list:
                    for j in range(len(all_cuts)):
                        tmp_cut = all_cuts[j]
                        if min_win+j in dict_pos_seq.keys():
                            dict_pos_seq[min_win + j].append([ID, i+1, tmp_cut])
                        else:
                            dict_pos_seq[min_win + j] = [[ID, i + 1, tmp_cut]]
                else:
                    for j in range(len(all_cuts)):
                        tmp_cut = all_cuts[j]
                        if min_win+j in dict_neg_seq.keys():
                            dict_neg_seq[min_win + j].append([ID, i+1, tmp_cut])
                        else:
                            dict_neg_seq[min_win + j]=[[ID, i + 1, tmp_cut]]
    return dict_pos_seq,dict_neg_seq


def save_frag(dict_pos_seq, dict_neg_seq, filename, result_dir):
    save_dir = result_dir+'/'+filename
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for win in dict_pos_seq.keys():
        tmp_pos = pd.DataFrame(dict_pos_seq[win],columns=['id','site','seq'])
        tmp_neg = pd.DataFrame(dict_neg_seq[win],columns=['id','site','seq'])
        pos_file_name = save_dir + '/' + filename + '_pos' + str(win) + '.csv'
        neg_file_name = save_dir + '/' + filename + '_neg' + str(win) + '.csv'
        print('save file:'+pos_file_name)
        print('save file:'+neg_file_name)
        tmp_pos.to_csv(pos_file_name, index=None)
        tmp_neg.to_csv(neg_file_name, index=None)



if __name__ == '__main__':
    type = ['Acetylation','Glycation','Malonylation','Methylation',
            'Succinylation','Sumoylation','Ubiquitination']
    # type = ['test']
    result_dir = 'fragment_data'
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    for i in range(len(type)):
        tmp_type = type[i]
        tmp_dir = tmp_type+'/'+tmp_type + '.elm'
        dict_id_site, dict_id_seq = read_one_file(tmp_dir)
        dict_pos_seq, dict_neg_seq = get_frag(dict_id_site,dict_id_seq,3,25)
        save_frag(dict_pos_seq,dict_neg_seq, tmp_type, result_dir)


