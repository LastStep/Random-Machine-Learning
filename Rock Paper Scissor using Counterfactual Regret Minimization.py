import random
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

Rock, Paper, Scissior = 0, 1, 2
numActions = 3
oppStratergy = np.array([0.4,0.3,0.3])

def getStratergy(regretSum, stratergySum):
    stratergy = np.maximum(regretSum, 0)
    normalizingSum = np.sum(stratergy)
    if normalizingSum > 0:
        stratergy /= normalizingSum
    else:
        stratergy = np.ones(3)/numActions
    stratergySum += stratergy
    return stratergy

def getAverageStratergy(regretSum, stratergySum):
    avgStratergy = np.zeros(3)
    normalizingSum = np.sum(stratergySum)
    if normalizingSum > 0:
        avgStratergy = stratergySum/normalizingSum
    else:
        avgStratergy = np.ones(3)/numActions
    return avgStratergy
    
def getAction(stratergy):
#    return np.searchsorted(np.cumsum(stratergy), random.random())
    return np.sum(np.where(np.cumsum(stratergy) > random.random(), 0, 1))

def train(iterations):
    
    regretSum = np.zeros(numActions)
    stratergySum = np.zeros(3)
    actionUtility = np.zeros(numActions)
    
    for i in range(iterations):
        
        stratergy = getStratergy(regretSum, stratergySum)
        myAction = getAction(stratergy)
        oppAction = getAction(oppStratergy)
        
        actionUtility[oppAction] = 0
        actionUtility[(oppAction + 1) % numActions] = 1
        actionUtility[(oppAction - 1) % numActions] = -1
        
        regretSum += actionUtility - actionUtility[myAction]
    
    return regretSum, stratergySum


getAverageStratergy(*train(10000))

