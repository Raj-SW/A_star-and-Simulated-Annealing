import random
from SimulatedAnnealing.GenerateRandomPath import generateRandomPath
from SimulatedAnnealing.CalculateCost import calculateCost
from SimulatedAnnealing.GenerateNeighbourPath import generateNeighbourPath
from SimulatedAnnealing.CalculateAcceptanceProbability import calculateAcceptanceProbability
class SimulatedAnnealing():
    def Traversal(graph,startNode,endNode):
        currentTemp=1000
        FINAL_TEMP=0.1
        ALPHA=0.1

        pointer=1
        cost=0
        newCost=0

        #generate random solution once
        randomSolution=generateRandomPath(graph=graph,end=endNode,start=startNode)
        #generate cost of random solution
        cost=calculateCost(graph=graph,solution=randomSolution)            
       
        while(currentTemp>FINAL_TEMP):
            if(randomSolution[pointer]==endNode):
                pointer=1
            #generate neighbour solution
            neighbourSolution=generateNeighbourPath(graph=graph,start=startNode,end=endNode,solution=randomSolution,pointer=pointer)
            newCost=calculateCost(graph=graph,solution=neighbourSolution)

            #generate neighbour solution cost
            #compare between two solutions
            if(newCost<cost):
                randomSolution=neighbourSolution
                cost=newCost
                pointer+=1

            # if cost of new solution is not good
            # calculate acceptance probability
            else:
                acceptanceProbability=calculateAcceptanceProbability(newCost=newCost,oldCost=cost,currentTemp=currentTemp)
                r=random.uniform(0,1)
                # if acceptance probabiity high enough
                # accept worse solution anymay
                if(r<acceptanceProbability):
                    randomSolution=neighbourSolution
                    cost=newCost
                    pointer+=1

            currentTemp-=ALPHA

        return randomSolution,cost
