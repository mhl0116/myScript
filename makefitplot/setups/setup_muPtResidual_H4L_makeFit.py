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
    parser.add_argument('--datasetpath', dest='datasetpath', type=str, help='')
    parser.add_argument('--datasetname', dest='datasetname', type=str, help='')
    parser.add_argument('--plotpath', dest='plotpath', type=str, help='')

    args = parser.parse_args()
    return args

args=ParseOption()

pts = args.pts #[5,20,40,50,60,100]
etas = args.etas #[0,0.9,1.8,2.4]
summaryTxtPath = args.txtpath #"/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = args.txtname #"Z4L_muPtResidual.txt"
datasetpath = args.datasetpath
datasetname = args.datasetname
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
        "inputfilename":"ggH125_2016MC_20170223.root",\
#        "inputfilename":"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root",\
#        "inputfilename":"DYJetsToLL_M-50_kalman_v4_m2mu.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 &&  \
       pTGENL4 > " + str(pt1)  + " && pTGENL4 < " + str(pt2) + " && \
       abs(etaL4) > " + str(eta1) + " && abs(etaL4) < " + str(eta2),\
"x_low":-0.2,\
"x_high":0.2,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("pTL4","",0,100),\
               ROOT.RooRealVar("pTGENL4","",0,100),\
               ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("mass4l","",105,140),\
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
                      + "_eta_" + str(eta1).replace(".","p") + "_" + str(eta2).replace(".","p") + "_dcb"
}
config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0],config["roorealvars"][1])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/config["x_bins"])

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

# get pdf
makeplotClass = plt.MakeFitPlot(config)
makeplotClass.MakePdfFactory()
pdf = makeplotClass.w.pdf(config["pdfname"])

# get dataset
datasetFile = ROOT.TFile(datasetpath + datasetname + ".root")
w_in = datasetFile.Get("w_out")
dataset = w_in.obj("dataset")
makeplotClass.rooargset.add(makeplotClass.w.var("x"))

makeplotClass.cut = "passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 &&         pTGENL4 > 50.0 && pTGENL4 < 60.0 &&        abs(etaL4) > 0.9 && abs(etaL4) < 1.5"

dataset_select = ROOT.RooDataSet("dataset_select","",dataset,makeplotClass.rooargset,makeplotClass.cut)

print makeplotClass.cut
dataset.Print("v")
dataset_select.Print("v")

sys.exit()
# make fit and plot
makeplotClass.fitResult = pdf.fitTo(dataset_select, ROOT.RooFit.Save(True))
makeplotClass.MakePlot(makeplotClass.w.var("x"),pdf,dataset_select)

# do second fit
postfitSigma = makeplotClass.w.var("sigmaDCB").getVal()
postfitAlpha1 = makeplotClass.w.var("alphaDCB").getVal()
postfitAlpha2 = makeplotClass.w.var("alpha2").getVal()
fitRange = min(postfitSigma*postfitAlpha1, postfitSigma*postfitAlpha2)*0.8
config["x_low"] = -1*fitRange
config["x_high"] = fitRange
config["x_bins"] = 50
config["pdfname"] = "gauss_1"
config["savename"] = config["savename"].replace("_dcb","_gauss")
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/config["x_bins"])

makeplotClass2 = plt.MakeFitPlot(config)
dataset2 = w_in.obj("dataset")
makeplotClass2.rooargset.add(makeplotClass2.w.var("x"))
dataset2_select = ROOT.RooDataSet("dataset2_select","",dataset2,makeplotClass2.rooargset,makeplotClass2.cut)
makeplotClass2.MakePdfFactory()
pdf2 = makeplotClass2.w.pdf(config["pdfname"])

dataset2.Print("v")
dataset2_select.Print("v")
#makeplotClass2.fitResult = pdf2.fitTo(dataset2_select, ROOT.RooFit.Save(True))
#makeplotClass2.MakePlot(makeplotClass2.w.var("x"),pdf2,dataset2_select)

#save post-fit parameters
'''
with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(pt1),str(pt2),str(eta1),str(eta2), \
     str(makeplotClass2.w.var("meanGauss").getVal() ), \
     str(makeplotClass2.w.var("meanGauss").getError() ) ] ) + '\n' )
myfile.close()
'''
