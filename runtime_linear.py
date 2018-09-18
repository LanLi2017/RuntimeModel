import networkx as nx
import json
import time


G=nx.Graph()

# input the raw dataset as start node
start_node='A'
G.add_node(start_node)


# input the json file (operation steps)
with open('runtime_Model.json','r')as f:
    data=json.load(f)

counter=0
node_list=[]
node_list.append(start_node)

# initialize the starting node
new_node=start_node
for d in data:
    counter+=1
    new_node=chr(ord(start_node)+counter)
    node_list.append(new_node)
    G.add_node(new_node)

# output of the clean dataset as final node
final_node=chr(ord(new_node)+1)
G.add_node(final_node)

# add the edges  [(A,B),(B,C),(C,D)]
node_list.append(final_node)
print(node_list)
edge_list=[]
for i in range(len(node_list)-1):
    edge_list.append((node_list[i],node_list[i+1]))


# How to calculate the linear time: (A->B->C->D)   Just the edges' time....
start_time=time.time()
G.add_edges_from(edge_list)
end_time=time.time()
total_time=end_time-start_time
print('linear time: '+ str(total_time))

# graph it
import matplotlib.pyplot as plt
nx.draw(G)
plt.show()


