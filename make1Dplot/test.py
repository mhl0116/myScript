from ROOT import *

f_ = TFile("/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/ggH125_2016MC_20170223.root")
t_ = f_.Get("passedEvents")
rv_ = RooRealVar('mass4l','',105,140)
#cut = 'passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL1 > 5 && pTGENL1 < 20 && fabs(etaL1) > 0 && fabs(etaL1) < 0.9'
cut = 'mass4l > 105'
d_ = RooDataSet('d_', 'd_', t_, RooArgSet(rv_), cut )
print d_.sumEntries()
ras = RooArgSet()#rv_)
rv_.Print()
rv2_ = RooRealVar('mass3l','',1,2)
ras.add(rv2_)
ras.Print()
