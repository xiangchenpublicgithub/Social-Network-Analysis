# calculate closeness centrality
import snap
f = open('/Users/dukechan/Downloads/closeness_centrality.txt','w')
txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected-1.txt"
G = snap.LoadEdgeList(snap.PUNGraph, txt_file, 4, 5)
for NI in G.Nodes():
    CloseCentr = snap.GetClosenessCentr(G, NI.GetId())
    f.write("node: %d centrality: %f\n" % (NI.GetId(), CloseCentr))
f.close()
