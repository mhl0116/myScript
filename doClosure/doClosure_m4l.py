from ROOT import *
import makePlot_1D_fit
#RooMsgService.instance().Print() 
#RooMsgService.instance().getStream(1).removeTopic(RooFit.ObjectHandling)
#RooMsgService.instance().getStream(1).removeTopic(RooFit.DataHandling)
#RooMsgService.instance().getStream(1).removeTopic(RooFit.Eval)
#RooMsgService.instance().getStream(1).removeTopic(RooFit.Caching)
#RooMsgService.instance().setGlobalKillBelow(RooFit.WARNING)
import argparse
def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('--min', dest='min_m4lErr', type=float, help='min for relMassZErr')
    parser.add_argument('--max', dest='max_m4lErr', type=float, help='max for relMassZErr')
    parser.add_argument('--channel', dest='channel', type=str, help='channel')
    args = parser.parse_args()
    return args

args=ParseOption()

m4lErr_min = args.min_m4lErr #0.006
m4lErr_max = args.max_m4lErr #0.008

### move to previous level, open tree only once???
inputPath = '/cms/data/scratch/osg/mhl/Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/Ana_ZZ4L/Ntuples/'
inputFile = 'mH_125.root'
treeName = 'passedEvents'

savePath = '/home/mhl/public_html/2016/20161021_mass/fitmassH/'
### move to previous level

saveName = 'mass4l_HErr_' + str(m4lErr_min).replace('.','p') + '_' + str(m4lErr_max).replace('.','p')

channelCut = {'4mu':'(finalState == 1)', '4e':'(finalState == 2)', '2e2mu':'(finalState > 2)'}

cut = "passedFullSelection && mass4l > 105 && mass4l < 140 && \
       mass4lErr > " + str(m4lErr_min) + " && \
       mass4lErr < " + str(m4lErr_max)
cut += channelCut[args.channel]

plotParaConfig = \
{\
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'cuts1': ['1'], #
'weight1': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': str(m4lErr_min) + ' < m_{4l} < ' + str(m4lErr_max),
'pdfName': 'doubleCB'
}

#initialize to-be-saved fitted parameter 
fitResult = {'sigmaCB':0, 'sigmaDCB':0}

myFile = TFile(inputPath+inputFile,'READ')
myTree = myFile.Get(treeName)

#TProof.Open("")
#c = TChain("myTree")
#c.Draw(">>myList", cut, "entrylist")

#select part of tree to be used
myTree.Draw(">>myList", cut, "entrylist")
entryList = gDirectory.Get("myList")
myTree.SetEntryList(entryList)

#plot and fit massZ, get fitted sigma
makePlot_1D_fit.MakeFitPlotFromTree(myTree, plotParaConfig, fitResult)

print fitResult
selector = TSelector.GetSelector("MySelector_m4l.C")
myTree.Process(selector)

#corred m4l = selector.mass4lErr

### should make following lines more clean ...
sigma_m2l = [fitResult['sigma'], selector.massZErr_sum/selector.nEvents,\
                                 selector.massZErr_sum_corr/selector.nEvents]#,\
#                                 selector.massZErr_sum_rel/selector.nEvents,\
#                                 selector.massZErr_sum_rel_corr/selector.nEvents]
print ''
print sigma_m2l
sigma_m2l = [str(sigma_m2l[i]) for i in range(len(sigma_m2l))]

with open("sigma_m2l.txt",'a') as myfile:
     myfile.write(sigma_m2l[0] + ' ' + sigma_m2l[1] + ' ' + sigma_m2l[2] + '\n')
#     myfile.write(sigma_m2l[0] + ' ' + sigma_m2l[1] + ' ' + sigma_m2l[2] + ' ' + sigma_m2l[3] + ' ' + sigma_m2l[4] + '\n')

