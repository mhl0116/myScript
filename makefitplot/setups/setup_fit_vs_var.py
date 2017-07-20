import ROOT
import sys
from subprocess import call
import os.path
sys.path.append('/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/plotScript/makefitplot/')
import makefitplot as plt
import argparse

def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('--Vars',dest='Vars', nargs='+', help='', type=float)#, required=True)
#    parser.add_argument('--etas',dest='etas', nargs='+', help='', type=float)#, required=True)
    parser.add_argument('--txtpath', dest='txtpath', type=str, help='')
    parser.add_argument('--txtname', dest='txtname', type=str, help='')
    parser.add_argument('--plotpath', dest='plotpath', type=str, help='')
#    parser.add_argument('--plotname', dest='plotname', type=str, help='')

    args = parser.parse_args()
    return args

args=ParseOption()

Vars = args.Vars #[0,0.9,1.8,2.4]
summaryTxtPath = args.txtpath #"/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = args.txtname #"Z4L_muPtResidual.txt"

plotpath = args.plotpath

var1 = Vars[0]
var2 = Vars[1]

summaryTxt = summaryTxtPath+summaryTxtName
#if (os.path.exists(summaryTxt)): 
#   call('rm ' + summaryTxt, shell=True)

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v1_20170720/",\
"inputfilename":"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_m2mu.root",\
"treename":"passedEvents",\
"cut":"massZ > 80 && massZ < 100 && \
       ZLepDeltaR > " + str(var1) + " && ZLepDeltaR < " + str(var2),\
"x_low":89.5,\
"x_high":92.75,\
"x_bins": 50,\
"pdfname": "gauss_z4l",\
#"pdfname": "gauss_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("masssZ","",80,100),\
               ROOT.RooRealVar("ZLepDeltaR","",0,10)],\
#"plotVarFormula": "massZ",\
# plot set up
"doLogy":False,\
"xTitle": "massZ",\
"yTitle": "",\
"savepath": plotpath,\
"savename": "massZ_dR_" + str(var1).replace(".","p") + "_" + str(var2).replace(".","p")
}
config["plotVarFormula"] = config["roorealvars"][0].GetName()
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][0])

config["cut"] += " && " + config["plotVarFormula"] + " > " + str(config["x_low"]) \
+" && " + config["plotVarFormula"] + " < " + str(config["x_high"])
config["yTitle"] = "Events/" + str((config["x_high"]-config["x_low"])/config["x_bins"])

savedConfig = config["savepath"] + config["savename"] + '.txt'
if (os.path.exists(savedConfig)): call('rm ' + savedConfig, shell=True)

makeplotClass = plt.MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()
pdf = makeplotClass.w.pdf(config["pdfname"])
dataset = makeplotClass.dataset

makeplotClass.fitResult = pdf.fitTo(dataset, ROOT.RooFit.Save(True))
makeplotClass.MakePlot()

with open(summaryTxt, "a+") as myfile:
     myfile.write(' '.join([str(var1),str(var2), \
     str(makeplotClass.w.var("meanGauss_z4l").getVal() ), \
     str(makeplotClass.w.var("meanGauss_z4l").getError() ) ] )  + '\n')
#     str(makeplotClass.w.var("meanDCB").getError() ) ] ) + '\n' )
myfile.close()

