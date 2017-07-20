from ROOT import *
from array import array
from tdrStyle import *
setTDRStyle()

fileName = 'Zmumu_rawreco_2012D.root'
beforeHist = 'nSeg_lumi'
afterHist = 'nInTimeSeg_lumi'
rebin = 10
xmin = 0
xmax = 50
ymin = 1.1
ymax = 1.3
xTitle = 'lumi'
yTitle = 'Segment'

def makeplot(fileName,beforeHist,afterHist,rebin,xmin,xmax,ymin,ymax,xTitle,yTitle,saveName):
 gStyle.SetOptFit(0000)
 inputFile = TFile(fileName)

 h_before = inputFile.Get(beforeHist)
 h_after = inputFile.Get(afterHist)

 h_before.RebinX(rebin)
 h_after.RebinX(rebin)


 h_before.Sumw2()
 h_after.Sumw2()

 h_before_pfx = h_before.ProfileX("h_before_pfx", 1, -1)
 h_after_pfx = h_after.ProfileX("h_after_pfx", 1, -1)

 x,xErr = array('f'),array('f')
 y1,y1Err = array('f'),array('f')
 y2,y2Err = array('f'),array('f')

 for i in range(h_before_pfx.GetSize()):
#    print h_before_pfx.GetXaxis().GetBinCenter(i)
#    print h_before_pfx.GetBinContent(i), h_after_pfx.GetBinContent(i)
#    print h_before_pfx.GetBinContent(i)-0.5, h_after_pfx.GetBinContent(i)-0.5
#    print h_before_pfx.GetBinError(i), h_after_pfx.GetBinError(i)
    if h_before_pfx.GetXaxis().GetBinCenter(i) < 2: continue

    x.append(h_before_pfx.GetXaxis().GetBinCenter(i))
    xErr.append(0)
    y1.append(h_before_pfx.GetBinContent(i)-0.5)
    y2.append(h_after_pfx.GetBinContent(i)-0.5)
    y1Err.append(h_before_pfx.GetBinError(i))
    y2Err.append(h_after_pfx.GetBinError(i))
 
 gr_before = TGraphErrors(len(x),x,y1,xErr,y1Err)
 gr_after = TGraphErrors(len(x),x,y2,xErr,y2Err)

 c = TCanvas('c', '', 800, 800)

 c.SetGrid()
 dummy = TH1D("dummy","dummy",1,xmin,xmax)
 dummy.SetMinimum(ymin)
 dummy.SetMaximum(ymax)
 dummy.SetLineColor(0)
 dummy.SetMarkerColor(0)
 dummy.SetLineWidth(0)
 dummy.SetMarkerSize(0)
 dummy.GetYaxis().SetTitle(yTitle)
 dummy.GetXaxis().SetTitle(xTitle)
# dummy.GetXaxis().SetLabelOffset(0.015)
 dummy.Draw()

 gr_before.SetMarkerStyle(20)
 gr_after.SetMarkerStyle(20)
 gr_before.SetMarkerColor(1)
 gr_after.SetMarkerColor(2)
 gr_before.SetLineWidth(2)
 gr_after.SetLineWidth(2)
 gr_before.SetLineColor(1)
 gr_after.SetLineColor(2)

 gr_before.Draw('pe same')
 gr_after.Draw('pe same')

 gr_before.Fit('pol1','','',0,50)
 pol1.SetLineColor(1)
 pol1.SetLineWidth(2)
 gr_before.Fit('pol1','','',0,50)
 pol1.SetLineColor(2)
 pol1.SetLineWidth(2)
 gr_after.Fit('pol1','','',0,50)

 legend = TLegend(.13,.8,.6,.9)
 legend.SetTextColor(1)
 legend.AddEntry(gr_before, 'Current Reconstruction', "pl")
 legend.AddEntry(gr_after, 'Narrow Wire Time Window', "pl")

 legend.SetShadowColor(0);
 legend.SetFillColor(0);
 legend.SetLineColor(0);
 legend.SetTextSize(0.03)
 legend.Draw("same")
 
 c.SaveAs(saveName+'.png')

fileName = 'Zmumu_rawreco_2012D_full.root'
beforeHist = 'nSeg_lumi'
afterHist = 'nInTimeSeg_lumi'
rebin = 10
xmin = 0
xmax = 50
ymin = 0
ymax = 1.8
xTitle = 'Instantaneous Luminosity(10^{33}cm^{-2}s^{-1})'
yTitle = 'Number of Segment Per ME2/1'

makeplot(fileName,beforeHist,afterHist,rebin,xmin,xmax,ymin,ymax,xTitle,yTitle,'segLumi')

fileName = 'Zmumu_rawreco_2012D_full.root'
beforeHist = 'nRH_lumi'
afterHist = 'nInTimeRH_lumi'
rebin = 10
xmin = 0
xmax = 50
ymin = 0
ymax = 30
xTitle = 'Instantaneous Luminosity(10^{33}cm^{-2}s^{-1})'
yTitle = 'Number of RecHit Per ME2/1'

makeplot(fileName,beforeHist,afterHist,rebin,xmin,xmax,ymin,ymax,xTitle,yTitle,'rhLumi')

