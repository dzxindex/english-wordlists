# -*- coding: utf-8 -*-
import pandas as pd


## 切割csv文件

def _readCsv(filename):
    df = pd.read_csv(filename,encoding='GBK')
    print(df.head(5))
    print(df.shape)

    return df

def splitFile(filename, CuttingNumber):
    df = _readCsv(filename)
    total = df.shape[0]
    splitTime = int(total/CuttingNumber)
    if splitTime > 1 :
        for i in range(splitTime) :
            name = filename.split('.')[0]
            suffix = filename.split('.')[1]
            dfCut = df[CuttingNumber*i:CuttingNumber*(i+1)]
            dfCut.to_csv("{}-unit{}.{}".format(name,i,suffix))
    splitTime = total/CuttingNumber



filename = '四级高频词统计.csv'

CuttingNumber = 500
# df2 = df[:5]
_readCsv(filename)
splitFile(filename, CuttingNumber)
