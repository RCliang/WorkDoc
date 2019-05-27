# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:28:42 2019

@author: 8000725635
"""

import pandas as pd

with open('F:/项目/黄牛/hn_data.csv','rb') as f:
    rawdata=pd.read_csv(f,encoding="gbk")
    

temp_feature=list(rawdata.keys())

drop_feature=['REPORTDATE','REPORTHOUR','REPORTORNAME','REPORTORPHONENO','REPORTORMOBILE','LINKERNAME',\
              'LINKERPHONENO','LINKERMOBILE','ACCIDENTNO','DAMAGEREMARK','DAMAGESTARTDATE','DAMAGESTARTHOUR',\
              'DAMAGECAUSATIONNAME','DAMAGENAME','DAMAGEADDRESS','DAMAGECATALOGNAME','CHECKSITE','ARRIVELOCALETIME',\
              'CHECKDATE','REGISTNO_BYPERSON','HN_FLAG']
rawdata=rawdata.drop(drop_feature,axis=1)
temp_feature=list(rawdata.keys())
temp_feature.remove('REGISTNO')

drop_col=[]
keep_col=[]
for item in temp_feature:
    print (item)
    print ('cnt: '+str(rawdata[item].isnull().sum()))
    na_rate=rawdata[item].isnull().sum()/rawdata.shape[0]
    print ('na_rate: '+str(na_rate))
    if na_rate > 0.7:
        drop_col.append(item)
    else:
        keep_col.append(item)

newdata=rawdata.drop(drop_col,axis=1)
for item in keep_col:
    temp=newdata[item].mode()[0]
    newdata[item]=newdata[item].fillna(temp)


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(newdata['DAMAGECODE'])
le.classes_
newdata['DAMAGECODE']=le.transform(newdata['DAMAGECODE'])

#add new content
