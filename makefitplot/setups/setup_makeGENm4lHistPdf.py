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
"cut":"passedFullSelection > 0.5 && GENmass4l > 105 && GENmass4l < 140 && finalState == 1 ",\
#&& \
#       pTL1 > 20 && pTL1 < 100 && abs(etaL1) < 1.4 && \
#       pTL2 > 10 && pTL2 < 100 && abs(etaL2) < 1.4 && \
#       pTL3 > 5 && pTL3 < 100 && abs(etaL3) < 1.4 && \
#       pTL4 > 5 && pTL4 < 100 && abs(etaL4) < 1.4 ",\
"x_low": 124.5,\
"x_high": 125.5,\
"x_bins": 100,\
"pdfname": "BWxDCB_h",\
#"pdfname": "doubleCB_2",\
#"pdfname": "bw_h_float",\
#"pdfname": "DCBxDCB_h",\
#"pdfname": "GaussxDCB_h",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("GENmass4l","",105,140),\
#               ROOT.RooRealVar("pTL1","",0,100),\
#               ROOT.RooRealVar("etaL1","",-2.5,2.5),\
#               ROOT.RooRealVar("pTL2","",0,100),\
#               ROOT.RooRealVar("etaL2","",-2.5,2.5),\
#               ROOT.RooRealVar("pTL3","",0,100),\
#               ROOT.RooRealVar("etaL3","",-2.5,2.5),\
#               ROOT.RooRealVar("pTL4","",0,100),\
#               ROOT.RooRealVar("etaL4","",-2.5,2.5),\
#               ROOT.RooRealVar("passedFullSelection","",0,2),\
#               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("nFSRPhotons","",0,10)],\
"plotVarFormula": "GENmass4l",\
# plot set up
"doLogy":True,\
"xTitle": "mass4l_{H#rightarrow 4L}",\
"yTitle": "",\
"savepath": "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/plotScript/makefitplot/histpdf/",\
"savename": "GENm4l_H4L"
}
#config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
#+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/float(config["x_bins"]) )

#savedConfig = config["savepath"] + config["savename"] + '.txt'
#if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeGenShape()
#makeplotClass.MakeDataset()
#pdf = makeplotClass.w.pdf(config["pdfname"])
#dataset = makeplotClass.dataset

#makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
#makeplotClass.MakePlot()
