# A-> B -> C (-> D)
# A-> B
# A-> C
# B AND C ARE PARALLEL
from multiprocessing import Pool

import networkx as nx
import json
import time
import matplotlib.pyplot as plt

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

# # node_list: ['A','B','C','D'] edges [('A','B'),('A','C')]
node_list.append(final_node)

# add edges function :  [ add_edges('A','B'), add_edges('A','C')]
# How to calculate the parallel time: [func(A->B); func(A->C)]


def add_edges(G,a):
    return G.add_edges_from([a])


def serial(GL,node_list):
    return [add_edges(GL,edge) for edge in node_list]


def multiprocess(processes,node_list):
    with Pool(processes) as p:
        p.map(add_edges,node_list)
    # pool=mp.Pool(processes=processes)
    # print(node_list)
    # [pool.apply_async(add_edges,args=(edge))for edge in node_list]


def main():
    # add the linear edges  [(A,B),(B,C),(C,D)]
    Lnode_list=[]
    for i in range(len(node_list)-1):
        Lnode_list.append((node_list[i],node_list[i+1]))
    print(Lnode_list)




    #add the parallel structure edges [(A,B),(A,C)]
    Pnode_list=[]
    for node in node_list[1:(len(node_list)-1)]:
        tuple=(start_node,node)
        Pnode_list.append(tuple)
    print(Pnode_list)

    # GL=G.copy()
    # serial(GL,Lnode_list)

    # GSP=G.copy()
    multiprocess(4,Pnode_list)
    # start_time=time.time()
    # for edge in Pnode_list:
    #     add_edges(edge)
    # end_time=time.time()
    # print(start_time-end_time)

    # [('A', 'B'), ('A', 'C')]
    print('submitted tasks to pool')
    start_time=time.time()


    end_time=time.time()
    total_time=end_time-start_time
    print('SP time: '+str(total_time))





if __name__=='__main__':
    main()








