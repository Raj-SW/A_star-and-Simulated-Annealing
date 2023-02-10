import random

def generateNeighbourPath(graph,start,end,pointer,solution):
    loop=0
    path=[]
    #path.append(start)

    generatedNodes=set()
    generatedNodes.add(start)
    generatedNodes.add(end)

    for i in range(pointer):
        path.append(solution[i])
    
    generated=random.randint(0,len(graph)-1)

    while(len(path)<(len(solution)-1)):
        if((generated not in generatedNodes) and (generated not in path)):
            path.append(generated)
            generatedNodes.add(generated)    
        generated=random.randint(0,len(graph)-1)
    path.append(end)
    
    return path
