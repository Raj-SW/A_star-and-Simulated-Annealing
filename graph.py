from typing import ItemsView
import numpy as np

graph=[]

def getGraphData():
    filePath="./datasets/five_d.txt"
    # filePath="./datasets/gr17_d.txt"

    with open(filePath) as file:

        temp=list(e for e in file)
        for i in range(len(temp)): 
            graph.append((list(map(np.double ,list(x for x in temp[i].split(" ") if x)))))   
          
    return graph      

        
        
        
    

 