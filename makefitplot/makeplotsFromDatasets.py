import ROOT
from subprocess import call
import os.path
import sys
import makefitplot as fplt

sys.path.insert(0, '/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/plotScript/utils')
import utils

#process = "H4L"
process = "Z4L"
#process = "ZZ4L"
##process = "Z2L"
#datasetfileBase = "muPtResidual_allM4l"
#datasetfileBase = "muPtResidual_allM4l_Z2AT4"
#datasetfileBase = "muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4"
#datasetfileBase = "muPtResidual_allM4l_combine_ggH124_125_126_zz4L_Z2AT12"
#datasetfileBase = "muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4_L34"
#datasetfileBase = "muPtResidual_allM4l_combine_ggH_ZZ4L"
#datasetfileBase = "muPtResidual_pt"
#datasetfileBase = "muCurveResidual_pt_nofsr"
#datasetfileBase = "muPlusCurveResidual_pt"
#datasetfileBase = "muMinusCurveResidual_pt"
#datasetfileBase = "muPtResidual_allM4l_combine124_125_126"
#datasetfileBase = "muPtResidual_allM4l_MuPt4_Z2AT4_withFSR"
#datasetfileBase = "muPtResidual_allM4l_MuPt4_Z2AT4_noFSR"
#datasetfileBase = "muPtCurvature_muPlus"
datasetfileBase = "muPtResidual_muMinus"
#tag = datasetfileBase + "_lowPt"
#tag = datasetfileBase + "_fullRange"
#tag = datasetfileBase + "_eta_0p0_0p9_pt_10_100"
#tag = datasetfileBase + "_eta_1p8_2p4_pt_10_100"
#tag = datasetfileBase + "_checkEta"
#tag = datasetfileBase + "_allM4l_combine_124_125_126"
#tag = datasetfileBase + "_allM4l_combine_ggH_ZZ4L"
tag = datasetfileBase #+ "_plus1Sigma"# + "_pt_9_10_11" #+ "_use_3and4_lep"

plotdir = "20170719_" + datasetfileBase 

#pTs = [5,6,7,8,9,10,15,25,40,100]
pTs = [5,6,7,8,9,10,15,20,25,30,35,40,45,50,100]#,25,40,100]

#pTs[:] = [1.0/x for x in pTs]
#pTs = pTs[::-1]
#pTs.append(0.2)

etas = [0.0,0.9,2.4]

#####
#less modify
#####

plotpath = "/home/mhl/public_html/2017/"+plotdir+"/"+process+"_"+tag+"/"
if (not os.path.exists(plotpath)):
   call('mkdir -p ' + plotpath, shell=True)
   call('cp /home/mhl/public_html/index.php ' + plotpath, shell=True)
else:
   continueFit =  raw_input('plot dir "' + plotpath  + '" exsit, overwrite ? : ')
   if (not (continueFit == "y" or continueFit == "yes") ):
      print "path: " + plotpath  + " exsit, move them away or create new dir first !"
      sys.exit()
   else:
      call('rm  ' + plotpath + '*.png',shell=True)
      call('rm  ' + plotpath + '*.pdf',shell=True)
      call('rm  ' + plotpath + '*.txt',shell=True)

pdfName1 = "doubleCB_1"
#pdfName2 = "doubleCB_1"
pdfName2 = "gauss_2"

datafilepath = "/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/roodatasets/"

xLow = -0.5
xHigh = 0.5
xBins = 100

# save fitted parameters 
summaryTxtPath = "/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
#summaryTxtPath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
#summaryTxtName = process + "_muPtPull_eta_"+tag+".txt"
summaryTxtName = process + "_" + tag+".txt"
summaryTxt = summaryTxtPath+summaryTxtName
if (os.path.exists(summaryTxt)): 
   call('rm ' + summaryTxt, shell=True)

for i in range(len(pTs)-1):
    for j in range(len(etas)-1):

        pTLow = pTs[i]
        pTHigh = pTs[i+1]
        etaLow = etas[j]
        etaHigh = etas[j+1]
        config = {\
        "x_low":xLow,\
        "x_high":xHigh,\
        "x_bins":xBins,\
        "doLogy":False,\
        "xTitle":"(pT_{reco}-pT_{gen})/pT_{gen}",\
#        "xTitle":"(1/pT_{reco}-1/pT_{gen})/(1/pT_{gen})",\
        "yTitle":"Events/" + str((xHigh-xLow)/xBins),\
        "savepath":plotpath
        }

#        config["savename"] = "muPtCurvature_" + str(pTLow).replace(".","p") + "_" + str(pTHigh).replace(".","p") \
        config["savename"] = "muPtResidual_pt_" + str(pTLow).replace(".","p") + "_" + str(pTHigh).replace(".","p") \
                                       + "_eta_" + str(etaLow).replace(".","p") + "_" + str(etaHigh).replace(".","p") + "_dcb"
        logDataset = ''
        logCut = ''

        datasets = []

        # gather information from 4 leptons
        for k in [1,2,3,4]:
#        for k in [3,4]:

            datasetfile = datasetfileBase + "_" + process + "_L"+str(k)+".root"

            datafile = ROOT.TFile(datafilepath + datasetfile)
            logDataset += datafilepath + datasetfile + '\n'
            tmpworkspace = datafile.Get("w_out")
            dataset = tmpworkspace.obj("dataset")
           
            print dataset.sumEntries()

             
            cut = "pTGENL" + str(k) + " > " + str(pTLow) + " && pTGENL" + str(k) + " < " + str(pTHigh) + " && \
                   abs(etaL" + str(k) + ") > " + str(etaLow) + " && abs(etaL" + str(k) + ") < " + str(etaHigh) 
            #cut = "1/pTGENL" + str(k) + " > " + str(pTLow) + " && 1/pTGENL" + str(k) + " < " + str(pTHigh) + " && \
            #       abs(etaL" + str(k) + ") > " + str(etaLow) + " && abs(etaL" + str(k) + ") < " + str(etaHigh)
