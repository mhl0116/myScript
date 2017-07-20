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
    parser.add_argument('--plotpath', dest='plotpath', type=str, help='')
    parser.add_argument('--plotname', dest='plotname', type=str, help='')

    args = parser.parse_args()
    return args

args=ParseOption()

pts = args.pts #[5,20,40,50,60,100]
etas = args.etas #[0,0.9,1.8,2.4]
summaryTxtPath = args.txtpath #"/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = args.txtname #"Z4L_muPtResidual.txt"

plotpath = args.plotpath

pt1 = pts[0]
pt2 = pts[1]
eta1 = etas[0]
eta2 = etas[1]

summaryTxt = summaryTxtPath+summaryTxtName
#if (os.path.exists(summaryTxt)): 
#   call('rm ' + summaryTxt, shell=True)

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/",\
#        "inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v3_20170312_afterApproval/",\
#        "inputfilename":"ggH125_2016MC_20170223.root",\
"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root",\
#        "inputfilename":"DYJetsToLL_M-50_kalman_v4_m2mu.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 70 && mass4l < 105 && finalState == 1 && \
       pTGENL4 > " + str(pt1)  + " && pTGENL4 < " + str(pt2) + " && \
       abs(etaL4) > " + str(eta1) + " && abs(etaL4) < " + str(eta2),\
"x_low":-0.2,\
"x_high":0.2,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
#"pdfname": "gauss_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("pTL4","",0,100),\
               ROOT.RooRealVar("pTGENL4","",0,100),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("mass4l","",70,105),\
               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("etaL4","",-2.5,2.5),\
               ROOT.RooRealVar("nFSRPhotons","",0,10)],\
"plotVarFormula": "(pTL4-pTGENL4)/pTGENL4",\
# plot set up
"doLogy":False,\
"xTitle": "(pT_{reco}-pT_{gen})/pT_{gen}",\
"yTitle": "",\
"savepath": plotpath,\
"savename": "muPtResidual_pt_" + str(pt1).replace(".","p") + "_" + str(pt2).replace(".","p") \
                     + "_eta_" + str(eta1).replace(".","p") + "_" + str(eta2).replace(".","p")
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

#lep3
config["cut"] = config["cut"].replace("L4","L3")
config["plotVarFormula"] = config["plotVarFormula"].replace("L4","L3")
config["roorealvars"][0] = ROOT.RooRealVar("pTL3","",0,100)
config["roorealvars"][1] = ROOT.RooRealVar("pTGENL3","",0,100)
config["roorealvars"][-2] = ROOT.RooRealVar("etaL3","",-2.5,2.5)
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
makeplotClass2 = plt.MakeFitPlot(config)
makeplotClass2.MakeDataset()
dataset.append(makeplotClass2.dataset)

#lep2
config["cut"] = config["cut"].replace("L3","L2")
config["plotVarFormula"] = config["plotVarFormula"].replace("L3","L2")
config["roorealvars"][0] = ROOT.RooRealVar("pTL2","",0,100)
config["roorealvars"][1] = ROOT.RooRealVar("pTGENL2","",0,100)
config["roorealvars"][-2] = ROOT.RooRealVar("etaL2","",-2.5,2.5)
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
makeplotClass3 = plt.MakeFitPlot(config)
makeplotClass3.MakeDataset()
dataset.append(makeplotClass3.dataset)

#lep4
config["cut"] = config["cut"].replace("L2","L1")
config["plotVarFormula"] = config["plotVarFormula"].replace("L2","L1")
config["roorealvars"][0] = ROOT.RooRealVar("pTL1","",0,100)
config["roorealvars"][1] = ROOT.RooRealVar("pTGENL1","",0,100)
config["roorealvars"][-2] = ROOT.RooRealVar("etaL1","",-2.5,2.5)
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
makeplotClass4 = plt.MakeFitPlot(config)
makeplotClass4.MakeDataset()
dataset.append(makeplotClass4.dataset)

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
makeplotClass.MakePlot()

with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass.w.var("meanDCB").getVal() ), \
     str(makeplotClass.w.var("meanDCB").getError() ),\
     str(makeplotClass.w.var("sigmaDCB").getVal() ), \
     str(makeplotClass.w.var("sigmaDCB").getError() ), \
     str(makeplotClass.w.var("alphaDCB").getVal() ), \
     str(makeplotClass.w.var("alphaDCB").getError() ),\
     str(makeplotClass.w.var("nDCB").getVal() ), \
     str(makeplotClass.w.var("nDCB").getError() ), \
     str(makeplotClass.w.var("alpha2").getVal() ), \
     str(makeplotClass.w.var("alpha2").getError() ), \
     str(makeplotClass.w.var("n2").getVal() ), \
     str(makeplotClass.w.var("n2").getError() ) ] )  + '\n')
#     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()

