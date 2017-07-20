from subprocess import call
import os.path
import sys

#pts = [50,60]#20,30,40,50,60,100]
#etas = [0.9,1.4] #[0.0,0.9,1.4,2.4]
Vars = [0,1.5,2,2.5,3,3.5,4,6]
tag = "test"

#process = "H4L"
#process = "Z4L"
#process = "ZZ4L"
process = "Z2L"
plotpath = "/home/mhl/public_html/2017/20170720_massZ_deltaR/"+process+"_"+tag+"/"

summaryTxtPath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = process + "_massZ_deltaR_"+tag+".txt"

#datasetpath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/roodatasets/"
#datasetname = "muPtResidual_pt_"+process
summaryTxt = summaryTxtPath+summaryTxtName

if (os.path.exists(summaryTxt)): 
   call('rm ' + summaryTxt, shell=True)

if (not os.path.exists(plotpath)):
   call('mkdir ' + plotpath, shell=True)
   call('cp /home/mhl/public_html/index.php ' + plotpath, shell=True)

#lepIndexs = [1,2,3,4]

for i in range(len(Vars)-1):
#    for j in range(len(etas)-1):
#        for lepIndex in lepIndexs:
            cmd = 'python setups/setup_fit_vs_var.py --Vars ' + str(Vars[i]) + ' ' + str(Vars[i+1]) + \
                            ' --txtpath ' + summaryTxtPath + \
                            ' --txtname ' + summaryTxtName + \
                            ' --plotpath ' + plotpath 
                         

#            cmd = 'python setups/setup_muPtResidual_' + process + '_makeFit.py --pts ' + str(pts[i]) + ' ' + str(pts[i+1]) + \
#                            ' --etas ' + str(etas[j]) + ' ' + str(etas[j+1]) + \
#                            ' --txtpath ' + summaryTxtPath + \
#                            ' --txtname ' + summaryTxtName + \
#                            ' --plotpath ' + plotpath + \
#                            ' --datasetpath ' + datasetpath + \
#                            ' --datasetname ' + datasetname #+ ' &'
            print cmd
            call(cmd, shell=True)


