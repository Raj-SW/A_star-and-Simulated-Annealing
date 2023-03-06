def calculateCost(graph,solution):
    cost=0
    for i in range(1,len(solution),1):
        cost+=graph[solution[i]][solution[i-1]]
    cost+=graph[solution[0]][solution[len(solution)-1]]
    return cost
    