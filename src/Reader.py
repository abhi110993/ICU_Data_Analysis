"""

# Author: Abhishek Mishra
# MTech Student
# IIT Ropar
# Entry Number- 2018CSM1002

"""
import numpy as np
import random

class Helper:
    
    def readValuesFromFile(self):
        f = open("linregdata", "r")
        x = []
        y = []
        s=f.readline()
        sex=0
        while s!="":
            a = s.split(',')
            if a[0]=='F':
                sex=[1,1,0,0]
            elif a[0]=='I':
                sex=[1,0,1,0]
            else:
                sex=[1,0,0,1]
            x1 = [sex[0],sex[1],sex[2],sex[3], float(a[1]), float(a[2]), float(a[3]),float(a[4]),float(a[5]),float(a[6]),float(a[7])] 
            x.append(x1)
            y.append(float(a[8].split('\n')[0]))
            s=f.readline()
        return [np.array(x),np.array(y).transpose()]
    
    
    ## This function extracts features from file w.r.t. Heart Rates. 
    # @params:     isAbnormal        :      It should be given 1 is abnormal else 0
    def readHeartRatesFromFile(self, isAbnormal):
        if(isAbnormal==1):
            f = open("out_abnormal.csv", "r")
        else:
            f = open("out_normal.csv", "r")
        x = []
        y = []
        s=f.readline()
        while s!="":
            a = s.split(',')
            x1 = [float(a[0]),float(a[1]),float(a[2])] 
            x.append(x1)
            y.append(float(isAbnormal))
            s=f.readline()
        return [np.array(x),np.array(y).transpose()]
    
    def standardizeTestingSet(self,X,mean,std):
        for i in range(0,len(X)):
            for j in range(4,11):
                X[i][j]=((X[i][j]-mean[j])/std[j])
        return X
    
    def standardizeTrainingSet(self,X):
        mean=np.mean(X, axis=0)
        std=np.std(X, axis=0)
        for i in range(0,len(X)):
            for j in range(4,11):
                X[i][j]=((X[i][j]-mean[j])/std[j])
        #print("Mean and Standard Deviation is - "+ str(np.mean(X,axis=0))+str(np.std(X,axis=0)))
        return [X, mean, std]
    
    def getTrainingAndValidationSet(self,X,Y,frac):
        trainFracSize=int(frac*len(X));
        trainIndex=random.sample(range(0, len(X)), trainFracSize)
        trainInput=[]
        testInput=[]
        trainOutput=[]
        testOutput=[]
        for i in range(0, len(X)):
            if i in trainIndex:
                trainInput.append(X[i])
                trainOutput.append(Y[i])
            else:
                testInput.append(X[i])
                testOutput.append(Y[i])
        return [trainInput,trainOutput,testInput,testOutput]
    