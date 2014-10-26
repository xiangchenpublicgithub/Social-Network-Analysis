import snap
f = open('/Users/dukechan/Downloads/result2.txt','w')
f2 = open('/Users/dukechan/Downloads/result3.txt','w')
txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected.txt"
G = snap.LoadEdgeList(snap.PUNGraph, txt_file, 4, 5)
print "1"
Nodes = snap.TIntFltH()
print "2"
Edges = snap.TIntPrFltH()
print "3"
snap.GetBetweennessCentr(G, Nodes, Edges, 500.0)
print "4"



