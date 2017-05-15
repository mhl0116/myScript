from subprocess import call
import os.path
import sys

pts = [50,60]#20,30,40,50,60,100]
#pts = [5,10,15,20,25,30,35,40,45,50,100]
#pts = [5,15]
etas = [0.9,1.4] #[0.0,0.9,1.4,2.4]
tag = "fullRange"
#tag = str(etas[0]).replace(".","p") + "_" + str(etas[1]).replace(".","p")#"0p0_2p4"

process = "H4L"
#process = "Z4L"
#process = "ZZ4L"
#process = "Z2L"
plotpath = "/home/mhl/public_html/2017/20170515_checkMuPtResidual_gauss/"+process+"_"+tag+"/"

summaryTxtPath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = process + "_muPtResidual_eta_"+tag+".txt"

datasetpath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/roodatasets/"
datasetname = "muPtResidual_pt_"+process
summaryTxt = summaryTxtPath+summaryTxtName

if (os.path.exists(summaryTxt)): 
   call('rm ' + summaryTxt, shell=True)

if (not os.path.exists(plotpath)):
   call('mkdir ' + plotpath, shell=True)
   call('cp /home/mhl/public_html/index.php ' + plotpath, shell=True)

lepIndexs = [1,2,3,4]

for i in range(len(pts)-1):
    for j in range(len(etas)-1):
        for lepIndex in lepIndexs:

            cmd = 'python setups/setup_muPtResidual_' + process + '_makeFit.py --pts ' + str(pts[i]) + ' ' + str(pts[i+1]) + \
                            ' --etas ' + str(etas[j]) + ' ' + str(etas[j+1]) + \
                            ' --txtpath ' + summaryTxtPath + \
                            ' --txtname ' + summaryTxtName + \
                            ' --plotpath ' + plotpath + \
                            ' --datasetpath ' + datasetpath + \
                            ' --datasetname ' + datasetname #+ ' &'
            print cmd
            call(cmd, shell=True)


