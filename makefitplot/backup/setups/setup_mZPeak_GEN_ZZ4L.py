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
"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && finalState == 1 && \
       GENmassZ1 > 60 && GENmassZ1 < 120 && GENmassZ2 > 80 && GENmassZ2 < 100 ",\
"x_low": 60,\
"x_high": 120,\
"x_bins": 100,\
"pdfname": "bw_float",\
#"pdfname": "model_m4l_Z4L",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("GENmassZ1","",60,100),\
               ROOT.RooRealVar("GENmassZ2","",60,100),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("finalState","",0,5),\
               ],\
"plotVarFormula": "GENmassZ1",\
# plot set up
"doLogy":False,\
"xTitle": "GENmassZ",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170508_checkM4l/",\
"savename": "GENmassZ_ZZ4LSample"
}
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/float(config["x_bins"]) )

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()
pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

config["plotVarFormula"] = config["plotVarFormula"].replace("Z1","Z2")
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][1])
makeplotClass2 = plt.MakeFitPlot(config)
makeplotClass2.MakeDataset()
dataset.append(makeplotClass2.dataset)

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
makeplotClass.MakePlot()

'''
with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass.w.var("meanDCB").getVal() ), \
     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()
'''
