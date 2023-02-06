import matplotlib.pyplot as plt
from graph import getGraphData
import networkx as nx

graph=getGraphData()
adjacencygraph={}

count=0
for i in graph:
    adjacencygraph[count]=i
    count+=1

print(adjacencygraph)

g = nx.Graph()

count=0
count2=0
while(count<len(graph)):
    while(count2<len(graph)):
        print("count",count,"count2",count2,"graphdata",graph[count][count2])
        if(graph[count][count2]!=0):
            g.add_edge(count,count2,attr=graph[count][count2],weight=graph[count][count2])
        count2+=1
    count2=0
    count+=1
# labels = nx.get_edge_attributes(g,'weight')

nx.draw_spring(g,with_labels=True)

plt.show()