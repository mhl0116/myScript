import ROOT
import sys
from subprocess import call
import os.path
import argparse

sys.path.append('/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/plotScript/makefitplot/')
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
"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/",\
#"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer_test/Ntuples/",\
#        "inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v3_20170312_afterApproval/",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root",\
#"inputfilename":"ZZTo4L_2016MC_ext_cancelBias_overall_Z2AT4_20170620.root",\
#"inputfilename":"combine_ggH125_ZZ4L_Z2AT4_20170621.root",\
#"inputfilename":"combine_ggH124125126_ZZ4L_20170620.root",\
"inputfilename":"ggHZZ4L_2016MC_MuPt4_Z2AT4_20170704.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 70 && finalState == 1 && idL" + lepIndex + " == -13 && \
       pTGENL" + lepIndex + " > " + str(pt1)  + " && pTGENL" + lepIndex + " < " + str(pt2) + " && \
       abs(etaL" + lepIndex + ") > " + str(eta1) + " && abs(etaL" + lepIndex + ") < " + str(eta2),\
#"cut":"passedFullSelection > 0.5 && mass4l > 70 && finalState == 1 &&  \
#       pTGENL" + lepIndex + " > " + str(pt1)  + " && pTGENL" + lepIndex + " < " + str(pt2) + " && \
#       abs(etaL" + lepIndex + ") > " + str(eta1) + " && abs(etaL" + lepIndex + ") < " + str(eta2),\
"x_low":-5,\
"x_high":5,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("pTL" + lepIndex,"",0,100),\
               ROOT.RooRealVar("pTGENL" + lepIndex,"",0,100),\
               ROOT.RooRealVar("etaL" + lepIndex,"",-2.5,2.5),\
#"roorealvars":[ROOT.RooRealVar("pTL" + lepIndex,"",0,100),\
#               ROOT.RooRealVar("pTGENL" + lepIndex,"",0,100),\
#               ROOT.RooRealVar("etaL" + lepIndex,"",-2.5,2.5),\
               ROOT.RooRealVar("idL" + lepIndex,"",-20,20),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
#               ROOT.RooRealVar("mass4l","",70,1050),\
               ROOT.RooRealVar("mass4l","",70,1050),\
               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("nFSRPhotons","",0,10)],\
"plotVarFormula": "(pTL" + lepIndex + "- pTGENL" + lepIndex + ")/pTGENL" + lepIndex,\
#"plotVarFormula": "(pTL" + lepIndex + "- pTGENL" + lepIndex + ")/pTGENL" + lepIndex,\
"doWeightDataset":False,\
# plot set up
"doLogy":False,\
"xTitle": "",\
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

logInfo = config["savepath"] + config["savename"]
plt.WriteLog(logInfo, "inputfile: " + config["inputfilepath"] + config["inputfilename"] + "\n")
plt.WriteLog(logInfo, "cut: " + config["cut"] + "\n", False)
plt.WriteLog(logInfo, "plotVarFormula: " + config["plotVarFormula"] + "\n", False)

pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

dataset.Print("v")

w_out = ROOT.RooWorkspace("w_out")
getattr(w_out, 'import')(dataset)
w_out.writeToFile(config["savepath"] + config["savename"] + '.root')


