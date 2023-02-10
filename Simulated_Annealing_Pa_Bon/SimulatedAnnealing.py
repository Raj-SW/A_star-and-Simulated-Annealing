import random
import numpy as np
from Simulated_Annealing.route import Route


class SimulatedAnnealing():
       
    def Traversal(graph,startNodePointer,endNodePointer):
        Solutions=[]
        currTemp=50
        FINAL_TEMP=1
        MAX_ITERATIONS=3
        iterations=0
        alpha=0.5

        visitedNodes=[]
        currPointer=1
        oldCost=0
        newCost=0
        visitedNodes.append(startNodePointer)
        
        # get random solution/path
        randomSolution=SimulatedAnnealing.generateRandomPath(graph=graph,start=startNodePointer,end=endNodePointer)
        
        while( iterations<MAX_ITERATIONS):
            # calculate cost of random solution
            oldCost =oldCost+ SimulatedAnnealing.calculateCost(graph=graph,solution=randomSolution,pointer=currPointer,start=startNodePointer)
            # print("old cost ->",oldCost)

            # generate neighbour solution/path
            neighbourSolution=SimulatedAnnealing.generateNeighbourPath(graph=graph,solution=randomSolution,currentPointer=currPointer,visitedNodes=visitedNodes,start=startNodePointer,end=endNodePointer)
            # print("neighbour solution",neighbourSolution)

            # calculate the new cost of neighbour solution
            newCost= newCost+ SimulatedAnnealing.calculateCost(graph=graph,solution=neighbourSolution,pointer=currPointer,start=startNodePointer)
            # print("new cost ->",newCost)
            
            # compare costs of the old and new generated solution
            # if newcost is better, newcost is considered
            # if(newCost<oldCost):
            #     randomSolution=neighbourSolution
            #     oldCost=newCost
            #     visitedNodes.append(randomSolution[currPointer])
            #     currPointer+=1
            # # if cost of new solution is not good
            # # calculate acceptance probability
            # else:
            #     acceptanceProbability=SimulatedAnnealing.calculateAcceptanceProbability(newCost=newCost,oldCost=oldCost,currentTemp=currTemp)
            #     r=random.randint(0,1)
            #     # if acceptance probabiity high enough
            #     # accept worse solution anymay
            #     if(r<acceptanceProbability):
            #         randomSolution=neighbourSolution
            #         oldCost=newCost
            #         visitedNodes.append(randomSolution[currPointer])
            #         currPointer+=1
            iterations=iterations+1
            currTemp = currTemp* alpha

            if(currPointer==len(graph)-1):
                currPointer=1
            
            print()
            print("Random Solution ->",randomSolution)
            print()
            print("Neighbour Solution ->",neighbourSolution)

        return randomSolution,oldCost,iterations


    def calculateAcceptanceProbability(oldCost,newCost,currentTemp):
        return np.exp((oldCost-newCost)/currentTemp)
        
    def generateRandomPath(graph,start,end):
        # generate random solution
        # start and ending node already given, 
        # intermediary numbers to be generated 
        path=[]
        path.append(start)

        generatedPointers=set()
        generatedPointers.add(start)
        generatedPointers.add(end)
        
        genNum=random.randint(0,len(graph)-1)
        loopCount=0

        while(len(path)!=(len(graph[0])-1)):
            if(genNum not in generatedPointers):
                generatedPointers.add(genNum)
                path.append(genNum)
                loopCount+=1
            genNum=random.randint(0,len(graph)-1)
        path.append(end)
        return path

    # this methode generates a whole new set of nodes besides for starting and ending nodes.
    # another school of thought may suggest randomize only next node to be visited
    def generateNeighbourPath(graph,solution,currentPointer,visitedNodes,start,end):
        # since the graph is a matrix and 
        # near all nodes are interconnected 
        neighbourPath=solution
        generatedSet=set()
        generatedSet.add(start)
        generatedSet.add(end)
        num=random.randint(0,len(graph)-1)
        # generate random next set of solution        
        while(num in generatedSet and num in solution[0:currentPointer]):
            num=random.randint(0,len(graph)-1)
        solution[currentPointer]=num
        return solution

    # cost is calculated by taking the distance from 
    # current node to the next node of the solution
    # and value is returned
    def calculateCost(graph,solution,pointer,start):
        return graph[start][solution[pointer]]

