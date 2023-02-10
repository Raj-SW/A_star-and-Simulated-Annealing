def calculateCost(graph,solution,pointer,start):
    cost=0
    print(solution)
    for i in range(1,len(solution),1):
        cost+=graph[solution[i]][solution[i-1]]
        print("distance from",solution[i-1]," to ", solution[i]," graph ", graph[solution[i]][solution[i-1]])
    cost+=graph[solution[0]][solution[len(solution)-1]]
    print("Final cost ",cost)
    # while(pointer>0):
    #     cost+=graph[solution[pointer-1]][solution[pointer]]
    #     pointer-=1
    return cost
    