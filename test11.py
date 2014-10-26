import networkx as nx
import csv
f = open('/Users/dukechan/Downloads/betweenness_centrality.txt','w')
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected-1.csv"
reader = csv.reader(file(csv_file))
G = nx.Graph()
for line in reader:
    G.add_edge(line[4],line[5])
B = nx.betweenness_centrality(G,1)
for item in B:
    f.write("Node: %s Centrality %.10f\n" %(item,B[item]) )
f.close()
