import ROOT
import sys
from subprocess import call
import os.path
import argparse

sys.path.append('/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/plotScript/makefitplot/')
import makefitplot as plt

def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('--pts',dest='pts', nargs='+', help='', type=float)#, required=True)
    parser.add_argument('--etas',dest='etas', nargs='+', help='', type=float)#, required=True)
    parser.add_argument('--txtpath', dest='txtpath', type=str, help='')
    parser.add_argument('--txtname', dest='txtname', type=str, help='')
    parser.add_argument('--plotpath', dest='plotpath', type=str, help='')
    parser.add_argument('--datasetpath', dest='datasetpath', type=str, help='')
    parser.add_argument('--datasetname', dest='datasetname', type=str, help='')
    parser.add_argument('--lepIndex', dest='lepIndex', type=str, help='')

    args = parser.parse_args()
    return args

args=ParseOption()

pts = args.pts #[5,20,40,50,60,100]
etas = args.etas #[0,0.9,1.8,2.4]
#summaryTxtPath = args.txtpath #"/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
#summaryTxtName = args.txtname #"Z4L_muPtResidual.txt"
datasetpath = args.datasetpath
datasetname = args.datasetname
lepIndex = args.lepIndex

pt1 = pts[0]
pt2 = pts[1]
eta1 = etas[0]
eta2 = etas[1]

#summaryTxt = summaryTxtPath+summaryTxtName
#if (os.path.exists(summaryTxt)): 
#   call('rm ' + summaryTxt, shell=True)

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/",\
#        "inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v3_20170312_afterApproval/",\
        "inputfilename":"ggH125_2016MC_20170223.root",\
#        "inputfilename":"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root",\
#        "inputfilename":"DYJetsToLL_M-50_kalman_v4_m2mu.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 &&  \
       pTGENL" + lepIndex + " > " + str(pt1)  + " && pTGENL" + lepIndex + " < " + str(pt2) + " && \
       abs(etaL" + lepIndex + ") > " + str(eta1) + " && abs(etaL" + lepIndex + ") < " + str(eta2),\
"x_low":-0.2,\
"x_high":0.2,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("pTL" + lepIndex,"",0,100),\
               ROOT.RooRealVar("pTGENL" + lepIndex,"",0,100),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("mass4l","",105,140),\
               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("etaL" + lepIndex,"",-2.5,2.5),\
               ROOT.RooRealVar("nFSRPhotons","",0,10)],\
"plotVarFormula": "(pTL" + lepIndex + "-pTGENL" + lepIndex + ")/pTGENL" + lepIndex,\
# plot set up
"doLogy":False,\
"xTitle": "(pT_{reco}-pT_{gen})/pT_{gen}",\
"yTitle": "",\
"savepath": datasetpath,\
"savename": datasetname
}
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/config["x_bins"])

#savedConfig = config["savepath"] + config["savename"] + '.txt'
#if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)

makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()

logInfo = config["savepath"] + config["savename"] + ".txt"
plt.WriteLog(logInfo, "inputfile: " + config["inputfilepath"] + config["inputfilename"] + "\n")

pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

w_out = ROOT.RooWorkspace("w_out")
getattr(w_out, 'import')(dataset)
w_out.writeToFile(config["savepath"] + config["savename"] + '.root')


'''
#lep3
config["cut"] = config["cut"].replace("L4","L3")
config["plotVarFormula"] = config["plotVarFormula"].replace("L4","L3")
config["roorealvars"][0] = ROOT.RooRealVar("pTL3","",0,100)
config["roorealvars"][1] = ROOT.RooRealVar("pTGENL3","",0,100)
config["roorealvars"][-2] = ROOT.RooRealVar("etaL3","",-2.5,2.5)
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
makeplotClass2 = plt.MakeFitPlot(config)
makeplotClass2.MakeDataset()

makeplotClass2.dataset.Print("v")
makeplotClass2.dataset.get(40925).Print("v")

dataset.append(makeplotClass2.dataset)
dataset.Print("v")
dataset.get(40925).Print("v")
dataset.get(81913).Print("v")
sys.exit()

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

dataset.Print("v")

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

dataset.Print("v")

w_out = ROOT.RooWorkspace("w_out")
getattr(w_out, 'import')(dataset)
w_out.writeToFile(config["savepath"] + config["savename"] + '.root')
'''
#makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
#makeplotClass.MakePlot()

#with open(summaryTxt, "a+") as myfile:
#     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
#     str(makeplotClass.w.var("meanDCB").getVal() ), \
#     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
#myfile.close()

