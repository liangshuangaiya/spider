from math import log


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    label = ['no flipers', 'flipers']
    return dataSet, label


def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelSet = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelSet:
            labelSet[currentLabel] = 0
        labelSet[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelSet:
        prop = float(labelSet[key]) / numEntries
        shannonEnt -= prop * log(prop, 2)
    return shannonEnt


if __name__ == '__main__':
    dataSet, label = createDataSet()
    shannonEnt = calcShannonEnt(dataSet)
    print(shannonEnt)
