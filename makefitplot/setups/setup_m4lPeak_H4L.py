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
"cut":"passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 ",\
#&& \
#       pTL1 > 20 && pTL1 < 100 && abs(etaL1) < 1.4 && \
#       pTL2 > 10 && pTL2 < 100 && abs(etaL2) < 1.4 && \
#       pTL3 > 5 && pTL3 < 100 && abs(etaL3) < 1.4 && \
#       pTL4 > 5 && pTL4 < 100 && abs(etaL4) < 1.4 ",\
"x_low": 105,\
"x_high": 140,\
"x_bins": 50,\
#"pdfname": "BWxDCB_h",\
#"pdfname": "doubleCB_2",\
#"pdfname": "bw_h_float",\
"pdfname": "DCBxDCB_h",\
#"pdfname": "GaussxDCB_h",\
#"pdfname": "GENShapexDCB_h",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("mass4l","",105,140),\
               ROOT.RooRealVar("pTL1","",0,100),\
               ROOT.RooRealVar("etaL1","",-2.5,2.5),\
               ROOT.RooRealVar("pTL2","",0,100),\
               ROOT.RooRealVar("etaL2","",-2.5,2.5),\
               ROOT.RooRealVar("pTL3","",0,100),\
               ROOT.RooRealVar("etaL3","",-2.5,2.5),\
               ROOT.RooRealVar("pTL4","",0,100),\
               ROOT.RooRealVar("etaL4","",-2.5,2.5),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("nFSRPhotons","",0,10)],\
"plotVarFormula": "mass4l",\
# plot set up
"doLogy":False,\
"xTitle": "mass4l_{H#rightarrow 4L}",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170511_checkMuPtResidual_endcap/",\
"savename": "m4l_H4L_all_DCBxDCB"
}
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/float(config["x_bins"]) )

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)

#load genshape
makeplotClass.LoadGenShape("GENm4l_H4L")

makeplotClass.MakePdfFactory()

#makeplotClass.w.Print()

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
