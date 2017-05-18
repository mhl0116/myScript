from ROOT import *
from array import array
import math
from tdrStyle import *
setTDRStyle()
import sys

def MakeGraph(txtfile, cut, xIndex1, xIndex2, yIndex, yErrIndex):

    data = [line.strip().split() for line in open(txtfile, 'r') if cut in line]
    print txtfile, cut
    print data
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
    c.SetGridy()
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
    dummy.GetXaxis().SetNdivisions(505)
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

#txtfiles = ["Z4L_muCurveResidual_pt_fullRange.txt","H4L_muCurveResidual_pt_fullRange.txt"]
#txtfiles = ["Z4L_muCurveResidual_pt_fullRange.txt","ZZ4L_muCurveResidual_pt_fullRange.txt"]
txtfiles = ["Z4L_muCurveResidual_pt_checkEta.txt","H4L_muCurveResidual_pt_checkEta.txt"]
#txtfiles = ["Z4L_muCurveResidual_pt_checkEta.txt","ZZ4L_muCurveResidual_pt_checkEta.txt"]
#savename = "pTResiduals_Z4L_ZZ4L_"
#savename = "pTResiduals_Z4L_H4L_"
#savename = "pTResiduals_Z4L_ZZ4L_checkEta_"
savename = "pTResiduals_Z4L_H4L_checkEta_"

savepath = "/home/mhl/public_html/2017/20170518_muCurveResidual_pt/"
txtpath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"

drawOption = "ep"
xMin = 0
xMax = 2.4
yMin = -0.004
yMax = 0.004
#yMin = 0
#yMax = 15
#xTitle = "1/p_{T}^{gen}"
xTitle = "|#eta|"
yTitle = "(1/pT_{Reco}-1/pT_{Gen})/(1/pT_{Gen})"
#yTitle = "fitted n2"

#cuts = [" 0.9 1.1 ", " 1.1 1.4 "]
#cuts = [" 0.0 2.4 "]
#cuts = [" 0.0 0.5 ", " 0.5 0.9 ", " 0.9 1.5 ", " 1.5 2.4 "]
#cuts = [" 0.0 0.5 ", " 0.5 0.7 ", " 0.7 0.9 ", " 0.9 1.4 ", " 1.4 2.4 "]
#cuts = [" 0.0 0.9 ", " 0.9 1.4 ", " 1.4 2.4 "]
#cuts = [" -2.4 -1.4 ", " -1.4 -0.9 ", " -0.9 0.0 ", " 0.0 0.9 ", " 0.9 1.4 ", " 1.4 2.4 "]
cuts = ["0.04 0.08 "]
#cuts = [" 0.0 0.2 "]
grs = []
legends = []
markerstyle = []
markercolor = []

for i in range(len(cuts)):
    for j in range(len(txtfiles)):
        cut = cuts[i]
        txtfile = txtpath+txtfiles[j]
        grs.append(MakeGraph(txtfile, cut, 2, 3, 4, 5))
#        grs.append(MakeGraph(txtfile, cut, 0, 1, 4, 5))
        cut1 = (cut.split())[0]
        cut2 = (cut.split())[1]
        if txtfiles[j].startswith("Z4L"):
#           legends.append("Z #rightarrow 4L ("+cut1+" < |#eta| < "+cut2+")")
           legends.append("Z #rightarrow 4L ("+cut1+" < 1/pT < "+cut2+")")
           markercolor.append(1)
           markerstyle.append(20)

        if "H4L" in txtfiles[j]:
#           legends.append("H #rightarrow 4L ("+cut1+" < |#eta| < "+cut2+")")
           legends.append("H #rightarrow 4L ("+cut1+" < 1/pT < "+cut2+")")
           markercolor.append(2)
           markerstyle.append(24)

        if "ZZ4L" in txtfiles[j]:
#           legends.append("ZZ #rightarrow 4L ("+cut1+" < |#eta| < "+cut2+")")
           legends.append("ZZ #rightarrow 4L ("+cut1+" < 1/pT < "+cut2+")")
           markercolor.append(2)
           markerstyle.append(24)

#        savename_tag = savename + "eta_" + cut1 + "_" + cut2
        savename_tag = savename + "pT_" + cut1 + "_" + cut2
    print legends
    PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename_tag)
    del grs[:]
    del legends[:]

print "NEED LOG !!!"
