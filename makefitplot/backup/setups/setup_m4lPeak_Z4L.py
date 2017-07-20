import ROOT
import sys
from subprocess import call
import os.path
import makefitplot as plt
import argparse

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/",\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer_test/Ntuples/",\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer_test/Ntuples/compareM4lPeak_H4mu_Z4mu_20170615/",\
#"inputfilepath":"/raid/raid8/mhl/tmp/liteUFHZZ4LAnalyzer_test/Ntuples/",\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/inputRoots_2016MC/",\
#"inputfilename":"ZZTo4L_2016MC_ext_cancelBias_overall_20170619.root",\
#"inputfilename":"ZZTo4L_2016MC_ext_cancelBias_overall_Z2AT4_20170622.root",\
#"inputfilename":"ZZTo4L_2016MC_ext_cancelBias_overall_commonBias_20170620.root",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_cancelBias_overall.root",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_cancelBias_perEvent.root",\
#"inputfilename":"ZZTo4L_2016MC_MuPt4_Z2AT4_20170627.root",\
#"inputfilename":"ZZTo4L_2016MC_MuPt4_Z2AT4_20170704.root",\
#"inputfilename":"ZZTo4L_2016MC_MuPt4_Z2AT4_cancelBiasUseMedian_20170704.root",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2_20170627_v1.root",\
"inputfilename":"ZZTo4L_2016MC_MuPt4_Z2AT4_scale_up_dn_20170720.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && finalState == 1 &&\
       pTL1 > 5 && pTL1 < 100 && abs(etaL1) < 10 && \
       pTL2 > 5 && pTL2 < 100 && abs(etaL2) < 10 && \
       pTL3 > 5 && pTL3 < 100 && abs(etaL3) < 10 && \
       pTL4 > 5 && pTL4 < 100 && abs(etaL4) < 10 ",\
#"cut":"1",\
#"cut":"passedFullSelection",\
"x_low": 89.5,\
"x_high": 92.75,\
#"x_low": 90.2,\
#"x_high": 92.2,\
#"x_low": 80,\
#"x_high": 100,\
"x_bins": 50,\
"pdfname": "gauss_z4l",\
#"pdfname": "doubleCB_3",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("mass4l_up","",70,105)],\
#"roorealvars":[ROOT.RooRealVar("GENmassZZ","",70,105)],\
#"doWeightDataset":False,\
"doWeightDataset":False,\
"weight": "effiWeight",\
# plot set up
"doLogy":False,\
"xTitle": "mass4l_{Z#rightarrow 4L}",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170720_scale_up_dn/",\
#"savename": "m4mu_Z4L_MuPt4_Z2AT4_noWeight_gauss"
#"savename": "GENm4l_Z4L_MuPt4_Z2AT4_all"
#"savename": "GENm4l_born_Z4L_Z2AT4_withWeight_gauss"
"savename":"m4mu_Z4L_up"
}


config["roorealvars"] += [\
ROOT.RooRealVar("massZ2","",0,120),\
ROOT.RooRealVar("GENmassZZ","",0,120),\
ROOT.RooRealVar("GENmassZZ_born","",0,120),\
ROOT.RooRealVar("pTL1","",0,100),\
ROOT.RooRealVar("etaL1","",-2.5,2.5),\
ROOT.RooRealVar("pTL2","",0,100),\
ROOT.RooRealVar("etaL2","",-2.5,2.5),\
ROOT.RooRealVar("pTL3","",0,100),\
ROOT.RooRealVar("etaL3","",-2.5,2.5),\
ROOT.RooRealVar("pTL4","",0,100),\
ROOT.RooRealVar("etaL4","",-2.5,2.5),\
ROOT.RooRealVar("passedFullSelection","",0,2),\
ROOT.RooRealVar("effiWeight","",0,1000),\
ROOT.RooRealVar("finalState","",0,5),\
ROOT.RooRealVar("nFSRPhotons","",0,10)
]

config["plotVarFormula"] = config["roorealvars"][0].GetName()
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0])
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/float(config["x_bins"]) )

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()
pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True), ROOT.RooFit.SumW2Error(True))
config["pdf"] = pdf
config["dataset"] = dataset
makeplotClass.MakePlot()

logInfo = config["savepath"] + config["savename"]
plt.WriteLog(logInfo, "inputfile: " + config["inputfilepath"] + config["inputfilename"] + "\n")
plt.WriteLog(logInfo, "cut: " + config["cut"] + "\n", False)
plt.WriteLog(logInfo, "plotVarFormula: " + config["plotVarFormula"] + "\n", False)
for rv in config["roorealvars"]:
    plt.WriteLog(logInfo, "RooRealVar::" + rv.GetName() + " L(" + str(rv.getMin()) + "-" + str(rv.getMax()) + ") \n", False)
'''
with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass.w.var("meanDCB").getVal() ), \
     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()
'''
