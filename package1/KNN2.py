import numpy as np


def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i + j] = int(lineStr[j])
    return returnVect


if __name__ == '__main__':
    imgVector = img2vector('D:\\Downloads\\machinelearninginaction\\Ch02\\digits\\trainingDigits\\0_0.txt')
    print(imgVector[0, 0:31])
