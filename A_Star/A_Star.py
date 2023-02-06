from hashlib import new
import random
from A_Star.Node import Node
from graph import getGraphData


class A_star_Search():
    def TraverseGragh(graph,startNodePointer,endNodePointer):
        openList=[]
        closeList=[]
        path=[]
        startNode=Node(pointer=startNodePointer)
        startNode.hN=graph[startNodePointer][endNodePointer]
        endNode=Node(pointer=endNodePointer)
        openList.append(startNode)
 
        while(len(openList)>0):

            #sort list to ascending order in terms of f(n)
            openList.sort(key=lambda x: x.fN, reverse=False)
            #pop smallest f(n) current List
            currentNode=openList.pop(0)
            #append to visited/closed list
            closeList.append(currentNode)

            #if goal node reached, backtrack to find path
            if (currentNode.pointer==endNode.pointer):
                while (currentNode.parent):
                    path.append(currentNode.pointer)
                    currentNode=currentNode.parent
                #add start node pointer as last in the list
                path.append(currentNode.pointer)
                #reversing the list so as to get proper path
                path.reverse()
                #clear openList 
                openList=[]
                #getting goal node since it has least f(n)
                childrenList.sort(key=lambda x: x.fN, reverse=False)

                return path,childrenList[0]
            
            childrenList=[]
            # find children of current node
            for i in  range(len(graph)):
                    # to make sure we do not add current node 
                    # as a child node to itself 
                if (graph[currentNode.pointer][i]!=0 ):
                    childNode = Node(pointer=i,parent=currentNode)
                    # calculate and assign f(n) of each child nodes
                    # assigning g(n)
                    childNode.gN= childNode.parent.gN + graph[childNode.parent.pointer][childNode.pointer]
                    # assigning h(n)
                    childNode.hN= graph[endNodePointer][i]
                    # calculating and assigning f(n)
                    childNode.fN=childNode.gN+childNode.hN
                    childrenList.append(childNode)

            #check if child is already in closedList
            for child in childrenList:
                for visitedNode in closeList:
                    if(child.pointer==visitedNode.pointer):
                        continue

                #check if the child is already in openList else add to open list
                for openNode in openList:
                    if(child.pointer==openNode.pointer and child.gN>openNode.gN):
                        continue
                openList.append(child)


