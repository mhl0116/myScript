from ROOT import *
from array import array
from tdrStyle import *
setTDRStyle()
import sys
from paraConfigurations import *
import argparse

def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('-t', dest='tag', type=str, help='for each plot')

    args = parser.parse_args()
    return args

args=ParseOption()

tag = args.tag
paraConfig = paraConfigs[tag]

rootPath1 = paraConfig['rootPath1']
rootPath2 = paraConfig['rootPath2']
rootfile1 = paraConfig['rootfile1']
rootfile2 = paraConfig['rootfile2']
tree1 = paraConfig['tree1']
tree2 = paraConfig['tree2']
binInfo = paraConfig['binInfo']
vars1 = paraConfig['vars1']
vars2 = paraConfig['vars2']
cuts1 = paraConfig['cuts1']
cuts2 = paraConfig['cuts2']
weight1 = paraConfig['weight1']
weight2 = paraConfig['weight2']
xTitle = paraConfig['xTitle']
yTitle = paraConfig['yTitle']
legend1 = paraConfig['legend1']
legend2 = paraConfig['legend2']
savePath = paraConfig['savePath']
saveName = paraConfig['saveName']
latexNote1 = paraConfig['latexNote1']
latexNote2 = paraConfig['latexNote2']
doFit = paraConfig['doFit']
pdfName = paraConfig['pdfName']
#color1 = paraConfig['color1']

###
# read from tree
###

f1 = TFile(rootPath1 + rootfile1, 'READ')
f2 = TFile(rootPath2 + rootfile2, 'READ')

t1 = f1.Get(tree1)
t2 = f2.Get(tree2)

hists1 = [ TH1F('hist1_'+str(i),'', binInfo[0], binInfo[1], binInfo[2]) for i in range(len(vars1)) ]
hists2 = [ TH1F('hist2_'+str(i),'', binInfo[0], binInfo[1], binInfo[2]) for i in range(len(vars2)) ]

HIST1 = TH1F('HIST1', '', binInfo[0], binInfo[1], binInfo[2])
HIST2 = TH1F('HIST2', '', binInfo[0], binInfo[1], binInfo[2])

for i in range(len(vars1)):
       t1.Project(hists1[i].GetName(), vars1[i], weight1[i]+"*"+cuts1[i])
       if i == 0:
          HIST1 = hists1[0].Clone()
       else:
          HIST1.Add(hists1[i])
for i in range(len(vars2)):
       t2.Project(hists2[i].GetName(), vars2[i], weight2[i]+"*"+cuts2[i])
       if i == 0:
          HIST2 = hists2[0].Clone()
       else:
          HIST2.Add(hists2[i])

#HIST2.Scale(1/HIST2.Integral()*HIST1.Integral())
#HIST1.Scale(1/HIST1.Integral())
#HIST2.Scale(1/HIST2.Integral())
   
HIST1.Sumw2()
HIST2.Sumw2()

###
# do plot
###

c1 = TCanvas("c1", "c1", 800, 800)
c1.SetLeftMargin(0.15)
c1.SetBottomMargin(0.2)
#c1.SetLogy()

pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
pad1.SetBottomMargin(0)
pad1.SetGridx()
pad1.Draw()
pad1.cd()
#pad1.SetLogy()

dummy = TH1D("dummy","dummy",1,binInfo[1],binInfo[2])
dummy.SetMinimum(0)
yMax1 = HIST1.GetMaximum()*1.2
yMax2 = HIST2.GetMaximum()*1.2
yMax_nofit = max(yMax1,yMax2)
dummy.SetMaximum(yMax_nofit)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle(yTitle)
dummy.GetYaxis().SetTitleOffset(1.4)
dummy.GetXaxis().SetTitle(xTitle)
#dummy.GetXaxis().SetLableOffset(1.2)
dummy.Draw()

HIST1.Draw('hist same')
HIST2.Draw('hist same')

