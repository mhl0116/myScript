import ROOT
from tdrStyle import *
setTDRStyle()
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit.so')
import sys

class MakeFitPlot():

      def __init__(self, config):

          # load configurations
          self.doUnbin = config["unbinFit"]
          self.inputfilepath = config["inputfilepath"]
          self.inputfilename = config["inputfilename"]
          self.treename = config["treename"]
          self.cut = config["cut"]
          self.x_low = config["x_low"]
          self.x_high = config["x_high"]
          #self.pdfname = config["pdfname"]
          # for bin fit
          self.roorealvars = config["roorealvars"]     
          self.plotVarFormula = config["plotVarFormula"]
          self.plotArgList = config["plotArgList"]

          # initialize a workspace
          self.var_x = ROOT.RooRealVar("x", "", self.x_low, self.x_high)
          self.w = ROOT.RooWorkspace()
          getattr(self.w, 'import')(self.var_x)

          # assemble rooargset for roodataset
          self.rooargset = ROOT.RooArgSet()
          for roorealvar in self.roorealvars:
              self.rooargset.add(roorealvar)

          self.dataset = ROOT.RooDataSet()
          self.fitResult = ROOT.RooFitResult()


      def MakeDataset(self):

          file_ = ROOT.TFile(self.inputfilepath + self.inputfilename)
          tree_ = file_.Get(self.treename)
          # make slim tree
#          tree_.Draw(">>myList", self.cut, "entrylist")
#          entryList = ROOT.gDirectory.Get("myList")
#          tree_.SetEntryList(entryList)

          if self.doUnbin:

             self.dataset = ROOT.RooDataSet("dataset", "", tree_, self.rooargset, self.cut)

             x_formula = ROOT.RooFormulaVar("x", "",  self.plotVarFormula, self.plotArgList)                          
             x_indata = self.dataset.addColumn(x_formula)
             x_indata.setRange(self.x_low,self.x_high)

             #self.dataset.reduce(ROOT.RooFit.Cut("x > " + str(self.x_low) + " && x < " + str(self.x_high) ) )


      def MakePdfFactory(self):

          self.w.factory('DoubleCB::doubleCB_1(x, \
                          meanDCB[-0.000387,-0.001,0.001], sigmaDCB[0.0146,0.001,0.1], \
                          alphaDCB[1,0,5], nDCB[5,0.1,20], alpha2[1,0,5], n2[5,0.1,20])')
#                          meanDCB_1[-0.0001,-10,10], sigmaDCB_1[0.01,0.009,0.02], \
#                          alphaDCB_1[1.39,1.5], nDCB_1[3.4,3.5], alpha2_1[1.35,1.4], n2_1[5.5,5.8])')

          self.w.factory('DoubleCB::doubleCB_2(x, \
                          meanDCB_2[125,105,140], sigmaDCB_2[1,0,10], \
                          alphaDCB_2[9.13056e-01,0,10], nDCB_2[5,0.1,20], alpha2_2[1.21649e+00,0,10], n2_2[5,0.1,20])')

          self.w.factory('Gaussian::gauss_1(x, meanGauss[-0.001,-1,1], sigmaGauss[1,0,10])')

          self.w.factory('CBShape::singleCB_1(x, meanCB[0,-0.01,0.01], sigmaCB[0.001,0,10], alphaCB[1,0,10], nCB[1,0,50])')

          self.w.factory('SUM:model(fsig[0.9,0.7,1]*doubleCB_1, gauss_1)')

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/",\
"inputfilename":"ggH125_2016MC_20170223.root",\
#"inputfilename":"ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 ",#&& \
#       pTGENL2 > 5 && pTGENL2 < 20 && abs(etaL2) > 0 && abs(etaL2) < 0.9",\
"x_low":-0.1,\
"x_high":0.1,\
#"x_low":105,\
#"x_high":140,\
# for bin fit
"roorealvars":[ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("mass4l","",105,140),\
               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("pTL1","",0,100),\
               ROOT.RooRealVar("pTGENL1","",0,100),\
               ROOT.RooRealVar("etaL1","",-2.5,2.5)],\

#"plotVarFormula": "@0"\
"plotVarFormula": "(@0-@1)/@1"\
}
#config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][1])
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][3],config["roorealvars"][4])


makeplotClass = MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()

pdfname = 'model'
#pdfname = 'doubleCB_1'
#pdfname = 'doubleCB_2'

makeplotClass.fitResult = makeplotClass.w.pdf(pdfname).fitTo(makeplotClass.dataset, ROOT.RooFit.Save(True))


makeplotClass.w.pdf(pdfname).Print()
makeplotClass.w.var("x").Print()
makeplotClass.dataset.Print("v")

makeplotClass.var_x.setBins(100)
frame = makeplotClass.var_x.frame()

makeplotClass.dataset.plotOn(frame, ROOT.RooFit.MarkerStyle(20), ROOT.RooFit.MarkerColor(1))
makeplotClass.w.pdf(pdfname).plotOn(frame, ROOT.RooFit.LineWidth(2), ROOT.RooFit.LineColor(4))
makeplotClass.w.pdf(pdfname).paramOn(frame, ROOT.RooFit.Layout(0.12, 0.5, 0.7), ROOT.RooFit.Format("NE", ROOT.RooFit.FixedPrecision(4)))


c = ROOT.TCanvas("c","",800,800)
frame.Draw()
c.SaveAs("/home/mhl/public_html/2017/20170503_testUnbinFitCode/test.png")
c.SaveAs("/home/mhl/public_html/2017/20170503_testUnbinFitCode/test.pdf")


