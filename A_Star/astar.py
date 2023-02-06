from array import *
# from node import *
from collections import deque
import copy
from Node import Node
#//-------------Function Definitions------------//#

#Function to read the adjacency matrix from the text file
def initializeMatrix():
    #Opens the file in read mode
    file = open("./datasets/gr17_d.txt", "r")
    counter=0
    matrix = []
    #Reads each line in the file
    for line in file.readlines():
        #print(line)
        #Splits each line in the file into a list of float values, white space acting as separator
        edges = [float(i) for i in line.split(" ") if i.strip()]
        #Inserts the list as a row at its corresponding index in the matrix 2D list
        matrix.insert(counter,edges)
        counter+=1 
    file.close()
    #Returns the 2D list
    return matrix
#Function to initialize the list of nodes, children and h(n) values
def initializeListOfNodes(graph, endNode):

    #Initialize a list of nodes
    listNodes=[]
    children=[]
    for i in range(0,len(graph[0]),1):
        listNodes.append(Node(i,graph[i][endNode]))

    #For each node, set their corresponding children list (Any node apart the node itself)
    for i in range(0,len(graph[0]),1):

        children = copy.deepcopy(listNodes)
        children.pop(i)
        listNodes[i].setChildren(children)
        children.clear()
    #Display each node's h(n)  
    for i in range(0,len(graph[0]),1):
        print(str(listNodes[i].value)+ ":" + str(listNodes[i].hn))
                        
    return listNodes

def algorithm():
    print("Algo")
    #variables
    startNode = 0
    endNode = 3 
    graph=initializeMatrix()
    listOfNodes=initializeListOfNodes(graph,endNode)
    goal = listOfNodes[endNode]
    #Start of algo
    listOfNodes[startNode].setGn(0)
    listOfNodes[startNode].calculateFn()
    visited=set()
    frontier=[]
    frontier.append(listOfNodes[startNode])
    while frontier:
        print("------")
        for node in frontier:
            #node being considered
            print("Node being considered:" + str(node.value) + " F(n): " +str(node.fn))
        currentNode = frontier.pop(0)
        if(currentNode.value==goal.value):
            break
        for child in currentNode.children:
            #Get distance from current node and add to cost of parent for g(n)
            distance = graph[currentNode.value][child.value]
            # print(distance)
            child.setGn(distance + currentNode.gn)
            child.calculateFn()
            #child.setParent(currentNode)
            print("fn: " + str(child.value) + " "+ str(child.getFn()) )
            if child.value in visited:
                continue
            frontier.append(child)
        frontier.sort(key=lambda x:x.fn,reverse=False)
        listOfNodes[frontier[0].value].setParent(currentNode.value)
        visited.add(currentNode.value)

    theParent = listOfNodes[endNode].parent
    finalPath=[]
    finalPath.append(endNode)
    while(theParent!=-1):
        finalPath.append(theParent)
        print(theParent)
        theParent= listOfNodes[theParent].parent
    finalPath.reverse()
    print("Final Path: " +str(finalPath) + "Fn: " , currentNode.fn)


#//-------------Main Program----------//#
algorithm()