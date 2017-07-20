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
"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 70 && mass4l < 105 && finalState == 1 && \
       pTL1 > 30 && pTL1 < 40 && abs(etaL1) < 0.9 && \
       pTL2 > 15 && pTL2 < 25 && abs(etaL2) < 0.9 && \
       pTL3 > 12 && pTL3 < 16 && abs(etaL3) < 0.9 && \
       pTL4 > 6 && pTL4 < 8 && abs(etaL4) < 0.9 ",\
"x_low": 70,\
"x_high": 105,\
"x_bins": 100,\
"pdfname": "model_m4l_Z4L",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("pTL1","",0,100),\
               ROOT.RooRealVar("etaL1","",-2.5,2.5),\
               ROOT.RooRealVar("pTL2","",0,100),\
               ROOT.RooRealVar("etaL2","",-2.5,2.5),\
               ROOT.RooRealVar("pTL3","",0,100),\
               ROOT.RooRealVar("etaL3","",-2.5,2.5),\
               ROOT.RooRealVar("pTL4","",0,100),\
               ROOT.RooRealVar("etaL4","",-2.5,2.5),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("mass4l","",70,105),\
               ROOT.RooRealVar("finalState","",0,5) ],\
"plotVarFormula": "mass4l",\
# plot set up
"doLogy":False,\
"xTitle": "mass4l_{Z#rightarrow 4L}",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170508_checkM4l/",\
"savename": "m4l_Z4L"
}
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/config["x_bins"])

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
