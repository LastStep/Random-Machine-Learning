import random
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

Rock, Paper, Scissior = 0, 1, 2
numActions = 3
oppStrategy = np.array([0.4,0.3,0.3])

def getstrategy(regretSum, strategySum):
    strategy = np.maximum(regretSum, 0)
    normalizingSum = np.sum(strategy)
    if normalizingSum > 0:
        strategy /= normalizingSum
    else:
        strategy = np.ones(3)/numActions
    strategySum += strategy
    return strategy

def getAveragestrategy(strategySum):
    avgStrategy = np.zeros(3)
    normalizingSum = np.sum(strategySum)
    if normalizingSum > 0:
        avgStrategy = strategySum/normalizingSum
    else:
        avgStrategy = np.ones(3)/numActions
    return avgStrategy

def getAction(strategy):
#   return np.searchsorted(np.cumsum(strategy), random.random())
    return np.sum(np.where(np.cumsum(strategy) > random.random(), 0, 1))

def train(iterations):

    regretSum = np.zeros(numActions)
    strategySum = np.zeros(3)
    actionUtility = np.zeros(numActions)

    for i in range(iterations):

        strategy = getstrategy(regretSum, strategySum)
        myAction = getAction(strategy)
        oppAction = getAction(oppStrategy)

        actionUtility[oppAction] = 0
        actionUtility[(oppAction + 1) % numActions] = 1
        actionUtility[(oppAction - 1) % numActions] = -1

        regretSum += actionUtility - actionUtility[myAction]

    return strategySum


print(getAveragestrategy(train(10000)))

