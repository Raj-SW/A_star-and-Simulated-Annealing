import numpy as np
def calculateAcceptanceProbability(oldCost,newCost,currentTemp):
        costdiff=newCost-oldCost
        return np.exp(-costdiff/currentTemp)