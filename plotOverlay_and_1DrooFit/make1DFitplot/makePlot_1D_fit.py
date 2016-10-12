import ROOT, sys, os, string, re
from ROOT import *
from array import array

from tdrStyle import *
setTDRStyle()
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit.so')

from paraConfigurations import *

import argparse
def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('-t', dest='tag', type=str, help='for each plot')

    args = parser.parse_args()
    return args

args=ParseOption()

tag = args.tag
paraConfig = paraConfigs[tag]

rootPath1 = paraConfig['rootPath1']
#rootPath2 = paraConfig['rootPath2']
rootfile1 = paraConfig['rootfile1']
#rootfile2 = paraConfig['rootfile2']
tree1 = paraConfig['tree1']
#tree2 = paraConfig['tree2']
binInfo = paraConfig['binInfo']
vars1 = paraConfig['vars1']
#vars2 = paraConfig['vars2']
cuts1 = paraConfig['cuts1']
#cuts2 = paraConfig['cuts2']
weight1 = paraConfig['weight1']
#weight2 = paraConfig['weight2']
xTitle = paraConfig['xTitle']
yTitle = paraConfig['yTitle']
#legend1 = paraConfig['legend1']
#legend2 = paraConfig['legend2']
savePath = paraConfig['savePath']
saveName = paraConfig['saveName']
latexNote1 = paraConfig['latexNote1']
#latexNote2 = paraConfig['latexNote2']
pdfName = paraConfig['pdfName']


f1 = TFile(rootPath1 + rootfile1, 'READ')
#f2 = TFile(rootPath2 + rootfile2, 'READ')

t1 = f1.Get(tree1)
#t2 = f2.Get(tree2)

hists1 = [ TH1F('hist1_'+str(i),'', binInfo[0], binInfo[1], binInfo[2]) for i in range(len(vars1)) ]
#hists2 = [ TH1F('hist2_'+str(i),'', binInfo[0], binInfo[1], binInfo[2]) for i in range(len(vars2)) ]

HIST1 = TH1F('HIST1', '', binInfo[0], binInfo[1], binInfo[2])
#HIST2 = TH1F('HIST2', '', binInfo[0], binInfo[1], binInfo[2])

for i in range(len(vars1)):
    t1.Project(hists1[i].GetName(), vars1[i], weight1[i]+"*"+cuts1[i])
    if i == 0:
       HIST1 = hists1[0].Clone()
    else:
       HIST1.Add(hists1[i])
#for i in range(len(vars2)):
#    t2.Project(hists2[i].GetName(), vars2[i], weight2[i]+"*"+cuts2[i])
#    if i == 0:
#       HIST2 = hists2[0].Clone()
#    else:
#       HIST2.Add(hists2[i])

#HIST1.Scale(1/HIST1.Integral())
#HIST2.Scale(1/HIST2.Integral())

w = RooWorkspace('w')

xmin = binInfo[1]
xmax = binInfo[2]

w.factory('Gaussian::gauss(x[' + str(xmin) + ',' + str(xmax) + '],meanGauss[0,-1,1],sigmaGauss[1,0,2])')
w.factory('BreitWigner::bw(x[' + str(xmin) + ',' + str(xmax) + '],meanBW[91.2, 90, 92],sigmaBW[2.4,2,3])')
w.factory('DoubleCB::doubleCB(x[' + str(xmin) + ',' + str(xmax) + '], \
                              meanDCB[0,-1.5,1.5], sigmaDCB[0.1,0,10], \
                              alpha[1.1,0,50], n[1,0,50], alpha2[1.1,0,50], n2[1,0,50])')
#x = RooRealVar('pull', '', -5, 5)
#m = RooRealVar('mean', '', 0, -1, 1)
#s = RooRealVar('sigma', '', 1, 0, 2)
#gauss = RooGaussian('gauss', '', x, m, s)
#mean = RooRealVar("mean","mean", 0, -1.5, 1.5)
#sigmaCB = RooRealVar("sigmaCB", "sigmaCB", 0.1, 0, 10)
#alpha = RooRealVar("a","a", 1.1, 0, 50)
#n = RooRealVar("n","n", 1, 0, 50)
#alpha2 = RooRealVar("a2","a2", 1.1, 0, 50)
#n2 = RooRealVar("n2","n2", 1, 0, 50)
#CB = RooDoubleCB("CB","CB", x, mean, sigmaCB, alpha, n, alpha2, n2)

dataHist1 = RooDataHist('dataHist1', 'dataHist1', RooArgList(w.var('x')), HIST1, 1)
pdf = w.pdf(pdfName)
fFit = pdf.fitTo(dataHist1)

xframe = w.var('x').frame(RooFit.Title(xTitle))

dataHist1.plotOn(xframe, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
#gauss.plotOn(xframe, RooFit.LineColor(4), RooFit.LineWidth(2) )
#gauss.paramOn(xframe, RooFit.Layout(0.17, 0.3, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(2)))
pdf.plotOn(xframe, RooFit.LineColor(4), RooFit.LineWidth(2) )
pdf.paramOn(xframe, RooFit.Layout(0.17, 0.4, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(4)))

c1 = TCanvas("c1", "c1", 800, 800)

#dummy = TH1D("dummy","dummy",1,binInfo[1],binInfo[2])
dummy = TH1D("dummy","dummy",1,-3,3)
dummy.SetMinimum(0)
yMax1 = HIST1.GetMaximum()*1.5
#yMax2 = HIST2.GetMaximum()*1.5
yMax = yMax1
dummy.SetMaximum(yMax)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle(yTitle)
dummy.GetYaxis().SetTitleOffset(1.3)
dummy.GetXaxis().SetTitle(xTitle)
dummy.Draw()

#HIST1.Draw('hist same')
#HIST2.Draw('hist same')
xframe.Draw('same')

HIST1.SetLineColor(1)
#HIST2.SetLineColor(2)
HIST1.SetLineWidth(1)
#HIST2.SetLineWidth(1)

legend = TLegend(0.15,0.75,0.42,0.9)
#legend.AddEntry(HIST1, legend1, 'l')
#legend.AddEntry(HIST2, legend2, 'l')
legend.SetTextSize(0.03)
legend.SetLineWidth(2)
legend.SetFillColor(0)
legend.SetBorderSize(1)
#legend.Draw('SAME')

latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.45*c1.GetTopMargin())
latex.SetTextFont(42)
latex.SetTextAlign(11)
latex.DrawLatex(0.45, 0.85, latexNote1)
#if len(latexNote2) > 0:
#   latex.DrawLatex(0.45, 0.75, latexNote2)
c1.SaveAs(savePath+saveName+'.png')
c1.SaveAs(savePath+saveName+'.pdf')

