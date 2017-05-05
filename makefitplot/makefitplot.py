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
          self.x_bins = config["x_bins"]
          self.pdfname = config["pdfname"]
          # for bin fit
          self.roorealvars = config["roorealvars"]     
          self.plotVarFormula = config["plotVarFormula"]
          self.plotArgList = config["plotArgList"]
          # set up plot
          self.doLogy = config["doLogy"]
          self.xTitle = config["xTitle"]
          self.yTitle = config["yTitle"]
          self.savepath = config["savepath"]
          self.savename = config["savename"]

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
    
          self.chi2 = -1

      def MakeDataset(self):

          file_ = ROOT.TFile(self.inputfilepath + self.inputfilename)
          tree_ = file_.Get(self.treename)

          if self.doUnbin:

             self.dataset = ROOT.RooDataSet("dataset", "", tree_, self.rooargset, self.cut)
             x_formula = ROOT.RooFormulaVar("x", "",  self.plotVarFormula, self.plotArgList)                          
             x_indata = self.dataset.addColumn(x_formula)
             x_indata.setRange(self.x_low,self.x_high)


      def MakePlot(self): 

          ### parepare frame 
          makeplotClass.var_x.setBins(self.x_bins)
          frame = makeplotClass.var_x.frame()

          self.dataset.plotOn(frame, ROOT.RooFit.MarkerStyle(20), ROOT.RooFit.MarkerColor(1))
          self.w.pdf(self.pdfname).plotOn(frame, ROOT.RooFit.LineWidth(2), ROOT.RooFit.LineColor(4))
          self.w.pdf(self.pdfname).paramOn(frame, ROOT.RooFit.Layout(0.2, 0.85, 0.9), ROOT.RooFit.Format("NE", ROOT.RooFit.FixedPrecision(4)))
          #frame.getAttText().SetTextSize(0.02)

          self.chi2 = frame.chiSquare(self.fitResult.floatParsFinal().getSize())

          ### plot
          c = ROOT.TCanvas("c","",800,800)
          c.SetLeftMargin(0.15) 
          if self.doLogy: c.SetLogy()
          dummy = ROOT.TH1D("dummy","dummy",1,config["x_low"],config["x_high"])
          dummy.SetMinimum(int(self.doLogy) )
          dummy.SetMaximum(frame.GetMaximum()*2)
          dummy.SetLineColor(0)
          dummy.SetMarkerColor(0)
          dummy.SetLineWidth(0)
          dummy.SetMarkerSize(0)
          dummy.GetYaxis().SetTitle(self.yTitle)
          dummy.GetYaxis().SetTitleOffset(1.4)
          dummy.GetXaxis().SetTitle(self.xTitle)
          dummy.Draw()

          frame.Draw("same")

          latex = ROOT.TLatex()
          latex.SetNDC()
          latex.SetTextSize(0.45*c.GetTopMargin())
          latex.SetTextFont(42)
          latex.SetTextAlign(11)
          latex.DrawLatex(0.25, 0.25, "#chi^{2}/DOF = %.3f" %(self.chi2))

          c.SaveAs(self.savepath + self.savename + ".png")
          c.SaveAs(self.savepath + self.savename + ".pdf")
                

      def MakePdfFactory(self):

          self.w.factory('DoubleCB::doubleCB_1(x, \
                          meanDCB[-0.000387,-0.001,0.001], sigmaDCB[0.0146,0.001,0.1], \
                          alphaDCB[1,0,5], nDCB[5,0,20], alpha2[1,0,5], n2[5,0,100])')

          self.w.factory('DoubleCB::doubleCB_2(x, \
                          meanDCB_2[125,105,140], sigmaDCB_2[1,0,10], \
                          alphaDCB_2[9.13056e-01,0,10], nDCB_2[5,0.1,20], alpha2_2[1.21649e+00,0,10], n2_2[5,0.1,20])')

          self.w.factory('Gaussian::gauss_1(x, meanGauss[-0.001,-1,1], sigmaGauss[0.1,0,1])')

          self.w.factory('CBShape::singleCB_1(x, meanCB[0,-0.01,0.01], sigmaCB[0.001,0,10], alphaCB[1,0,10], nCB[1,0,50])')

          self.w.factory('SUM:model(fsig[0.9,0.7,1]*doubleCB_1, gauss_1)')

config = \
{\
"unbinFit":True,\
"inputfilepath":"/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/",\
"inputfilename":"ggH125_2016MC_20170223.root",\
"treename":"passedEvents",\
"cut":"passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && \
       pTGENL4 > 5 && pTGENL4 < 20 && abs(etaL4) > 0 && abs(etaL4) < 0.9 &&\
       (pTL4-pTGENL4)/pTGENL4 > -0.1 && (pTL4-pTGENL4)/pTGENL4 < 0.1",\
"x_low":-0.1,\
"x_high":0.1,\
"x_bins": 100,\
"pdfname": "doubleCB_1",\
# for bin fit
"roorealvars":[ROOT.RooRealVar("passedFullSelection","",0,2),\
               ROOT.RooRealVar("mass4l","",105,140),\
               ROOT.RooRealVar("finalState","",0,5),\
               ROOT.RooRealVar("pTL4","",0,100),\
               ROOT.RooRealVar("pTGENL4","",0,100),\
               ROOT.RooRealVar("etaL4","",-2.5,2.5)],\
"plotVarFormula": "(pTL4-pTGENL4)/pTGENL4",\
# plot set up
"doLogy":False,\
"xTitle": "(pT_{reco}-pT_{gen})/pT_{gen}",\
"yTitle": "Events/" + str((0.1-(-0.1))/100),\
"savepath": "/home/mhl/public_html/2017/20170503_testUnbinFitCode/",\
"savename": "test"
}
config["plotArgList"] = ROOT.RooArgList(config["roorealvars"][3],config["roorealvars"][4])
### add cut and yTitle in the end

makeplotClass = MakeFitPlot(config)
makeplotClass.MakePdfFactory()
makeplotClass.MakeDataset()
makeplotClass.fitResult = makeplotClass.w.pdf(config["pdfname"]).fitTo(makeplotClass.dataset, ROOT.RooFit.Save(True))
makeplotClass.MakePlot()
