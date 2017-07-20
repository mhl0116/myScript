from ROOT import *
from array import array
import math
from tdrStyle import *
setTDRStyle()
import sys

gStyle.SetMarkerSize(0.8)

def MakeGraph(txtfile, cut, xIndex1, xIndex2, yIndex, yErrIndex=-1):

    data = [line.strip().split() for line in open(txtfile, 'r') if cut in line]
    print txtfile, cut
    print data
    x,y,xErr,yErr = array('f'),array('f'),array('f'),array('f')
    for i in range(len(data)):
        x.append( (float(data[i][xIndex1]) + float(data[i][xIndex2]) )/2 )
        xErr.append((float(data[i][xIndex2]) - float(data[i][xIndex1]) )/2)
        y.append( float(data[i][yIndex]) )
        if yErrIndex == -1:
           yErr.append( 0 )
        else:
           yErr.append( float(data[i][yErrIndex]) )
    gr = TGraphErrors(len(x),x,y,xErr,yErr)
    return gr

def PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename):

    c = TCanvas("c","",800,800)
    c.SetLogx()
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


def MakeGraphs(txtfiles,cuts,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,indexs,depend,compareAverage=False,tags=["",""]): 

    grs = []
    legends = []
    markerstyle = []
    markercolor = []

    for i in range(len(cuts)):
        cut = cuts[i]
        cut1 = (cut.split())[0]
        cut2 = (cut.split())[1]
        for j in range(len(txtfiles)):
            tag = tags[j]
            txtfile = txtpath+txtfiles[j]
            index = indexs[j]
            grs.append(MakeGraph(txtfile, cut, index[0], index[1], index[2], index[3]))

#            if depend == "pt":
#               grs.append(MakeGraph(txtfile, cut, 0, 1, 4, 5))
#            if depend == "eta":
#               grs.append(MakeGraph(txtfile, cut, 2, 3, 4, 5))

            if txtfiles[j].startswith("Z4L"):
               if depend == "pt":
                  legends.append("Z #rightarrow 4L ("+cut1+" < |#eta| < "+cut2+")")
               if depend == "eta":
                  legends.append("Z #rightarrow 4L ("+cut1+" < pT < "+cut2+")")
               if compareAverage and index[3] == -1: 
                  markercolor.append(2)
               else:
                  markercolor.append(1)
               markerstyle.append(20)

            if "H4L" in txtfiles[j]:
               if depend == "pt":
                  legends.append("H #rightarrow 4L ("+cut1+" < |#eta| < "+cut2+")")
               if depend == "eta":
                  legends.append("H #rightarrow 4L ("+cut1+" < pT < "+cut2+")")
               markercolor.append(2)
               markerstyle.append(24)

            if "ZZ4L" in txtfiles[j]:
               if depend == "pt":
                  legends.append("ZZ #rightarrow 4L ("+cut1+" < |#eta| < "+cut2+")")
               if depend == "eta":
                  legends.append("ZZ #rightarrow 4L ("+cut1+" < pT < "+cut2+")")
               markercolor.append(2)
               markerstyle.append(24)

            legends[-1] = legends[-1] + tag
            if len(tag) > 0: markercolor[-1] = 4

        if depend == "pt":
           savename_tag = savename + "eta_" + cut1 + "_" + cut2
        if depend == "eta":
           savename_tag = savename + "pT_" + cut1 + "_" + cut2
        print legends
        PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename_tag)
        del grs[:]
        del legends[:]


#PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename)
#MakeGraph(txtfile, cut, xIndex1, xIndex2, yIndex, yErrIndex=-1)
#def MakeGraphs(txtfiles,cuts,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,indexs,depend,compareAverage=False,tags=["",""]):

#savename = "pTCurvature_H4LZ4L_"
savename = "pTResidual_H4LZ4L_"
savepath = "/home/mhl/public_html/2017/20170719_summary/"
txtpath = "/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
drawOption = "ep"
xMin = 4.9999
xMax = 100.0001
yMin = -0.004
yMax = 0.008
xTitle = "p_{T}^{gen}"
yTitle = "(pT_{Reco}-pT_{Gen})/pT_{Gen}"
#yTitle = "(1/pT_{Reco} - 1/pT_{Gen})/(1/pT_{Gen})"

#txtfiles = ["Z4L_muPtCurvature_muPlus.txt","Z4L_muPtCurvature_muMinus.txt"]
txtfiles = ["Z4L_muPtResidual_muPlus.txt","Z4L_muPtResidual_muMinus.txt"]
tags = ["plus muon","minus muon"]
markerstyle = [20,24]
markercolor = [1,2]
cuts = [" 0.0 0.9 ", " 0.9 2.4 "]
indexs = [0,1,4,5]

for i in range(len(cuts)):
    gr1 = MakeGraph(txtpath + txtfiles[0], cuts[i], indexs[0], indexs[1], indexs[2], indexs[3])
    gr2 = MakeGraph(txtpath + txtfiles[1], cuts[i], indexs[0], indexs[1], indexs[2], indexs[3])
    grs = [gr1,gr2]
    legends = [(cuts[i].split())[0] + " < |#eta| < " + (cuts[i].split())[1] + ", " + tags[0], \
               (cuts[i].split())[0] + " < |#eta| < " + (cuts[i].split())[1] + ", " + tags[1] ]
    savename_tag = savename + "eta_" + (cuts[i].split())[0] + "_" + (cuts[i].split())[1]
    PlotGraph(grs,legends,markerstyle,markercolor,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,savename_tag)

