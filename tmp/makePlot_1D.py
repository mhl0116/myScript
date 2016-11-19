from ROOT import *
from array import array

from tdrStyle import *
setTDRStyle()

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

HIST1.Scale(1/HIST1.Integral())
HIST2.Scale(1/HIST2.Integral())

c1 = TCanvas("c1", "c1", 800, 800)

dummy = TH1D("dummy","dummy",1,binInfo[1],binInfo[2])
dummy.SetMinimum(0)
yMax1 = HIST1.GetMaximum()*1.5
yMax2 = HIST2.GetMaximum()*1.5
yMax = max(yMax1,yMax2)
dummy.SetMaximum(yMax)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle(yTitle)
dummy.GetYaxis().SetTitleOffset(1.3)
dummy.GetXaxis().SetTitle(xTitle)
dummy.Draw()

HIST1.Draw('hist same')
HIST2.Draw('hist same')

HIST1.SetLineColor(1)
HIST2.SetLineColor(2)
HIST1.SetLineWidth(1)
HIST2.SetLineWidth(1)

legend = TLegend(0.15,0.75,0.42,0.9)
legend.AddEntry(HIST1, legend1, 'l')
legend.AddEntry(HIST2, legend2, 'l')
legend.SetTextSize(0.03)
legend.SetLineWidth(2)
legend.SetFillColor(0)
legend.SetBorderSize(1)
legend.Draw('SAME')

latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.45*c1.GetTopMargin())
latex.SetTextFont(42)
latex.SetTextAlign(11)
latex.DrawLatex(0.45, 0.85, latexNote1)
if len(latexNote2) > 0:
   latex.DrawLatex(0.45, 0.75, latexNote2)
c1.SaveAs(savePath+saveName+'.png')
c1.SaveAs(savePath+saveName+'.pdf')

