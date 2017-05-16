import ROOT
from tdrStyle import *
setTDRStyle()
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit.so')
import sys
import time
import datetime
from subprocess import call
import os.path

def WriteLog(saveInfo, log, overwrite=True):

    if (overwrite):
       with open(saveInfo+".txt", "w+") as myfile:
            myfile.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " EDT \n")
            myfile.write(log + "\n")
       myfile.close()
    else:
       with open(saveInfo+".txt", "a+") as myfile:
            myfile.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " EDT \n")
            myfile.write(log + "\n")
       myfile.close()


class MakeFitPlot():

      def __init__(self, config):

          # load configurations
          '''
          self.doUnbin = config["unbinFit"]
          self.inputfilepath = config["inputfilepath"]
          self.inputfilename = config["inputfilename"]
          self.treename = config["treename"]
          self.cut = config["cut"]
          '''

          self.config = config

          self.x_low = self.config["x_low"]
          self.x_high = self.config["x_high"]
          self.x_bins = self.config["x_bins"]
          #self.pdfname = config["pdfname"]
          # for bin fit
          '''
          self.roorealvars = config["roorealvars"]     
          self.plotVarFormula = config["plotVarFormula"]
          self.plotArgList = config["plotArgList"]
          
          # set up plot
          self.doLogy = config["doLogy"]
          self.xTitle = config["xTitle"]
          self.yTitle = config["yTitle"]
          self.savepath = config["savepath"]
          self.savename = config["savename"]
          # save input config
          with open(self.savepath+self.savename+".txt", "a+") as myfile:
               myfile.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " EDT \n")
               myfile.write("inputfile: " + self.inputfilepath + self.inputfilename + "\n")
               myfile.write("cut: " + self.cut + "\n")
               myfile.write("plotVariable: " + self.plotVarFormula + "\n")
          myfile.close()
          '''

          # initialize a workspace
          self.var_x = ROOT.RooRealVar("x", "", self.x_low, self.x_high)
          self.w = ROOT.RooWorkspace()
          getattr(self.w, 'import')(self.var_x)

          '''
          # assemble rooargset for roodataset
          self.rooargset = ROOT.RooArgSet()
          for roorealvar in self.roorealvars:
              self.rooargset.add(roorealvar)
          '''
 
          self.dataset = ROOT.RooDataSet()
          self.fitResult = ROOT.RooFitResult()
    
          self.chi2 = -1

      def MakeDataset(self):

          self.doUnbin = self.config["unbinFit"]
          self.inputfilepath = self.config["inputfilepath"]
          self.inputfilename = self.config["inputfilename"]
          self.treename = self.config["treename"]
          self.cut = self.config["cut"]

          self.roorealvars = self.config["roorealvars"]
          self.plotVarFormula = self.config["plotVarFormula"]
          self.plotArgList = self.config["plotArgList"]

          self.rooargset = ROOT.RooArgSet()
          for roorealvar in self.roorealvars:
              self.rooargset.add(roorealvar)

          file_ = ROOT.TFile(self.inputfilepath + self.inputfilename)
          tree_ = file_.Get(self.treename)

          if self.doUnbin:

             self.dataset = ROOT.RooDataSet("dataset", "", tree_, self.rooargset, self.cut)
             x_formula = ROOT.RooFormulaVar("x", "",  self.plotVarFormula, self.plotArgList)                          
             x_indata = self.dataset.addColumn(x_formula)
             x_indata.setRange(self.x_low,self.x_high)


      def SetUpPlotVar(self, dataset):

          x_formula = ROOT.RooFormulaVar("x", "",  self.plotVarFormula, self.plotArgList)
          dataset = dataset.addColumn(x_formula)
          dataset.setRange(self.x_low,self.x_high)


      def MakePlot(self): 

          self.var = self.w.var("x")#self.config["var"]
          pdf = self.config["pdf"]
          dataset = self.config["dataset"]

          self.doLogy = self.config["doLogy"]
          self.xTitle = self.config["xTitle"]
          self.yTitle = self.config["yTitle"]
          self.savepath = self.config["savepath"]
          self.savename = self.config["savename"]

          ### parepare frame 
          self.var.setBins(self.x_bins)
          frame = self.var.frame()

          dataset.plotOn(frame, ROOT.RooFit.MarkerStyle(20), ROOT.RooFit.MarkerColor(1))
          pdf.plotOn(frame, ROOT.RooFit.LineWidth(2), ROOT.RooFit.LineColor(4))

          pdf.paramOn(frame, ROOT.RooFit.Layout(0.2, 0.85, 0.9), ROOT.RooFit.Format("NE", ROOT.RooFit.FixedPrecision(6)))

          dataset.plotOn(frame, ROOT.RooFit.MarkerStyle(20), ROOT.RooFit.MarkerColor(1))
          pdf.plotOn(frame, ROOT.RooFit.LineWidth(2), ROOT.RooFit.LineColor(4))
          #frame.getAttText().SetTextSize(0.02)

          self.chi2 = frame.chiSquare(self.fitResult.floatParsFinal().getSize())

          ### plot
          c = ROOT.TCanvas("c","",800,800)
          c.SetLeftMargin(0.15) 
          if self.doLogy: c.SetLogy()
          dummy = ROOT.TH1D("dummy","dummy",1,self.x_low,self.x_high)
          dummy.SetMinimum(int(self.doLogy) )
          dummy.SetMaximum(frame.GetMaximum()*2)
          dummy.SetLineColor(0)
          dummy.SetMarkerColor(0)
          dummy.SetLineWidth(0)
          dummy.SetMarkerSize(0)
          dummy.GetYaxis().SetTitle(self.yTitle)
          dummy.GetYaxis().SetTitleOffset(1.5)
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

                
      def MakeGenShape(self):

          file_ = ROOT.TFile(self.inputfilepath + self.inputfilename)
          tree_ = file_.Get(self.treename)

          tmpHist_ = ROOT.TH1F("tmpHist","",self.x_bins,self.x_low,self.x_high)
          tree_.Project("tmpHist", self.plotVarFormula, "1*"+self.cut)

          datahist_ = ROOT.RooDataHist("tmpDatahist","", ROOT.RooArgList(self.w.var("x")), tmpHist_)
          histpdf_ = ROOT.RooHistPdf("genshape","", ROOT.RooArgSet(self.w.var("x")), datahist_)

          w_histpdf = ROOT.RooWorkspace("w_histPdf")
          getattr(w_histpdf, 'import')(histpdf_)

          w_histpdf.writeToFile(self.savepath + self.savename + ".root")
          
      def LoadGenShape(self, histpdfname):

          histpdffile = ROOT.TFile("histpdf/" + histpdfname + ".root")
          histpdfws_ = histpdffile.Get("w_histPdf")
          histpdf_ = histpdfws_.pdf("genshape")
          getattr(self.w, 'import')(histpdf_)


      
      def SaveConfig(self):

         # save input config
          with open(self.savepath+self.savename+".txt", "w+") as myfile:
               myfile.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " EDT \n")
               myfile.write("inputfile: " + self.inputfilepath + self.inputfilename + "\n")
               myfile.write("cut: " + self.cut + "\n")
               myfile.write("plotVariable: " + self.plotVarFormula + "\n")
          myfile.close()

      def MakePdfFactory(self):

          self.w.factory('DoubleCB::doubleCB_1(x, \
                          meanDCB[0,-0.1,0.1], sigmaDCB[0.01,0,10], \
                          alphaDCB[1,0,5], nDCB[5,0,20], alpha2[1,0,5], n2[5,0,100])')

          self.w.factory('DoubleCB::doubleCB_2(x, \
                          meanDCB_2[125,105,140], sigmaDCB_2[1,0,10], \
                          alphaDCB_2[9.13056e-01,0,10], nDCB_2[5,0.1,20], alpha2_2[1.21649e+00,0,10], n2_2[5,0.1,20])')

          self.w.factory('DoubleCB::doubleCB_3(x, \
                          meanDCB_3[91,70,105], sigmaDCB_3[1,0,10], \
                          alphaDCB_3[9.13056e-01,0,10], nDCB_3[5,0.1,20], alpha2_3[1.21649e+00,0,10], n2_3[5,0.1,20])')

          self.w.factory('DoubleCB::doubleCB_fix_H4mu(x, \
                          meanDCB_fix_H4mu[125.000], sigmaDCB_fix_H4mu[0.00191], \
                          alphaDCB_fix_H4mu[1.082], nDCB_fix_H4mu[1.537], alpha2_fix_H4mu[1.108], n2_fix_H4mu[2.173])')

          self.w.factory('Gaussian::gauss_1(x, meanGauss[0,-0.1,0.1], sigmaGauss[0.01,0,1])')

          self.w.factory('Gaussian::gauss_h_gen(x, meanGauss_h_gen[125], sigmaGauss_h_gen[0.004])')

          self.w.factory('CBShape::singleCB_1(x, meanCB[0,-0.01,0.01], sigmaCB[0.001,0,10], alphaCB[1,0,10], nCB[1,0,50])')

          self.w.factory('BreitWigner::bw_fix(x, meanBW_fix[91.1876], sigmaBW_fix[2.4952])')

          self.w.factory('BreitWigner::bw_h_fix(x, meanBW_h_fix[125], sigmaBW_h_fix[0.004])')

          self.w.factory('BreitWigner::bw_float(x, meanBW_float[91.2,80,100], sigmaBW_float[1,0,10])')
 
          self.w.factory('BreitWigner::bw_h_float(x, meanBW_h_float[125,120,130], sigmaBW_h_float[1,0,10])')

          self.w.factory('FCONV::BWxDCB(x,bw_fix,doubleCB_1)')

          self.w.factory('FCONV::BWxDCB_h(x,bw_h_fix,doubleCB_1)')

          self.w.factory('FCONV::DCBxDCB_h(x,doubleCB_fix_H4mu,doubleCB_1)')

          self.w.factory('FCONV::GaussxDCB_h(x,gauss_h_gen,doubleCB_1)')

          #self.w.factory('FCONV::GENShapexDCB_h(x,genshape,doubleCB_1)')

          self.w.factory('Bernstein::bernstein_float(x, {b0[1,-100,100], b1[10,-100,100], b2[10,-100,100]})')

          self.w.factory('SUM:model_m4l_Z4L(f1[0.8,0,1]*BWxDCB, bernstein_float)')

          #self.w.factory('SUM:model(fsig[0.9,0.7,1]*doubleCB_1, gauss_1)')

