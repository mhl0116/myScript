from ROOT import *
from array import array

from tdrStyle import *
setTDRStyle()

import numpy as np
import matplotlib.pyplot as plt

savePath = '/home/mhl/public_html/2016/20161013_investigateGENZrecoz/'


## failed to find an easy way to generate multivari-gaussian using roofit

#w = RooWorkspace('w')
#w.factory('x1[10, 100]')
#w.factory('x2[10, 100]')
#cov = TMatrixDSym(2)
#cov[0][0] = 156.25
#cov[0][1] = -96.4
#cov[1][0] = -96.4
#cov[1][1] = 156.25
#getattr(w,'import')(cov, 'cov')
#w.factory('MultiVarGaussian::mvg({x1,x2},{45.5,45.5},cov)')

## numpy way is much easier
mean = [45.6,45.6]
#cov = [[156.25,-96.4],[-96.4,156.25]]
cov = [[6,-3.75],[-3.75,6]]

x1, x2 = np.random.multivariate_normal(mean, cov, 5000000).T
mZ = x1 + x2
mZ_cutOneLeg = [mZ[i] for i in range(len(x1)) if (x1[i] > 42 and x1[i] < 48)]
mZ_cutTwoLeg = [mZ[i] for i in range(len(x1)) if (x1[i] > 42 and x1[i] < 48 and x2[i] > 10 and x2[i] < 40)]

print len(mZ),len(mZ_cutOneLeg),len(mZ_cutTwoLeg)

hist_mZ = TH1F('hist_mZ', '', 100, 80, 100)
hist_mZ_cutOneLeg = TH1F('hist_mZ_cutOneLeg', '', 100, 80, 100)
hist_mZ_cutTwoLeg = TH1F('hist_mZ_cutTwoLeg', '', 100, 80, 100)

for i in range(len(mZ)):
    hist_mZ.Fill(mZ[i])

for i in range(len(mZ_cutOneLeg)):
    hist_mZ_cutOneLeg.Fill(mZ_cutOneLeg[i])

for i in range(len(mZ_cutTwoLeg)):
    hist_mZ_cutTwoLeg.Fill(mZ_cutTwoLeg[i])

roovar_mZ = RooRealVar('roovar_mZ','',80,100)

dataHist_mZ = RooDataHist('dataHist_mZ', '', RooArgList(roovar_mZ), hist_mZ, 1)
dataHist_mZ_cutOneLeg = RooDataHist('dataHist_mZ_cutOneLeg', '', RooArgList(roovar_mZ), hist_mZ_cutOneLeg, 1)
dataHist_mZ_cutTwoLeg = RooDataHist('dataHist_mZ_cutTwoLeg', '', RooArgList(roovar_mZ), hist_mZ_cutTwoLeg, 1)

mean = RooRealVar('mean','', 90, 80, 100)
sigma = RooRealVar('sigma', '', 10, 0, 30)
gauss = RooGaussian('gauss', '', roovar_mZ,mean,sigma)

### no cut on lep
c1 = TCanvas("c1", "c1", 800, 800)

dummy = TH1D("dummy","dummy",1,80,100)
dummy.SetMinimum(0)
dummy.SetMaximum(hist_mZ.GetMaximum()*1.5)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle('Events/0.02GeV')
dummy.GetYaxis().SetTitleOffset(1.3)
dummy.GetXaxis().SetTitle('massZ')
dummy.Draw()

mZFrame = roovar_mZ.frame()
dataHist_mZ.plotOn(mZFrame, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
fit1 = gauss.fitTo(dataHist_mZ)
gauss.plotOn(mZFrame, RooFit.LineColor(4), RooFit.LineWidth(2) )
gauss.paramOn(mZFrame, RooFit.Layout(0.17, 0.4, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(4)))

mZFrame.Draw('same')

c1.SaveAs(savePath+'toy.png')
c1.SaveAs(savePath+'toy.pdf')


### cut on one leg
dummy = TH1D("dummy","dummy",1,80,100)
dummy.SetMinimum(0)
dummy.SetMaximum(hist_mZ_cutOneLeg.GetMaximum()*1.5)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle('Events/0.02GeV')
dummy.GetYaxis().SetTitleOffset(1.3)
dummy.GetXaxis().SetTitle('massZ')
dummy.Draw()

mZFrame = roovar_mZ.frame()
dataHist_mZ_cutOneLeg.plotOn(mZFrame, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
fit1 = gauss.fitTo(dataHist_mZ_cutOneLeg)
gauss.plotOn(mZFrame, RooFit.LineColor(4), RooFit.LineWidth(2) )
gauss.paramOn(mZFrame, RooFit.Layout(0.17, 0.4, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(4)))

mZFrame.Draw('same')

c1.SaveAs(savePath+'toy_cutOneLeg.png')
c1.SaveAs(savePath+'toy_cutOneLeg.pdf')


### cut on two leg
dummy = TH1D("dummy","dummy",1,80,100)
dummy.SetMinimum(0)
dummy.SetMaximum(hist_mZ_cutTwoLeg.GetMaximum()*1.5)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle('Events/0.02GeV')
dummy.GetYaxis().SetTitleOffset(1.3)
dummy.GetXaxis().SetTitle('massZ')
dummy.Draw()

mZFrame = roovar_mZ.frame()
dataHist_mZ_cutTwoLeg.plotOn(mZFrame, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
fit1 = gauss.fitTo(dataHist_mZ_cutTwoLeg)
gauss.plotOn(mZFrame, RooFit.LineColor(4), RooFit.LineWidth(2) )
gauss.paramOn(mZFrame, RooFit.Layout(0.17, 0.4, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(4)))

mZFrame.Draw('same')

c1.SaveAs(savePath+'toy_cutTwoLeg.png')
c1.SaveAs(savePath+'toy_cutTwoLeg.pdf')

