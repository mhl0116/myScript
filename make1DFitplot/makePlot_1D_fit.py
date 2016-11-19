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

w.factory('Gaussian::gauss(x[' + str(xmin) + ',' + str(xmax) + '],meanGauss[90, 40, 120],sigmaGauss[10, 0, 100])')
#w.factory('Gaussian::gauss(x[' + str(xmin) + ',' + str(xmax) + '],meanGauss[7.22605e+01],sigmaGauss[1.08673e+01])')

w.factory('BreitWigner::bw(x[' + str(xmin) + ',' + str(xmax) + '],meanBW[91.2, 80, 100],sigmaBW[2.5,0,10])')
#w.factory('BreitWigner::bw(x[' + str(xmin) + ',' + str(xmax) + '],meanBW[91.18],sigmaBW[2.49])')

w.factory('DoubleCB::doubleCB(x[' + str(xmin) + ',' + str(xmax) + '], \
                              meanDCB[0,-1,1], sigmaDCB[1, 0,10], \
                              alphaDCB[1,0,5], nDCB[5,0,50], alpha2[1,0,5], n2[5,0,50])')
w.factory('CBShape::singleCB(x, \
#                            meanCB[85,80,95], sigmaCB[5,0,10], alphaCB[1,0,10], nCB[1,0,50])')
#                            meanCB[9.10005e+01], sigmaCB[8.77700e-01], alphaCB[4.56794e-01], nCB[3.82520e+00])')
#                            meanCB[90.95,85,95], sigmaCB[1.154,0,10], alphaCB[1.187,0,10], nCB[5.911,0,50])')

w.factory('Polynomial::poly3(x,{a0[1,-100,100],a1[10,-100,100],a2[-100,-1000,1000],a3[-10, -10000,10000]})')
w.factory("Exponential::bkg(x, tau[0.1,-1,1])")
w.factory('Bernstein::bernstein(x, {b0[1,-100,100], b1[10,-100,100], b2[10,-100,100], b3[100,-1000,1000]})')

w.var('x').setBins(1000, 'fft')
w.factory('FCONV::BWxCB(x,bw,singleCB)')
w.factory('FCONV::BWxDCB(x,bw,doubleCB)')
w.factory('SUM:BWplusPOLY3(f1[0,1]*bw, poly3)')
w.factory('SUM:model(fsig[0.8,0.5,1]*BWxCB, bkg)')
#w.factory('SUM:model(fsig[5.94226e-01]*BWxCB, bkg)')

w.factory('Gaussian::gauss3(x,meanGauss3[90,40,100],sigmaGauss3[10, 0, 100])')

w.factory("ArgusBG:argus(x, 100, argpar[-20,-100,-1])")
#w.factory('SUM:BWplusDCB(fsig*bw,DCB)')
w.factory('SUM:genmz1(fsig*singleCB, gauss)')
w.factory('Gaussian::gauss2(x,meanGauss2[90,40,100],sigmaGauss2[10, 0, 100])')
#w.factory('Gaussian::gauss2(x,meanGauss2[9.22526e+01],sigmaGauss2[1.66743e+00])')
#w.factory('SUM:pdfgenmz1(fsig2[8.82722e-01]*genmz1, gauss2)')
w.factory('SUM:pdfgenmz1(fsig2[0.9,0.5,1]*genmz1, gauss2)')
w.factory('SUM:pdfpdfgenmz1(fsig3[0.9,0.5,1]*pdfgenmz1, gauss3)')


#w.factory('SUM:pdfgenmz1(fsig*doubleCB, argus)')

#w.factory("EXPR::RelBW('1/( (x*x-meanBW*meanBW)*(x*x-meanBW*meanBW)+x*x*x*x*(sigmaBW/meanBW)*(sigmaBW/meanBW))', x, meanBW,sigmaBW )")
#w.factory('CBShape::singleCB_tcheng(x,meanBW,sig_tcheng[0.133327],a_tcheng[0.0159116],n_tcheng[81.822])')
#w.factory('SUM::RelBWxCB(ftcheng1[0.650581]*RelBW,singleCB_tcheng)')
#w.factory('Gaussian::gauss_tcheng(x,gaussmean_tcheng[67.6329],gausssigma_tcheng[8.19463])')
#w.factory('SUM::RelBWxCBxgauss(ftcheng2[0.785403]*RelBWxCB, gauss_tcheng)')

#HIST1.Smooth()
dataHist1 = RooDataHist('dataHist1', 'dataHist1', RooArgList(w.var('x')), HIST1, 1)
pdf = w.pdf(pdfName)


fFit = pdf.fitTo(dataHist1)


print w.var("sigmaCB").getError()
print w.var("sigmaCB").getAsymErrorHi()
print w.var("sigmaCB").getAsymErrorLo()



w.factory('Gaussian::gausTest(y[40.1,5,100],testMean[40,39,41],testSig[1])')

xframe = w.var('x').frame(RooFit.Title(xTitle))

dataHist1.plotOn(xframe, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
pdf.plotOn(xframe, RooFit.LineColor(4), RooFit.LineWidth(2) )
if pdfName == 'model':
   pdf.plotOn(xframe, RooFit.LineColor(4), RooFit.LineWidth(2), RooFit.Components("bkg"), RooFit.LineStyle(kDashed))
pdf.paramOn(xframe, RooFit.Layout(0.17, 0.4, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(4)))

c1 = TCanvas("c1", "c1", 800, 800)
#c1.SetLogy()
dummy = TH1D("dummy","dummy",1,binInfo[1],binInfo[2])
#dummy = TH1D("dummy","dummy",1, 92,96)#binInfo[1],binInfo[2])
dummy.SetMinimum(10)
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

xframe.Draw('same')

HIST1.SetLineColor(1)
HIST1.SetLineWidth(1)

legend = TLegend(0.15,0.75,0.42,0.9)
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

