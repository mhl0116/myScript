import ROOT
import sys
from subprocess import call
import os.path
import makefitplot as plt
import argparse

def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('--pts',dest='pts', nargs='+', help='', type=float)#, required=True)
    parser.add_argument('--etas',dest='etas', nargs='+', help='', type=float)#, required=True)
    parser.add_argument('--txtpath', dest='txtpath', type=str, help='')
    parser.add_argument('--txtname', dest='txtname', type=str, help='')

    args = parser.parse_args()
    return args

args=ParseOption()

pts = args.pts #[5,20,40,50,60,100]
etas = args.etas #[0,0.9,1.8,2.4]
summaryTxtPath = args.txtpath #"/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = args.txtname #"Z4L_muPtResidual.txt"

pt1 = pts[0]
pt2 = pts[1]
eta1 = etas[0]
eta2 = etas[0]

summaryTxt = summaryTxtPath+summaryTxtName

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v3_20170312_afterApproval/",\
"inputfilename":"DYJetsToLL_M-50_kalman_v4_m2mu.root",\
"treename":"passedEvents",\
"cut":"massZ > 80 && massZ < 100 && \
       genLep_pt1 > " + str(pt1)  + " && genLep_pt1 < " + str(pt2) + " && \
       abs(genLep_eta1) > " + str(eta1) + " && abs(genLep_eta1) < " + str(eta2),\
"x_low":-0.1,\
"x_high":0.1,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("pT1","",0,100),\
               ROOT.RooRealVar("genLep_pt1","",0,100),\
               ROOT.RooRealVar("massZ","",80,100),\
               ROOT.RooRealVar("genLep_ete1","",-2.5,2.5)],\
"plotVarFormula": "(pT1-genLep_pt1)/genLep_pt1",\
# plot set up
"doLogy":False,\
"xTitle": "(pT_{reco}-pT_{gen})/pT_{gen}",\
"yTitle": "",\
"savepath": "/home/mhl/public_html/2017/20170505_checkResiduals/Z2L/",\
"savename": "muPtResidual_pt_" + str(pt1) + "_" + str(pt2) + "_eta_" + str(eta1).replace(".","p") + "_" + str(eta2).replace(".","p")
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

#lep2
config["cut"] = config["cut"].replace("pt1","pt2")
config["cut"] = config["cut"].replace("eta1","eta2")
config["plotVarFormula"] = config["plotVarFormula"].replace("pt1","pt2")
config["plotVarFormula"] = config["plotVarFormula"].replace("pT1","pT2")
config["roorealvars"][0] = ROOT.RooRealVar("pT2","",0,100)
config["roorealvars"][1] = ROOT.RooRealVar("genLep_pt2","",0,100)
config["roorealvars"][-1] = ROOT.RooRealVar("genLep_eta2","",-2.5,2.5)
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
makeplotClass2 = plt.MakeFitPlot(config)
makeplotClass2.MakeDataset()
dataset.append(makeplotClass2.dataset)

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
makeplotClass.MakePlot()

with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass.w.var("meanDCB").getVal() ), \
     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()

