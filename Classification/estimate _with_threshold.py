import csv
import numpy as np
from sklearn.metrics import auc
from collections import Iterable
import matplotlib.pyplot as plt
import pandas as pd
import os
import math


def read_data(filename):
    list1=[]
    with open(filename) as f:
        for line in f:
            sl=line.split(',')
            sl[-1].strip()
            if len(sl)>1:
                example = []
                for i in range(len(sl)):
                    example.append(float(sl[i]))
                list1.append(example)
            else:
                list1.append(int(sl[0]))
    return list1

def save_csv(data,dir):
    csvfile = open(dir, 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['TPR', 'FPR'])
    for i in range(len(data[0])):
        writer.writerow([data[0][i], data[1][i]])
    csvfile.close()

def save_result(data, dir):
    csv_file = open(dir, 'w', newline='')
    writer = csv.writer(csv_file)
    if isinstance(data[0],Iterable):
        for i in range(len(data)):
            writer.writerow(data[i])
    else:
        for i in range(len(data)):
            writer.writerow([data[i]])
    csv_file.close()


def ROC(prob,real,drawROC,now_class):
    num=len(real)
    p=[]
    t=[]
    for i in range(num):
        p.append(prob[i])
        t.append(real[i])
    data = pd.DataFrame(index=range(0, num), columns=('probability', 'The true label'))
    data['The true label'] = t
    data['probability'] = p
    data.sort_values('probability', inplace=True, ascending=False)
    TPRandFPR = pd.DataFrame(index=range(len(data)), columns=('TP', 'FP'))

    for j in range(len(data)):
        data1 = data.head(n=j + 1)
        FP = len(data1[data1['The true label'] == 0][data1['probability'] >= data1.head(len(data1))['probability']])/float(len(data[data['The true label'] == 0]))
        TP = len(data1[data1['The true label'] == 1][data1['probability'] >= data1.head(len(data1))['probability']])/float(len(data[data['The true label'] == 1]))
        TPRandFPR.iloc[j] = [TP, FP]
    AUC = auc(TPRandFPR['FP'], TPRandFPR['TP'])
    if drawROC >= 1:
        plt.scatter(x=TPRandFPR['FP'], y=TPRandFPR['TP'],s=5, label='(FPR,TPR)', color='k')
        plt.plot(TPRandFPR['FP'], TPRandFPR['TP'], 'k', label='AUC = %0.2f' % AUC)
        plt.legend(loc='lower right')
        plt.title('Receiver Operating Characteristic')
        plt.plot([(0, 0), (1, 1)], 'r--')
        plt.xlim([-0.01, 1.01])
        plt.ylim([-0.01, 01.01])
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        # plt.show()
        plt.savefig("./Picture/ROC"+str(now_class)+".png")
        plt.clf()
    return AUC,TPRandFPR['TP'],TPRandFPR['FP']


def get_confused_M(predict,label):
    l=7
    M=np.zeros((l,l))
    for i in range(len(label)):
        x=int(label[i]-1)
        y=int(predict[i]-1)
        M[x][y]=M[x][y]+1
    return M

def cal_MCC_whole(M):
    covxx=0
    covyy=0
    covxy=0
    for i in range(len(M)):
        Sl=np.sum(M,axis=0)[i]
        Sfg=np.sum(M)-Sl
        Sl2=np.sum(M,axis=1)[i]
        Sfg2=np.sum(M)-Sl2
        covxx+=Sl*Sfg
        covyy+=Sl2*Sfg2
    for k in range(len(M)):
        for l in range(len(M)):
            for m in range(len(M)):
                covxy+=M[k][k]*M[m][l]-M[l][k]*M[k][m]
    whole_MCC=covxy/np.sqrt(covxx*covyy)
    return whole_MCC


def cal_ACC_whole(M):
    Acc=0
    for i in range(len(M)):
        Acc+=M[i][i]
    ACC=float(Acc)/np.sum(M)
    return ACC


def cal_CEN_whole(M):
    CEN=0
    N=len(M)
    SS=np.sum(M)
    Row_sum=np.sum(M,axis=1)
    Col_sum=np.sum(M,axis=0)
    for j in range(N):
        Up_Pj=Col_sum[j]+Row_sum[j]
        Down_Pj=2*SS
        Pj=float(Up_Pj)/Down_Pj
        Nx_item=0
        for k in range(N):
            if k==j:
                continue
            else:
                Pjjk=float(M[j][k])/Up_Pj
                Pjkj=float(M[k][j])/Up_Pj
                Nx_item+=np.log2(pow(Pjjk,Pjjk)*pow(Pjkj,Pjkj))/np.log2(2*(N-1))
        CEN+=-1*Pj*Nx_item
    return CEN


def cal_E_whole(M):
    error=0
    SS=np.sum(M)
    right=0
    for i in range(len(M)):
        right+=M[i][i]
    error=float(SS-right)/SS
    return error


def get_estimators(predict,label):
    TP, TN, FP, FN = 0, 0, 0, 0
    for i in range(len(predict)):
        if predict[i]==label[i]:
            if predict[i]==1:
                TP+=1
            else:
                TN+=1
        else:
            if predict[i]==1:
                FP+=1
            else:
                FN+=1
    Accuracy = (TP + TN) / (TP + TN + FN + FP)
    Specitivity = TN / (TN + FP)
    Sensitivity = TP / (TP + FN)
    MCC = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    return Accuracy, Specitivity, Sensitivity, MCC


def JudgePositive(test_prob,th):
    IsPositive=[]
    for i in range(len(test_prob)):
        if test_prob[i]>=th:
            IsPositive.append(1)
        else:
            IsPositive.append(0)
    return IsPositive


if __name__=='__main__':
    if not os.path.exists('Picture/'):
        os.makedirs('Picture/')
    if not os.path.exists('classify_result/'):
        os.makedirs('classify_result/')
    test_label=read_data('test_label.csv')
    test_prob=read_data('test_pro.csv')
    test_predict=read_data('test_prediction.csv')
    M=get_confused_M(test_predict,test_label)
    threshhold=0.3
    for i in range(7):
        now_label=[]
        now_prob=[]
        now_predict=[]
        for j in range(len(test_label)):
            if test_label[j]==i+1:
                now_label.append(1)
            else:
                now_label.append(0)
            if test_predict[j]==i+1:
                now_predict.append(1)
            else:
                now_predict.append(0)
            now_prob.append(test_prob[j][i])
        if threshhold>0:
            now_predict=JudgePositive(now_prob,threshhold)
        AUC,TPR,FPR=ROC(now_prob,now_label,1,i+1)
        ACC,Spe,Sen,MCC=get_estimators(now_predict,now_label)
        if not os.path.exists('classify_result/class'+str(i+1)+'/'):
            os.makedirs('classify_result/class'+str(i+1)+'/')
        save_csv([TPR,FPR], './classify_result/class'+str(i+1)+'/'+str(i+1)+'TPR_FPR.csv')
        save_result([ACC,Spe,Sen,MCC,AUC],'./classify_result/class'+str(i+1)+'/'+str(i+1)+'Acc_Spe_Sen_MCC_AUC.csv')
    whole_ACC=cal_ACC_whole(M)
    print(whole_ACC)
    whole_MCC=cal_MCC_whole(M)
    print(whole_MCC)
    whole_CEN=cal_CEN_whole(M)
    print(whole_CEN)
    whole_E=cal_E_whole(M)
    print(whole_E)
    save_result([whole_ACC,whole_MCC,whole_CEN,whole_E],'whole_ACC_MCC_CEN_E_result.csv')







