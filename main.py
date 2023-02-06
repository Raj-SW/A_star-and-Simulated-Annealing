import random
from SimulatedAnnealing import SimulatedAnnealing
from graph import getGraphData
from A_Star.Node import Node
from A_Star.A_Star import A_star_Search

def main():
    graphData=getGraphData()
    nodeCount=0
    
    for i in graphData:
        print(i)
        nodeCount+=1
    print()
    print("Number of nodes found ->",nodeCount)
    print()

    # randomly generating start node and end node
    start_node_pointer= random.randint(0,len(graphData)-1)
    end_node_pointer= random.randint(0,len(graphData)-1)
    while (start_node_pointer==end_node_pointer):
        end_node_pointer= random.randint(0,len(graphData)-1)  


    # solution1=A_star_Search.TraverseGragh(graph=graphData,startNodePointer=start_node_pointer,endNodePointer=end_node_pointer)  
    # print("Using A* Algorithm Traversal")
    # print()
    # print("Start node is Node Number ->",start_node_pointer)
    # print()
    # print("End node is Node Number ->",end_node_pointer)
    # print()
    # print("Shortest path is -> ",solution1[0])
    # print()
    # print("Cost for path -> ",solution1[1].fN)
    # print()
    print("Using Simulated Annealing Algorithm")
    print()
    print("Start node is Node Number ->",start_node_pointer)
    print()
    print("End node is Node Number ->",end_node_pointer)
    print()
    solution2 = SimulatedAnnealing.Traversal(graph=graphData,startNodePointer=start_node_pointer,endNodePointer=end_node_pointer)
    print("Optimal path is -> ",solution2[0])
    print()
    print("Global minima/Cost of optimal path is -> ",solution2[1])
    print()
    print("Number of iterations -> ",solution2[2])



main()