HIST1.SetLineColor(1)
HIST2.SetLineColor(2)
HIST1.SetLineWidth(1)
HIST2.SetLineWidth(1)

legend = TLegend(0.2,0.8,0.85,0.9)
legend.AddEntry(HIST1, legend1, 'l')
legend.AddEntry(HIST2, legend2, 'l')
legend.SetTextSize(0.04)
legend.SetLineWidth(2)
legend.SetFillColor(0)
legend.SetBorderSize(0)
legend.Draw('SAME')

latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.6*c1.GetTopMargin())
latex.SetTextFont(42)
latex.SetTextAlign(11)

latex.SetTextColor(1)
latex.DrawLatex(0.45, 0.85, latexNote1)
if len(latexNote2) > 0:
   latex.DrawLatex(0.45, 0.75, latexNote2)

c1.cd()
pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
#pad2.SetLogy()
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.2)
pad2.SetGrid()
pad2.Draw()
pad2.cd()
#make ratio plot
ratio = HIST1.Clone("ratio")
ratio.SetMinimum(0.0)
ratio.SetMaximum(0.2)
#ratio.Sumw2()
ratio.SetStats(0)
ratio.Divide(HIST2)
ratio.SetMarkerStyle(20)
ratio.Draw('e1p')
ratio.SetTitle("")
ratio.GetYaxis().SetTitle("black/red ratio")
ratio.GetXaxis().SetTitle(xTitle)
ratio.GetYaxis().SetTitleSize(30)
ratio.GetYaxis().SetTitleFont(43)
ratio.GetYaxis().SetTitleOffset(1.55)
ratio.GetYaxis().SetLabelFont(43)
ratio.GetYaxis().SetLabelSize(25)
ratio.GetXaxis().SetTitleSize(30)
ratio.GetXaxis().SetTitleFont(43)
ratio.GetXaxis().SetTitleOffset(3.)
ratio.GetXaxis().SetLabelFont(43)
ratio.GetXaxis().SetLabelSize(25)

'''
latex2 = TLatex()
latex2.SetNDC()
latex2.SetTextSize(0.5*c1.GetTopMargin())
latex2.SetTextFont(42)
latex2.SetTextAlign(31) # align right                                                                     
latex2.DrawLatex(0.90, 0.95,"#sqrt{s} = 13 TeV")
latex2.SetTextSize(0.8*c1.GetTopMargin())
latex2.SetTextFont(62)
latex2.SetTextAlign(11) # align right                                                                     
latex2.DrawLatex(0.15, 0.95, "CMS")
latex2.SetTextSize(0.6*c1.GetTopMargin())
latex2.SetTextFont(52)
latex2.SetTextAlign(11)
latex2.DrawLatex(0.28, 0.95, "Simulation")
latex2.DrawLatex(0.465, 0.95, "Preliminary")
latex2.SetTextFont(42)
latex2.SetTextSize(0.45*c1.GetTopMargin())
'''

c1.SaveAs(savePath+saveName+'.png')
c1.SaveAs(savePath+saveName+'.pdf')
c1.SaveAs(savePath+saveName+'.root')

with open(savePath + saveName + ".txt", "w") as myfile:
   myfile.write('rootPath1: ' + rootPath1 + '\n')
   myfile.write('rootfile1: ' + rootfile1 + '\n')
   for i in range(len(vars1)):
       myfile.write('var1: ' + vars1[i] + '\n')
       myfile.write('cut1: ' + cuts1[i] + '\n\n')

   myfile.write('rootPath2: ' + rootPath2 + '\n')
   myfile.write('rootfile2: ' + rootfile2 + '\n')
   for i in range(len(vars2)):
       myfile.write('var2: ' + vars2[i] + '\n')
       myfile.write('cut2: ' + cuts2[i] + '\n\n')
   
myfile.close()


outRootFile = ROOT.TFile("LUT_"+saveName+".root","RECREATE")
ratio.Write()
outRootFile.Close()
