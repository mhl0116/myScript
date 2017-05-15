import ROOT
import sys
from subprocess import call
import os.path
import makefitplot as plt
import argparse

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/",\
"inputfilename":"ggH125_2016MC_20170223.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && \
       pTL1 > 20 && pTL1 < 45 && abs(etaL1) < 2.4 && \
       pTL2 > 20 && pTL2 < 45 && abs(etaL2) < 2.4 && \
       pTL3 > 15 && pTL3 < 45 && abs(etaL3) < 2.4 && \
       pTL4 > 15 && pTL4 < 45 && abs(etaL4) < 2.4 ",\
"x_low": -10,\
"x_high": 10,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("mass4l","",105,140),\
               ROOT.RooRealVar("GENmass4l","",105,140),\
               ROOT.RooRealVar("pTL1","",0,100),\
               ROOT.RooRealVar("etaL1","",-2.5,2.5),\
               ROOT.RooRealVar("pTL2","",0,100),\
               ROOT.RooRealVar("etaL2","",-2.5,2.5),\
               ROOT.RooRealVar("pTL3","",0,100),\
               ROOT.RooRealVar("etaL3","",-2.5,2.5),\
               ROOT.RooRealVar("pTL4","",0,100),\
               ROOT.RooRealVar("etaL4","",-2.5,2.5),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("finalState","",0,5) ],\
"plotVarFormula": "mass4l-GENmass4l",\
# plot set up
"doLogy":False,\
"xTitle": "mass4l_{H#rightarrow 4L}",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170508_checkM4l/",\
"savename": "m4l_diff_reco_gen_H4L"
}
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0], config["roorealvars"][1]) 
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/float(config["x_bins"]) )

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()
pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
makeplotClass.MakePlot()

'''
with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass.w.var("meanDCB").getVal() ), \
     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()
'''
