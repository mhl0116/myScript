from ROOT import *

def MakePlot(fileName, fs):

    f1 = TFile(fileName)
    h1 = f1.Get(fs)
    c1 = TCanvas("c1", "c1", 800, 800)
    h1.Draw("text")
    c1.SaveAs("~/public_html/2016/20161006_2015MCebeCorrection/ICHEP_2016MC_LUT/"+ (fileName.split(".")[0])+'.png')


MakePlot('DYJetsToLL_M-50_m2eLUT_m2e.root', '2e')
MakePlot('DYJetsToLL_M-50_m2muLUT_m2mu.root', '2mu')
#MakePlot('DoubleLepton_m2eLUT_m2e.root', '2e')
#MakePlot('DoubleLepton_m2muLUT_m2mu.root', '2mu')
