from subprocess import call
import os.path

pts = [5,20,40,50,60,100]
#etas = [0,0.9]#,1.8,2.4]
#etas = [0.9,1.8]#,1.8,2.4]
#etas = [1.8,2.4]#,1.8,2.4]

summaryTxtPath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/txtfiles/"
summaryTxtName = "Z4L_muPtResidual.txt"

summaryTxt = summaryTxtPath+summaryTxtName
#if (os.path.exists(summaryTxt)): 
#   call('rm ' + summaryTxt, shell=True)


for i in range(len(pts)-1):
    for j in range(len(etas)-1):
        cmd = 'python setup.py --pts ' + str(pts[i]) + ' ' + str(pts[i+1]) + \
                            ' --etas ' + str(etas[j]) + ' ' + str(etas[j+1]) + \
                            ' --txtpath ' + summaryTxtPath + \
                            ' --txtname ' + summaryTxtName + ' &'
        print cmd
        call(cmd, shell=True)

