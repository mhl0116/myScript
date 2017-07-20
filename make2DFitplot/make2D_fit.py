from ROOT import *
#from array import array
#from math import *
#from subprocess import call
from tdrStyle import *
setTDRStyle()
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit.so')
import sys

inputRootPath = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/"
outputPlotPath = "/home/mhl/public_html/2017/20170223_makeModel/"
modelPath = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/doMeasurement/CreateDatacards_Moriond17_expect_20170222/"
channels = ["4mu","4e","2e2mu"]
m4lTypes = ["reco","refit"]

class Make2DFit():

      def __init__(self, inputConfig):

          #filename, treename, varName1, varName2, var1Low, var1High, var2Low, var2High, nbins1, nbins2, cut, isUnbin, importModel, saveName1, saveName2):

          self.rootfile = TFile(inputConfig["filename"])
          self.tree = self.rootfile.Get(inputConfig["treename"])
          # var1 is on xaxis, var2 is on yaxis
          self.varName1 = inputConfig["varName1"]
          self.varName2 = inputConfig["varName2"]
          self.nbins1 = inputConfig["nbins1"]
          self.nbins2 = inputConfig["nbins2"]
          self.var1Low = inputConfig["var1Low"]
          self.var1High = inputConfig["var1High"]
          self.var2Low = inputConfig["var2Low"]
          self.var2High = inputConfig["var2High"]
          self.roovar1 = RooRealVar(inputConfig["roovarName1"],inputConfig["roovarName1"],inputConfig["var1Low"],inputConfig["var1High"])
          self.roovar2 = RooRealVar(inputConfig["roovarName2"],inputConfig["roovarName2"],inputConfig["var2Low"],inputConfig["var2High"])
          self.cut = inputConfig["cut"]
          self.isUnbin = inputConfig["isUnbin"]
          self.saveName1 = inputConfig["saveName1"]
          self.saveName2 = inputConfig["saveName2"]

          self.dataset = RooDataSet()
          self.w = RooWorkspace()
          self.fitResult = RooFitResult()

          print "Input Loaded ..."

      def MakeDataset(self):

          
          if self.isUnbin:

             self.dataset  = RooDataSet("dataset_tmp", "dataset_tmp", self.tree, RooArgSet(self.roovar1,self.roovar2), self.cut)             

          else:

             hist = TH2F("hist_tmp", "hist_tmp", self.nbins1, self.var1Low, self.var1High, self.nbins2, self.var2Low, self.var2High) 

             print hist
             print self.tree.GetEntries()

             self.tree.Project(hist.GetName(), self.varName2+":"+self.varName1, "1*("+self.cut+")")
             self.dataset = RooDataHist('datahist_tmp', 'datahist_tmp', RooArgList(self.roovar1,self.roovar2), hist, 1)

             print self.dataset.sumEntries()

          print "Dataset made ..."
  
      def MakeModel(self, dcbMean, dcba1, dcba2, pdfErrSFile):

          getattr(self.w,'import')(self.roovar1)
          getattr(self.w,'import')(self.roovar2)

          self.w.factory("mH[125]")
          self.w.factory("expr::sigma('@0*@1',{"+self.roovar2.GetName()+", mH})") 
