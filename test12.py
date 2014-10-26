import networkx as nx
import csv
f = open('/Users/dukechan/Downloads/pagerank_centrality.txt','w')
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected-1.csv"
reader = csv.reader(file(csv_file))
G = nx.Graph()
for line in reader:
    G.add_edge(line[4],line[5])
P = nx.pagerank(G)
for item in P:
    f.write("Node: %s Centrality %.10f\n" %(item,P[item]) )
f.close()
