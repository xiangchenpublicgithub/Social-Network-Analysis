# calculate eigenvector  centrality
import snap
f = open('/Users/dukechan/Downloads/result1.txt','w')
txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected.txt"
G = snap.LoadEdgeList(snap.PUNGraph, txt_file, 4, 5)
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(G, NIdEigenH)
for item in NIdEigenH:
    f.write("node: %d centrality: %.10f\n" % (item, NIdEigenH[item]))
f.close()

