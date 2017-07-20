import ROOT
import numpy as np

def GetAverage(roodataset,roorealvar):

    nTotal = roodataset.sumEntries()
    sum_ = 0.0
    for i in range(int(nTotal)):
        sum_ += roodataset.get(i).find(roorealvar).getVal()
    return sum_/nTotal

def GetMin(roodataset,roorealvar):

    nTotal = roodataset.sumEntries()
    min_ = []    
    for i in range(int(nTotal)):
        min_.append(roodataset.get(i).find(roorealvar).getVal())
    return min(min_)

def GetMedian(roodataset,roorealvar):

    nTotal = roodataset.sumEntries()
#    sum_ = 0.0
    list_ = []
    for i in range(int(nTotal)):
        list_.append(roodataset.get(i).find(roorealvar).getVal())
#        sum_ += roodataset.get(i).find(roorealvar).getVal()
    return np.median(list_)

