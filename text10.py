import networkx as nx
import csv
import scipy
import numpy
f = open('/Users/dukechan/Downloads/eigenvector_centrality.txt','w')
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected-1.csv"
reader = csv.reader(file(csv_file))
G = nx.Graph()
for line in reader:
    G.add_edge(line[4],line[5])
E = nx.eigenvector_centrality_numpy(G)
for item in E:
    f.write("Node: %s Centrality %.10f\n" %(item,E[item]) )
f.close()
