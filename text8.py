##  calculate indegree and outdegree centrality
import networkx as nx
import csv
f = open('/Users/dukechan/Downloads/indegree_centrality.txt','w')
f2 = open('/Users/dukechan/Downloads/outdegree_centrality.txt','w')
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_directed-1.csv"
reader = csv.reader(file(csv_file))
G = nx.DiGraph()
for line in reader:
    G.add_edge(line[4],line[5])
In = nx.in_degree_centrality(G)
for item in In:
    f.write("Node: %s Centrality %.10f\n" %(item,In[item]) )
f.close()
Out = nx.out_degree_centrality(G)
for item in Out:
    f2.write("Node: %s Centrality %.10f\n" %(item,Out[item]) )
f2.close()