#                   etaL" + str(k) + " > " + str(etaLow) + " && etaL" + str(k) + " < " + str(etaHigh)

            rv_genPt = ROOT.RooRealVar("pTGENL"+str(k),"",0,100)
            rv_pT = ROOT.RooRealVar("pTL"+str(k),"",0,100)
            rv_eta = ROOT.RooRealVar("etaL"+str(k),"",-2.4,2.4)
            '''
            cut = "pTGEN_noFSR_L" + str(k) + " > " + str(pTLow) + " && pTGEN_noFSR_L" + str(k) + " < " + str(pTHigh) + " && \
                   abs(eta_noFSR_L" + str(k) + ") > " + str(etaLow) + " && abs(eta_noFSR_L" + str(k) + ") < " + str(etaHigh)
            rv_genPt = ROOT.RooRealVar("pTGEN_noFSR_L"+str(k),"",0,100)
            rv_pT = ROOT.RooRealVar("pT_noFSR_L"+str(k),"",0,100)
            rv_eta = ROOT.RooRealVar("eta_noFSR_L"+str(k),"",-2.4,2.4)
            ''' 

            logCut += cut + '\n'

            rv_x = ROOT.RooRealVar("x","",xLow,xHigh)

            dataset_select = ROOT.RooDataSet("dataset_select_"+str(k),"",dataset, ROOT.RooArgSet(rv_genPt,rv_pT,rv_eta,rv_x),cut)
#                                  ROOT.RooArgSet(rv_passedFullSelection,rv_mass4l,rv_finalState,rv_genPt,rv_pT,rv_eta,rv_x),cut)

            print dataset_select.sumEntries()
 
            # plot only interesting variable x, and avoid problem when append if different dataset have different columns  
            dataset_reduce = dataset_select.reduce(ROOT.RooArgSet(rv_x))
            datasets.append(dataset_reduce)

        # append x from 4 leptons into one dataset, ready for fit and plot
        dataset_append = ROOT.RooDataSet(datasets[0], "dataset_append")
        dataset_append.append(datasets[1])
        dataset_append.append(datasets[2])
        dataset_append.append(datasets[3])

        # make a new class for fit plot
        fplot = fplt.MakeFitPlot(config) # config needed in MakePlot
        fplot.MakePdfFactory()
        pdf1 = fplot.w.pdf(pdfName1)
        fplot.fitResult = pdf1.fitTo(dataset_append, ROOT.RooFit.Save(True))

        fplot.config["dataset"] = dataset_append
        fplot.config["pdf"] = pdf1
 
        fplot.MakePlot()
        fplt.WriteLog(config["savepath"]+config["savename"],"dataset:\n " + logDataset)
        fplt.WriteLog(config["savepath"]+config["savename"],"cut:\n " + logCut,False)

        # save sigma and alpha1,2 from fitted dcb, proceed with gaussian fit
        mean = fplot.w.var("meanDCB").getVal()
        sigma = fplot.w.var("sigmaDCB").getVal() 
        alpha1 = fplot.w.var("alphaDCB").getVal()
        alpha2 = fplot.w.var("alpha2").getVal()
        newFitRange = min(alpha1,alpha2)*sigma*0.7
        xLow_new = -1*newFitRange + mean
        xHigh_new = newFitRange + mean

        # make new dataset, only allow data with smaller x range [-sigma*min(a1,a2), sigma*min(a1,a2)] * somefactor
        x_Average = utils.GetAverage(dataset_append,rv_x)
        x_Median = utils.GetMedian(dataset_append,rv_x)
        print "gen: ", utils.GetMin(dataset_select,rv_genPt)
        print "reco: ", utils.GetMin(dataset_select,rv_pT)
        dataset_reduce = dataset_append.reduce("x < " + str(xHigh_new) + " && x > " + str(xLow_new))
        x_Average_2 = utils.GetAverage(dataset_reduce,rv_x)

        # set up config for second make fit plot class
        config["x_low"] = xLow_new
        config["x_high"] = xHigh_new
        config["x_bins"] = 50
        config["yTitle"] = "Events/" + str(round((config["x_high"]-config["x_low"])/config["x_bins"],5) )
        config["savename"] = config["savename"].replace("dcb","gauss")

        # second class for fit plot
        fplot2 = fplt.MakeFitPlot(config)
        fplot2.MakePdfFactory()
        pdf2 = fplot2.w.pdf(pdfName2)
        fplot2.fitResult = pdf2.fitTo(dataset_reduce, ROOT.RooFit.Save(True))
        fplot2.config["dataset"] = dataset_reduce
        fplot2.config["pdf"] = pdf2

        fplot2.MakePlot()
        fplt.WriteLog(config["savepath"]+config["savename"],"dataset:\n " + logDataset)
        fplt.WriteLog(config["savepath"]+config["savename"],"cut:\n " + logCut,False)
        fplt.WriteLog(config["savepath"]+config["savename"], "x > " + str(xLow_new) + " && x < " + str(xHigh_new) )

        with open(summaryTxt, "a+") as myfile:
             myfile.write(' '.join([str(pTLow),str(pTHigh),str(etaLow),str(etaHigh), \
#             str(fplot2.w.var("meanDCB").getVal() ), \
#             str(fplot2.w.var("meanDCB").getError() ) ] ) + '\n' )
             str(fplot2.w.var("meanGauss_2").getVal()), \
             str(fplot2.w.var("meanGauss_2").getError() ), \
             str(x_Average), str(x_Median) ] ) + '\n' )
        myfile.close()

