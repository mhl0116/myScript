from ROOT import *
from array import array
import math
from tdrStyle import *
setTDRStyle()
import sys

def MakeGraph(txtfile, cut, xIndex1, xIndex2, yIndex, yErrIndex):

    data = [line.strip().split() for line in open(txtfile, 'r') if cut in line]

    x,y,xErr,yErr = array('f'),array('f'),array('f'),array('f')
    for i in range(len(data)):
        x.append( (float(data[i][xIndex1]) + float(data[i][xIndex2]) )/2 )
        xErr.append((float(data[i][xIndex2]) - float(data[i][xIndex1]) )/2)
        y.append( float(data[i][yIndex]) )
        yErr.append( float(data[i][yErrIndex]) )
    gr = TGraphErrors(len(x),x,y,xErr,yErr)
    return gr

def PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename):

    c = TCanvas("c","",800,800)
#    c.SetLogy()
    c.SetLeftMargin(0.20)
    dummy = TH1D("dummy","dummy",1,xMin,xMax)
    dummy.SetMinimum(yMin)
    dummy.SetMaximum(yMax)
    dummy.SetLineColor(0)
    dummy.SetMarkerColor(0)
    dummy.SetLineWidth(0)
    dummy.SetMarkerSize(0)
    dummy.GetXaxis().SetTitle(xTitle)
    dummy.GetYaxis().SetTitleOffset(2)
    dummy.GetYaxis().SetTitle(yTitle)
    dummy.Draw()

    for i in range(len(grs)):
        grs[i].Draw(drawOption)
        grs[i].SetMarkerStyle(markerstyle[i])
        grs[i].SetMarkerColor(markercolor[i])

    legend = TLegend(0.2,0.7,0.7,0.9)
    
    for i in range(len(legends)):
        legend.AddEntry(grs[i], legends[i], drawOption)
  
    legend.SetTextSize(0.03)
    legend.SetLineWidth(1)
    legend.SetFillColor(0)
    legend.SetBorderSize(1)
    legend.Draw()

    c.SaveAs(savepath + savename + ".png")
    c.SaveAs(savepath + savename + ".pdf")


txtpath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
txtfiles = ["Z4L_muPtResidual.txt","H4L_muPtResidual.txt"]
drawOption = "ep"
savepath = "/home/mhl/public_html/2017/20170505_checkResiduals/"
savename = "pTResiduals_H4L_Z4L"

xMin = 0
xMax = 100
yMin = -0.004
yMax = 0.004
xTitle = "p_{T}^{gen}"
yTitle = "(pT_{Reco}-pT_{Gen})/pT_{Gen}"

cuts = [" 0.0 0.9 ", " 0.9 1.8 ", " 1.8 2.4 "]
grs = []
legends = []
markerstyle = []
markercolor = []

for i in range(len(cuts)):
    for j in range(len(txtfiles)):
        cut = cuts[i]
        txtfile = txtpath+txtfiles[j]
        grs.append(MakeGraph(txtfile, cut, 0, 1, 4, 5))
        eta1 = (cut.split())[0]
        eta2 = (cut.split())[1]
        if "Z4L" in txtfiles[j]:
           legends.append("Z #rightarrow 4L ("+eta1+" < |#eta| < "+eta2+")")
           markercolor.append(1)
           markerstyle.append(20)
        if "H4L" in txtfiles[j]:
           legends.append("H #rightarrow 4L ("+eta1+" < |#eta| < "+eta2+")")
           markercolor.append(2)
           markerstyle.append(24)
        savename_tag = savename + "eta_" + eta1 + "_" + eta2
    PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename_tag)
    del grs[:]
    del legends[:]

print "NEED LOG !!!"
