from subprocess import call
import os.path
import sys

pt_fullRange = [5,100]
eta_fullRange = [0,2.4]

process = "H4L"
#process = "Z4L"
#process = "ZZ4L"
#process = "Z2L"

datasetpath = "/raid/raid9/mhl/HZZ4L_Run2_post2017Moriond/roodatasets/"
datasetname = "muMinusCurveResidual_pt_"+process

lepIndexs = [1,2,3,4]

for lepIndex in lepIndexs:

    datasetname_tmp = datasetname + "_L" + str(lepIndex)
    tmpConfig = 'setup_muPtResidual_' + process + '_makeDataset.py'

    cmd1 = 'python setups/' + tmpConfig + ' --pts ' + str(pt_fullRange[0]) + ' ' + str(pt_fullRange[1]) + \
                     ' --etas ' + str(eta_fullRange[0]) + ' ' + str(eta_fullRange[1]) + \
                     ' --datasetpath ' + datasetpath + ' --datasetname ' + datasetname_tmp + \
                     ' --lepIndex ' + str(lepIndex)  + ' &'

    print cmd1
    call(cmd1, shell=True)