#          self.w.factory("DoubleCB:dcb("+self.roovar1.GetName()+", mean_2D["+str(dcbMean)+"], sigma, a1_2D["+str(dcba1)+"],n1_2D[1,0,10],a2_2D["+str(dcba2)+"],n2_2D[1,0,50])")
          self.w.factory("DoubleCB:dcb("+self.roovar1.GetName()+", mean_2D["+str(dcbMean)+"], sigma, a1_2D[1,0,10],n1_2D[1,0,10],a2_2D[1,0,10],n2_2D[1,0,10])")

          #read err pdf
          histFile = TFile(pdfErrSFile)
          hist = histFile.Get("h_Dm")
          dataHist = RooDataHist("datahistname","",RooArgList(self.roovar2), hist)
          pdfErrS = RooHistPdf("histpdfname","",RooArgSet(self.roovar2), dataHist)

          #2D DCBxErr
          model = RooProdPdf("model","", RooArgSet(pdfErrS), RooFit.Conditional(RooArgSet(self.w.pdf("dcb")), RooArgSet(self.roovar1)))
          model.Print()
          getattr(self.w,'import')(model)

          #1D DCB
          self.w.factory("DoubleCB:dcb_1d("+self.roovar1.GetName()+", mean_1D[125,120,130], sigma_1D[1,0,10], a1_1D[1,0,10],n1_1D[1,0,10],a2_1D[1,0,10],n2_1D[1,0,10])")

      def MakeFit(self):

          self.fitResult = self.w.pdf("model").fitTo(self.dataset, RooFit.Save(kTRUE) )
          self.fitResult_1D = self.w.pdf("dcb_1d").fitTo(self.dataset, RooFit.Save(kTRUE))
          print "Fit done ..."

      def MakePlot(self):

          frame1 = self.roovar1.frame()
          frame2 = self.roovar2.frame()

          self.dataset.plotOn(frame1, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
          self.w.pdf("model").plotOn(frame1, RooFit.LineWidth(2), RooFit.LineColor(4))
          self.w.pdf("dcb_1d").plotOn(frame1, RooFit.LineWidth(2), RooFit.LineColor(1))

          self.w.pdf("model").paramOn(frame1, RooFit.Layout(0.12, 0.5, 0.45), RooFit.Format("NE", RooFit.FixedPrecision(4)), RooFit.Label("2D fit result"))
          frame1.getAttText().SetTextSize(0.03)
          frame1.getAttText().SetTextColor(4)

          self.w.pdf("dcb_1d").paramOn(frame1, RooFit.Layout(0.12, 0.5, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(4)), RooFit.Label("1D fit result"))
          frame1.getAttText().SetTextSize(0.03)
          frame1.getAttText().SetTextColor(1)
          #plot twice to cover parameter box
          self.dataset.plotOn(frame1, RooFit.MarkerStyle(20), RooFit.MarkerColor(1), RooFit.Name("mcsample"))
          self.w.pdf("model").plotOn(frame1, RooFit.LineWidth(2), RooFit.LineColor(4), RooFit.Name("2Dfit"))
          self.w.pdf("dcb_1d").plotOn(frame1, RooFit.LineWidth(2), RooFit.LineColor(1), RooFit.Name("1Dfit"))
        
          chi2_2d = frame1.chiSquare(self.fitResult.floatParsFinal().getSize())
          dof_2d =  self.fitResult.floatParsFinal().getSize()
          chi2_1d = frame1.chiSquare(self.fitResult_1D.floatParsFinal().getSize())
          dof_1d =  self.fitResult_1D.floatParsFinal().getSize()

          self.dataset.plotOn(frame2, RooFit.MarkerStyle(20), RooFit.MarkerColor(1))
          self.w.pdf("model").plotOn(frame2, RooFit.LineWidth(2), RooFit.LineColor(4))

          c1 = TCanvas("c", "", 800, 800)

          frame1.Draw()

          latex = TLatex()
          latex.SetNDC()
          latex.SetTextSize(0.45*c1.GetTopMargin())
          latex.SetTextFont(42)
          latex.SetTextAlign(11)
#          latex.DrawLatex(0.7, 0.85, "#chi^{2}/DOF = %.3f" %(chi2/dof))

          legend = ROOT.TLegend(0.63,0.75,0.992,0.95)
          legend.AddEntry(frame1.findObject("mcsample"), 'MC sample', 'pe')
          legend.AddEntry(frame1.findObject("1Dfit"), '1D fit, #chi^{2}/DOF = %.3f' %(chi2_1d/dof_1d), 'l')
          legend.AddEntry(frame1.findObject("2Dfit"), '2D fit, #chi^{2}/DOF = %.3f' %(chi2_2d/dof_2d), 'l')
          legend.SetTextSize(0.03)
          legend.SetLineWidth(2)
          legend.SetFillColor(0)
          legend.SetBorderSize(1)
          legend.Draw('SAME')

          c1.SaveAs(self.saveName1 + '.png')
          c1.SaveAs(self.saveName1 + '.pdf')

          frame2.Draw()
          c1.SaveAs(self.saveName2 + '.png')  
          c1.SaveAs(self.saveName2 + '.pdf')



inputConfig = \
{
"filename" : inputRootPath + "mH_125.root", 
"treename" : "passedEvents",
#"varName1" : "mass4l", #
#"varName2" : "mass4lErr/mass4l", #
"roovarName1" : "CMS_zz4l_mass",
"roovarName2" : "CMS_zz4l_massErr",
"var1Low" : 105,
"var1High" : 140,
#"var2Low" : 0.007,
#"var2High" : 0.1, #
"nbins1" : 100,
"nbins2" : 100,
#"cut" : "passedFullSelection && ", #
"isUnbin" : False,
#"saveName1" : outputPlotPath+"mass4lFrom2D", #
#"saveName2" : outputPlotPath+"mass4lErrFrom2D" #
}

cutREFIT = {"reco" : " mass4l > 105 && mass4l < 140 && ",\
            "refit": " mass4lREFIT > 105 && mass4lREFIT < 140 && " }
cutChannel = {"4mu" : " finalState == 1 ", "4e" : "finalState == 2 ", "2e2mu": "finalState > 2 "}

dcbMean_reco = {"4mu":124.81, "4e":124.17, "2e2mu":124.51}
dcbMean_refit = {"4mu":124.76, "4e":124.22, "2e2mu":124.54}
dcbMean = {"reco":dcbMean_reco, "refit":dcbMean_refit}

alpha_reco = {"4mu":1.27, "4e":0.80, "2e2mu":1.02}
alpha_refit = {"4mu":1.25, "4e":0.77, "2e2mu":0.91}
alpha = {"reco":alpha_reco, "refit":alpha_refit}

alpha2_reco = {"4mu":1.89, "4e":1.49, "2e2mu":1.82}
alpha2_refit = {"4mu":1.956, "4e":1.476, "2e2mu":1.59}
alpha2 = {"reco":alpha2_reco, "refit":alpha2_refit}

var2Low = {"4mu":0.005, "4e":0.007, "2e2mu":0.005}
var2High = {"4mu":0.05, "4e":0.1, "2e2mu":0.07}

for fs in channels:
    for m4lType in m4lTypes:

        if m4lType == "reco":

           pdfErrFile = modelPath + "templates2D/Dm_signal_"+fs+".root"
           inputConfig["varName1"] = "mass4l"
           inputConfig["varName2"] = "mass4lErr/mass4l"
           inputConfig["saveName1"] = outputPlotPath+"mass4lFrom2D_"+fs+"_reco"
           inputConfig["saveName2"] = outputPlotPath+"mass4lErrFrom2D_"+fs+"_reco"

        if m4lType == "refit": 

           pdfErrFile = modelPath + "templates2D_refit/Dm_signal_"+fs+".root"
           inputConfig["varName1"] = "mass4lREFIT"
           inputConfig["varName2"] = "mass4lErrREFIT/mass4lREFIT"
           inputConfig["saveName1"] = outputPlotPath+"mass4lFrom2D_"+fs+"_refit"
           inputConfig["saveName2"] = outputPlotPath+"mass4lErrFrom2D_"+fs+"_refit"

        inputConfig["cut"] = "passedFullSelection && " + cutREFIT[m4lType] + cutChannel[fs]
        inputConfig["var2Low"] = var2Low[fs]
        inputConfig["var2High"] = var2High[fs]

        do2DFit = Make2DFit(inputConfig)
        do2DFit.MakeDataset()
        do2DFit.MakeModel(dcbMean[m4lType][fs], alpha[m4lType][fs], alpha2[m4lType][fs], pdfErrFile)
        do2DFit.MakeFit()
        do2DFit.MakePlot()
