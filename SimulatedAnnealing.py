import random
import numpy as np
from Simulated_Annealing.route import Route


class SimulatedAnnealing():
       
    def Traversal(graph,startNodePointer,endNodePointer):
        Solutions=[]
        currTemp=50
        FINAL_TEMP=1
        MAX_ITERATIONS=50
        iterations=0
        alpha=0.5

        visitedNodes=[]
        currPointer=1
        oldCost=0
        newCost=0
        myRoute=Route(start=startNodePointer,end=endNodePointer)
        visitedNodes.append(startNodePointer)
        
        # get random solution/path
        randomSolution=SimulatedAnnealing.generateRandomPath(graph=graph,start=startNodePointer,end=endNodePointer)
        Solutions.append(randomSolution)
        
        while(currTemp>FINAL_TEMP and iterations<MAX_ITERATIONS):
            # calculate cost of random solution
            oldCost =oldCost+ SimulatedAnnealing.calculateCost(graph=graph,solution=randomSolution,pointer=currPointer,start=startNodePointer)
            # print("old cost ->",oldCost)

            # generate neighbour solution/path
            neighbourSolution=SimulatedAnnealing.generateNeighbourPath(graph=graph,solution=randomSolution,currentPointer=currPointer,visitedNodes=visitedNodes)
            # print("neighbour solution",neighbourSolution)
            Solutions.append(neighbourSolution)

            # calculate the new cost of neighbour solution
            newCost= newCost+ SimulatedAnnealing.calculateCost(graph=graph,solution=neighbourSolution,pointer=currPointer,start=startNodePointer)
            # print("new cost ->",newCost)
            
            # compare costs of the old and new generated solution
            # if newcost is better, newcost is considered
            if(newCost<oldCost):
                randomSolution=neighbourSolution
                oldCost=newCost
                visitedNodes.append(randomSolution[currPointer])
                currPointer+=1
            # if cost of new solution is not good
            # calculate acceptance probability
            else:
                acceptanceProbability=SimulatedAnnealing.calculateAcceptanceProbability(newCost=newCost,oldCost=oldCost,currentTemp=currTemp)
                r=random.randint(0,1)
                # if acceptance probabiity high enough
                # accept worse solution anymay
                if(r<acceptanceProbability):
                    randomSolution=neighbourSolution
                    oldCost=newCost
                    visitedNodes.append(randomSolution[currPointer])
                    currPointer+=1
            iterations=iterations+1
            currTemp = currTemp* alpha

            if(currPointer==len(graph)-1):
                currPointer=1
            
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

        while(loopCount<len(graph[0]) and len(path)<=3):
            if(genNum not in generatedPointers):
                generatedPointers.add(genNum)
                path.append(genNum)
                loopCount+=1
            genNum=random.randint(0,len(graph)-1)
        path.append(end)
        return path

    # this methode generates a whole new set of nodes besides for starting and ending nodes.
    # another school of thought may suggest randomize only next node to be visited
    def generateNeighbourPath(graph,solution,currentPointer,visitedNodes):
        # since the graph is a matrix and 
        # near all nodes are interconnected 
        generatedSet=set()
        generatedSet.add(solution[len(solution)-1])
        # generate random next set of solution        
        for i in range(len(solution)-(currentPointer+1)):
            randomNum=random.randint(0,len(graph)-1)
            while((randomNum in visitedNodes) or (randomNum in generatedSet)):
                randomNum=random.randint(0,len(graph)-1)
            solution[currentPointer]=randomNum
            generatedSet.add(randomNum)
            currentPointer+=1
        return solution

    # cost is calculated by taking the distance from 
    # current node to the next node of the solution
    # and value is returned
    def calculateCost(graph,solution,pointer,start):
        return graph[start][solution[pointer]]

