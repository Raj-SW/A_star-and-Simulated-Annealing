import random

def generateRandomPath(graph,start,end):
    path=[]
    path.append(start)

    generatedNodes=set()
    generatedNodes.add(start)
    generatedNodes.add(end)

    generated=random.randint(0,len(graph)-1)

    while(len(path)!=(len(graph) - 1)):
        if(generated not in generatedNodes):
            path.append(generated)
            generatedNodes.add(generated)    
        generated=random.randint(0,len(graph)-1)
    path.append(end)
    return path