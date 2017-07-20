import ROOT
import sys
from subprocess import call
import os.path
import makefitplot as plt
import argparse

config = \
{\
"unbinFit":True,\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer_test/Ntuples/compareM4lPeak_H4mu_Z4mu_20170615/",\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer_test/Ntuples/",\
"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/",\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/",\
#"inputfilename":"ggH125_2016MC_MuPt4_Z2AT4_20170627.root",\
#"inputfilename":"ggH125_2016MC_MuPt4_Z2AT4_20170704.root",\
#"inputfilename":"ggH125_2016MC_MuPt4_Z2AT4_cancelBiasUseMedian_20170704.root",\
#"inputfilename":"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2_20170627_v1.root",\
"inputfilename":"ggH125_2016MC_MuPt4_Z2AT4_scale_up_dn_20170720.root",\
"treename":"passedEvents",\
#"cut":"1",\
"cut":"passedFullSelection > 0.5 && finalState == 1 &&  \
       pTL1 > 5 && pTL1 < 100 && abs(etaL1) < 10 && \
       pTL2 > 5 && pTL2 < 100 && abs(etaL2) < 10 && \
       pTL3 > 5 && pTL3 < 100 && abs(etaL3) < 10 && \
       pTL4 > 5 && pTL4 < 100 && abs(etaL4) < 10 ",\
"x_low": 123.35,\
"x_high": 126.25,\
#"x_low": 124.9985,\
#"x_high": 125.0015,\
#"x_low": 105,\
#"x_high": 140,\
"x_bins": 50,\
"pdfname": "gauss_h4l",\
#"pdfname": "doubleCB_2",\
#"roorealvars":[ROOT.RooRealVar("GENmassZZ","",105,140)],\
"roorealvars":[ROOT.RooRealVar("mass4l_up","",105,140)],\
#"roorealvars":[ROOT.RooRealVar("GENMH","",105,140)],\
"doWeightDataset":False,\
"weight": "effiWeight",\
# plot set up
"doLogy":False,\
"xTitle": "mass4l_{H#rightarrow 4L}",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170720_scale_up_dn/",\
#"savename": "GENm4l_H4L_Z2AT4_gauss"
#"savename": "m4mu_H4L_MuPt4_Z2AT4_noWeight_gauss"
"savename":"m4mu_H4L_up"
}


config["roorealvars"] += [\
#ROOT.RooRealVar("GENmassZZ_born","",105,140),\
#ROOT.RooRealVar("GENmassZZ","",105,140),\
#ROOT.RooRealVar("massZ2","",0,120),\
ROOT.RooRealVar("pTL1","",0,100),\
ROOT.RooRealVar("etaL1","",-2.5,2.5),\
ROOT.RooRealVar("pTL2","",0,100),\
ROOT.RooRealVar("etaL2","",-2.5,2.5),\
ROOT.RooRealVar("pTL3","",0,100),\
ROOT.RooRealVar("etaL3","",-2.5,2.5),\
ROOT.RooRealVar("pTL4","",0,100),\
ROOT.RooRealVar("etaL4","",-2.5,2.5),\
ROOT.RooRealVar("passedFullSelection","",0,2),\
#ROOT.RooRealVar("effiWeight","",0,1000),\
ROOT.RooRealVar("finalState","",0,5),\
ROOT.RooRealVar("nFSRPhotons","",0,10)]

config["plotVarFormula"] = config["roorealvars"][0].GetName()
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0])
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/float(config["x_bins"]) )

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)

#load genshape
#makeplotClass.LoadGenShape("GENm4l_H4L")

makeplotClass.MakePdfFactory()

#makeplotClass.w.Print()

makeplotClass.MakeDataset()
pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
config["pdf"] = pdf
config["dataset"] = dataset
makeplotClass.MakePlot()

logInfo = config["savepath"] + config["savename"]
plt.WriteLog(logInfo, "inputfile: " + config["inputfilepath"] + config["inputfilename"] + "\n")
plt.WriteLog(logInfo, "cut: " + config["cut"] + "\n", False)
plt.WriteLog(logInfo, "plotVarFormula: " + config["plotVarFormula"] + "\n", False)
for rv in config["roorealvars"]:
    plt.WriteLog(logInfo, "RooRealVar::" + rv.GetName() + " L(" + str(rv.getMin()) + "-" + str(rv.getMax()) + ") \n", False)
#makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
#makeplotClass.MakePlot()

'''
with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass.w.var("meanDCB").getVal() ), \
     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()
'''
