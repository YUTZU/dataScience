import math
import operator
import numpy as np
import matplotlib.pyplot as plt



loadtraindata=[]
loadtestdata=[]



def main():
    k=20
    loadData()

    realtestdata = toDatasplit(loadtestdata)
    splittraindata = toDatasplit(loadtraindata)

    testingerror=geterrorrate(realtestdata,splittraindata,k)
    trainingerror=geterrorrate(splittraindata,splittraindata,k)

    getDiagram(trainingerror,testingerror)


def getDiagram(data1,data2):
    num1=[]
    num2=[]

    for index in range(len(data1)):
        num1.append(data1[index][1])
        num2.append(data2[index][1])

    plt.figure(figsize=(8, 4))
    plt.xlabel("K-Number")
    plt.ylabel("Error Number")
    y1=num1
    y2=num2
    x=range(1,21)
    plt.xticks(range(1,21))
    plt.plot(x,y1,'ob-', label='training error')
    plt.plot(x,y2,'or-',label='testing error')
    plt.legend()
    plt.show()

def geterrorrate(testData,trainData,krange):
    geterror=[]
    testdataAfterTrain = []
    del geterror[:]

    for k in range(krange):
        for index in range(len(testData)):
            neighborName=toCaculate(trainData,testData[index][0],k+1)
            testdataAfterTrain.append([testData[index][0],[neighborName]])
        errorrate=compared(testData, testdataAfterTrain)
        geterror.append([k+1,errorrate])
        del testdataAfterTrain[:]

    return geterror

def loadData():
    data = open('iris.txt', 'r')
    count = 0

    for index in data:
        count +=1
        if count <= 25:
            loadtraindata.append(index)
        if (count > 25) & (count <= 50):
            loadtestdata.append(index)
        if ((count > 50) & (count <= 75)):
            loadtraindata.append(index)
        if ((count >75) & (count <= 100)):
            loadtestdata.append(index)
        if ((count > 100) & (count <= 125)):
            loadtraindata.append(index)
        if ((count > 125) & (count <= 150)):
            loadtestdata.append(index)

def toDatasplit(testdata1):
    data=[]
    for i, x in enumerate(testdata1):
        data.append([[float(x[0:3]), float(x[4:7]), float(x[8:11]), float(x[12:15])], [x[16:len(x)-1]]])
    return data

def toCaculate(traindata,testdata,k):
    distance=[]

    for index in range(len(traindata)):
        x=traindata[index][0]
        y=testdata
        z=euclideanDistance(x,y,4)
        distance.append([z,traindata[index][1]])

    return findNeighbor(distance,k)


def findNeighbor(distance,k):
    sortedDis = sorted(distance, key=lambda x: x[0])
    category={'Iris-setosa':0 , 'Iris-versicolor':0,'Iris-virginica':0}
    neighbor=[]

    for index in range(k):
        neighbor.append(sortedDis[index])

    for index in range(k):
        if neighbor[index][1] == ['Iris-setosa'] :
            category['Iris-setosa']+=1
        elif neighbor[index][1] == ['Iris-versicolor'] :
            category['Iris-versicolor']+=1
        elif neighbor[index][1] == ['Iris-virginica']:
            category['Iris-virginica']+=1

    maxNeighbor = max(category.iteritems(), key=operator.itemgetter(1))[0]
    maxNum =  max(category.iteritems(), key=operator.itemgetter(1))[1]

    return maxNeighbor


def compared(trueData,testData):
    isCorret=[]
    for index in range(len(testData)):
        if(trueData[index][1] == testData[index][1]):
            isCorret.append(1)
        else:
            isCorret.append(0)
    errorrate=isCorret.count(0)/float(75)  #0 is error
    errornum=isCorret.count(0)
    correctrate=isCorret.count(1)/float(75)

    return errornum

def euclideanDistance(x,y,length):
    distance = 0.0
    for i in range(length):
        distance += pow((x[i] - y[i]), 2)
    return math.sqrt(distance)

main()