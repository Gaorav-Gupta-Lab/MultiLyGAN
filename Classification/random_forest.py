from sklearn.ensemble import RandomForestClassifier
import csv
import random
import numpy as np
import os
import pandas as pd
from sklearn.metrics import accuracy_score

classifier = RandomForestClassifier(n_estimators=50)


def readcsvfile(filename):
    df = pd.read_csv(filename,header=None)
    return df


def data_spilt(data, test_ratio=0.2):
    data_real = data[~(data.loc[:,2]=='-1.0')]
    n_col = data_real.shape[1]
    label_set = np.array(data_real.loc[:,n_col-1].unique())
    ind_test = pd.DataFrame()
    for label in label_set:
        tmp_df = data_real[data_real.loc[:,n_col-1]==label]
        tmp_ind = tmp_df.sample(frac=test_ratio)
        ind_test = pd.concat([ind_test,tmp_ind],axis=0)
    ind_test=ind_test.sample(frac=1)
    ind_test_idx = ind_test.loc[:,[0,1,2,ind_test.shape[1]-1]]
    train = pd.concat([data,ind_test,ind_test]).drop_duplicates(keep=False)
    test_feature = ind_test.loc[:, range(3,ind_test.shape[1]-1)]
    test_label = ind_test.loc[:,ind_test.shape[1]-1]
    train_feature = train.loc[:, range(3,train.shape[1]-1)]
    train_label = train.loc[:,train.shape[1]-1]
    return ind_test_idx, test_feature,test_label,train_feature,train_label


def K_cross(k,x,y,win,train_result_dir,im_dir):
    l=len(x)
    n=l//k
    label=[]
    result=[]
    pro_result=[]
    for i in range(k):
        if i==k-1:
            test_feature=x[n*i:l]
            test_label=y[n*i:l]
            train_feature=x[0:n*i]
            train_label=y[0:n*i]
        elif i==0:
            test_feature = x[n * i:n * (i + 1)]
            test_label = y[n * i:n * (i + 1)]
            train_feature = x[n*(i+1):l]
            train_label = y[n*(i+1):l]
        else:
            test_feature = x[n * i:n * (i + 1)]
            test_label = y[n * i:n * (i + 1)]
            train_feature = np.concatenate((x[0:n*i],x[n*(i+1):l]),axis=0)
            train_label = np.concatenate((y[0:n*i],y[n*(i+1):l]),axis=0)
        X_train = np.array(train_feature)
        Y_train = np.array(train_label)
        x_test = np.array(test_feature)
        classifier.fit(X_train, Y_train)
        predictions = classifier.predict(x_test)
        predict_pro = classifier.predict_proba(x_test)
        data = predictions
        result.extend(data)
        pro_result.extend(predict_pro)
        label.extend(test_label)
    importance=classifier.feature_importances_
    indices=np.argsort(importance)[::-1]
    out=[]
    for i in range(len(indices)):
        # print(str(indices[i])+'\t'+str(np.round(importance[indices[i]],5))+'\n')
        out.append([indices[i],np.round(importance[indices[i]],5)])
    im_name = im_dir+'soft_importance_'+str(win)+'.csv'
    train_label_name =train_result_dir+'train_label_'+str(win)+'.csv'
    train_pred_name =train_result_dir+'train_prediction_'+str(win)+'.csv'
    train_pro_name = train_result_dir+'train_pro_'+str(win)+'.csv'
    pd.DataFrame(out).to_csv(im_name, index=None, header=None)
    pd.DataFrame(result).to_csv(train_pred_name,index=None,header=None)
    pd.DataFrame(label).to_csv(train_label_name,index=None,header=None)
    pd.DataFrame(pro_result).to_csv(train_pro_name,index=None,header=None)


if __name__=='__main__':
    test_ratio = 0.2
    input_dir = './cgan_augmented_data/'
    output_dir = './cgan_rf_result/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fea_im_dir = output_dir+'feature_importance/'
    if not os.path.exists(fea_im_dir):
        os.makedirs(fea_im_dir)
    ind_test_dir = output_dir+'independent_test/'
    if not os.path.exists(ind_test_dir):
        os.makedirs(ind_test_dir)
    test_result_dir = output_dir+'test_results/'
    train_result_dir = output_dir+'train_results/'
    if not os.path.exists(test_result_dir):
        os.makedirs(test_result_dir)
    if not os.path.exists(train_result_dir):
        os.makedirs(train_result_dir)
    acc_result_dir = output_dir+'acc_results/'
    if not os.path.exists(acc_result_dir):
        os.makedirs(acc_result_dir)
    win=3
    file_name = input_dir + 'cgan_augmented_data_'+str(win)+'.csv'
    data = readcsvfile(file_name)
    ind_test_idx, test_feature,test_label, train_feature,train_label = data_spilt(data,test_ratio)
    ind_test_idx_name = ind_test_dir+'independent_test_'+str(win)+'.csv'
    ind_test_idx.to_csv(ind_test_idx_name,header=None,index=None)
    train_feature = np.array(train_feature)
    train_label = np.array(train_label)
    K_cross(10,train_feature,train_label, win,train_result_dir,fea_im_dir)
    X_test=np.array(test_feature)
    Y_test=np.array(test_label)
    classifier.fit(train_feature,train_label)
    predictions=classifier.predict(X_test)
    predict_pro = classifier.predict_proba(X_test)
    data = predictions
    test_pred_name = test_result_dir+'test_prediction_'+str(win)+'.csv'
    test_label_name = test_result_dir+'test_label_'+str(win)+'.csv'
    test_pro_name = test_result_dir+'test_pro_'+str(win)+'.csv'
    acc_name = acc_result_dir+'test_acc_'+str(win)+'.csv'
    pd.DataFrame(data).to_csv(test_pred_name,index=None,header=None)
    pd.DataFrame(test_label).to_csv(test_label_name,index=None,header=None)
    pd.DataFrame(predict_pro).to_csv(test_pro_name,index=None,header=None)
    a = accuracy_score(Y_test, predictions)
    pd.DataFrame([a]).to_csv(acc_name,index=None,header=None)
    print('win:',win,'acc',a)