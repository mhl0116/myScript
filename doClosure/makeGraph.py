from ROOT import *
from array import array
import sys

from tdrStyle import *
setTDRStyle()

import argparse
def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('--intxt', dest='intxt', type=str, help='')
    parser.add_argument('--plotpath', dest='plotpath', type=str, help='')
    parser.add_argument('--plotname', dest='plotname', type=str, help='')

    args = parser.parse_args()
    return args

args=ParseOption()

sigma2l_fit = []
sigma2l_pred = []
sigma2l_pred_corr = []

data = [line.strip() for line in open(args.intxt, 'r')]
for i in range(1, len(data)):

    dataperline = data[i].split(' ')
    sigma2l_fit.append(float(dataperline[0]))
    sigma2l_pred.append(float(dataperline[1]))
    sigma2l_pred_corr.append(float(dataperline[2]))

y, x1, x2 = array('f'), array('f'), array('f')

for i in range(len(sigma2l_fit)):
    y.append(sigma2l_fit[i])
    x1.append(sigma2l_pred[i])
    x2.append(sigma2l_pred_corr[i])

for i in range(len(x1)):
  print x1[i]

gr1 = TGraph(len(y),x1,y)
gr2 = TGraph(len(y),x2,y)

c1 = TCanvas('c1', '', 800, 800)

dummy = TH1D("dummy","dummy",1,0,5)
dummy.SetMinimum(0)
dummy.SetMaximum(5)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetXaxis().SetTitle('Predicted #sigma_{2l}')
dummy.GetYaxis().SetTitleOffset(1.3)
dummy.GetYaxis().SetTitle('Measured #sigma_{2l}')
dummy.Draw()

lineBoundDiagonal = TLine(0, 0, 5,5)
lineBoundDiagonal.SetLineStyle(kDashed)
lineBoundDiagonal.Draw()
lineBoundDiagonal_up = TLine(0, 0, 5/1.2,5)
lineBoundDiagonal_up.SetLineStyle(kDashed)
lineBoundDiagonal_up.Draw()
lineBoundDiagonal_down = TLine(0, 0, 5,5/1.2)
lineBoundDiagonal_down.SetLineStyle(kDashed)
lineBoundDiagonal_down.Draw()

gr1.Draw('p')
gr2.Draw('p')

gr1.SetMarkerStyle(20)
gr2.SetMarkerStyle(20)
gr1.SetMarkerColor(1)
gr2.SetMarkerColor(2)

#c1.SaveAs('/home/mhl/public_html/2016/20161020_mass/fitmassZ/closureZ.png')
c1.SaveAs(args.plotpath+args.plotname)

