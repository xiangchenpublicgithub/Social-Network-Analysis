##  calculate indegree and outdegree centrality----Fail   So I choose NetworkX
import snap
txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_directed.txt"
f = open('/Users/dukechan/Downloads/result4.txt','w')
f2 = open('/Users/dukechan/Downloads/result5.txt','w')
G = snap.LoadEdgeList(snap.PNGraph, txt_file, 4, 5)
InDegV = snap.TIntPrV()
OutDegV = snap.TIntPrV()
snap.GetNodeInDegV(G, InDegV)
snap.GetNodeOutDegV(G, OutDegV)
# indegree
for item in InDegV:
    DegCentr = snap.GetDegreeCentr(G, item.GetVal1())
    f.write("node: %d centrality: %f\n" % (item.GetVal1(), DegCentr))
f.close()
# outdegree
for item in OutDegV:
    DegCentr = snap.GetDegreeCentr(G, item.GetVal1())
    f2.write("node: %d centrality: %f\n" % (item.GetVal1(), DegCentr))
f2.close()


# problem :    centrality is  0    why????????