# import random
# import numpy as np
# from Simulated_Annealing.route import Route


# class SimulatedAnnealing2():
       
#     def Traversal(graph,startNodePointer,endNodePointer):
#         currTemp=5000
#         FINAL_TEMP=0.001
#         MAX_ITERATIONS=5
#         iterations=0
#         alpha=0.9
#         visitedNodes=[]
#         currPointer=1
#         visitedNodes.append(startNodePointer)
#         path=[]
#         path.append(startNodePointer)
#         currSolution=[]
#         neighbourSolution=[]
#         currCost=0
#         neighbourCost=0

#         #create intial solution
#         currSolution=SimulatedAnnealing2.generateRandomPath(graph=graph,start=startNodePointer,end=endNodePointer,pointer=currPointer,path=path)

#         while(currTemp>FINAL_TEMP):
#             iterations+=1
#             print("currSolution",currSolution,len(currSolution))
#             print("iteration",iterations)
#             print("pointer",currPointer)
#             # calculate cost of random solution
#             currCost += SimulatedAnnealing2.calculateCost(graph=graph,pointer=currPointer,start=startNodePointer,solution=currSolution)
#             # generate neighbour solution/path
#             neighbourSolution=SimulatedAnnealing2.generateNeighbourPath(graph=graph,currPointer=currPointer,currSolution=currSolution,start=startNodePointer)
#             # calculate the new cost of neighbour solution
#             neighbourCost += SimulatedAnnealing2.calculateCost(graph=graph,solution=neighbourSolution,pointer=currPointer,start=startNodePointer)
#             # compare costs of the old and new generated solution
#             # if newcost is better, newcost is considered
#             if(neighbourCost<currCost or neighbourSolution[currPointer]==endNodePointer):
#                 print("")    
#             # if cost of new solution is not good
#             # calculate acceptance probability
#             else:
#                 acceptanceProbability=SimulatedAnnealing2.calculateAcceptanceProbability(newCost=neighbourCost,oldCost=currCost,currentTemp=currTemp)
#                 r=random.randint(0,1)
#                 # if acceptance probabiity high enough
#                 # accept worse solution anymay
#                 if(r<acceptanceProbability):
#                     print("")
#             if(currPointer==len(graph)-1):
#                 currPointer=1
#             currTemp*=alpha

#         return currSolution,currCost,iterations


#     def calculateAcceptanceProbability(oldCost,newCost,currentTemp):
#         return np.exp((oldCost-newCost)/currentTemp)
        
#     def generateRandomPath(graph,start,end,pointer,path):
 
#         if(len(path)==len(graph)):
#             return path

#         genNum=random.randint(0,len(graph)-1)
#         while(genNum in path or graph[start][genNum]==0):
#             genNum = random.randint(0,len(graph)-1)
#             print("here")

#         path.append(genNum)

#         return path

#     # # this methode generates a whole new set of nodes besides for starting and ending nodes.
#     # # another school of thought may suggest randomize only next node to be visited
# #     def generateNeighbourPath(graph,currPointer,currSolution,start):
# #         neighbourPath=currSolution
# #         rndNode=random.randint(0,len(graph)-1)

# #         if(len(currSolution)==len(graph)):
# #             return currSolution
        
# #         while(rndNode in currSolution or graph[start][currPointer]==0 or currSolution[currPointer]==rndNode):
# #             rndNode=random.randint(0,len(graph)-1)
# #             print("there")

# #         neighbourPath.pop(currPointer)
# #         neighbourPath.append(rndNode)

# #         return neighbourPath

#     # cost is calculated by taking the distance from 
#     # current node to the next node of the solution
#     # and value is returned
#     def calculateCost(graph,solution,pointer,start):
#         return graph[solution[pointer-1]][solution[pointer]]
        

