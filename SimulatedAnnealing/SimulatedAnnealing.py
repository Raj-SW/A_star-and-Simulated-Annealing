import random
from SimulatedAnnealing.GenerateRandomPath import generateRandomPath
from SimulatedAnnealing.CalculateCost import calculateCost
from SimulatedAnnealing.GenerateNeighbourPath import generateNeighbourPath
from SimulatedAnnealing.CalculateAcceptanceProbability import calculateAcceptanceProbability
class SA():
    def Traversal(graph,startNode,endNode):
        currentTemp=50
        FINAL_TEMP=0.1
        iterations=0
        alpha=0.1

        visitedNodes=[]
        pointer=1
        cost=0
        newCost=0
        visitedNodes.append(startNode)

        #generate random solution once
        randomSolution=generateRandomPath(graph=graph,end=endNode,start=startNode)
        print("Random Solution ",randomSolution," cost -> ",cost)
        #generate cost of random solution
        cost=calculateCost(graph=graph,solution=randomSolution,pointer=pointer,start=startNode)            
       
        while(currentTemp>FINAL_TEMP):
            iterations+=1
            if(randomSolution[pointer]==endNode):
                pointer=1
            #generate neighbour solution
            neighbourSolution=generateNeighbourPath(graph=graph,start=startNode,end=endNode,solution=randomSolution,pointer=pointer)
            newCost=calculateCost(graph=graph,solution=neighbourSolution,pointer=pointer,start=startNode)
            print("Neighbour Solution -> ",neighbourSolution," cost -> ",newCost)
            #generate neighbour solution cost
            #compare between two solutions
            if(newCost<cost):
                randomSolution=neighbourSolution
                cost=newCost
                pointer+=1
                print("change 1")
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
                    print("change 2")

            currentTemp-=alpha

        print("pointer -> ", pointer)
        return randomSolution,cost,iterations
