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

#txtfiles = ["Z4L_muCurveResidual_pt_fullRange.txt","H4L_muCurveResidual_pt_fullRange.txt"]
#txtfiles = ["Z4L_muCurveResidual_pt_fullRange.txt","ZZ4L_muCurveResidual_pt_fullRange.txt"]
#txtfiles = ["Z4L_muPtResidual_pt_fullRange.txt","H4L_muPtResidual_pt_fullRange.txt"]
#txtfiles = ["Z4L_muPtResidual_pt_fullRange.txt","ZZ4L_muPtResidual_pt_fullRange.txt"]
#txtfiles = ["Z4L_muPtResidual_pt_checkEta.txt","H4L_muPtResidual_pt_checkEta.txt"]
#txtfiles = ["Z4L_muPtResidual_pt_checkEta.txt","ZZ4L_muPtResidual_pt_checkEta.txt"]
#txtfiles = ["Z4L_muPtResidual_pt_lowPt.txt","H4L_muPtResidual_pt_lowPt.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_allM4l_eta_0p0_0p9.txt","H4L_muPtResidual_allM4l_allM4l_eta_0p0_0p9.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_allM4l_lowPt_eta.txt","H4L_muPtResidual_allM4l_allM4l_lowPt_eta.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_allM4l_lowPt_eta_0p0_2p4.txt","H4L_muPtResidual_allM4l_allM4l_lowPt_eta_0p0_2p4.txt"]
#txtfiles = ["Z4L_muCurveResidual_pt_nofsr_allM4l_lowPt_eta.txt","H4L_muCurveResidual_pt_nofsr_allM4l_lowPt_eta.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_allM4l.txt","Z4L_muPtResidual_allM4l_allM4l.txt"]#"H4L_muPtResidual_allM4l_combine124_125_126_allM4l_combine_124_125_126.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_Z2AT4_allM4l.txt","H4L_muPtResidual_allM4l_Z2AT4_allM4l.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_combine_ggH_zz4L_allM4l_combine_ggH_zz4L.txt", "Z4L_muPtResidual_allM4l_combine_ggH_zz4L_allM4l_combine_ggH_zz4L.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_Z2AT4.txt","H4L_muPtResidual_allM4l_Z2AT4.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4.txt","Z4L_muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4_L4.txt","Z4L_muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4_L4.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_combine_ggH124_125_126_zz4L_Z2AT12.txt","Z4L_muPtResidual_allM4l_combine_ggH124_125_126_zz4L_Z2AT12.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4_L34_pt_9_10_11.txt","Z4L_muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4_L234_pt_19_20_21.txt"]
#txtfiles = ["H4L_muPtResidual_allM4l_MuPt4_Z2AT4_withFSR.txt","H4L_muPtResidual_allM4l_MuPt4_Z2AT4_noFSR.txt"]
#txtfiles = ["Z4L_muPtResidual_allM4l_MuPt4_Z2AT4_withFSR.txt","Z4L_muPtResidual_allM4l_MuPt4_Z2AT4_withFSR.txt"]
txtfiles = ["Z4L_muPtCurvature_muPlus.txt","Z4L_muPtCurvature_muPlus.txt"]

#savename = "pTResiduals_Z4L_ZZ4L_"
#savename = "pTResiduals_Z4L_H4L_"
#savename = "pTResiduals_Z4L_ZZ4L_checkEta_"
#savename = "pTResiduals_Z4L_H4L_oneEtaBin_"
#savename = "pTResiduals_combine_ggH_ZZ4L_"
#savename = "pTResiduals_Z2AT4_Z4LOnly_compareWithAverage"
#savename = "pTResiduals_Z4L_noFSR_compareAverage_"
savename = "pTCurvature_H4LZ4L_"

savepath = "/home/mhl/public_html/2017/20170719_summary/"
txtpath = "/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"

drawOption = "ep"
xMin = 0.01#4.9999
xMax = 0.2#100.0001
yMin = -0.004
yMax = 0.004
#yMin = 0
#yMax = 15
xTitle = "1/p_{T}^{gen}"#"p_{T}^{gen}"
#xTitle = "|#eta|"
#yTitle = "(pT_{Reco}-pT_{Gen})/(pT_{Gen})"
yTitle = "(1/pT_{Reco}-1/pT_{Gen})/(1/pT_{Gen})"

#cuts = [" 0.0 2.4 "]
#cuts = [" 0.0 0.9 ", " 0.9 1.4 " , " 1.4 2.4 "]
cuts = [" 0.0 0.9 ", " 0.9 2.4 "]
#cuts = ["15 50 "]

#MakeGraphs(txtfiles,cuts,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,[[0,1,7,-1],[0,1,7,-1]],"pt",True,["","_noFSR"])
MakeGraphs(txtfiles,cuts,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,[[0,1,4,5],[0,1,4,5]],"pt",False,["",""])#"_noFSR"])
#MakeGraphs(txtfiles,cuts,drawOption,xMin,xMax,xTitle,yMin,yMax,yTitle,savepath,"eta")
#            if depend == "pt":
#               grs.append(MakeGraph(txtfile, cut, 0, 1, 4, 5))
#            if depend == "eta":
#               grs.append(MakeGraph(txtfile, cut, 2, 3, 4, 5))

print "NEED LOG !!!"
