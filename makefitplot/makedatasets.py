from subprocess import call
import os.path
import sys

#pt_fullRange = [4,100]
#eta_fullRange = [0,2.4]

dPhi_fullRange = [0,3.15]

#process = "H4L"
#process = "Z4L"
process = "ZZ4L"
#process = "Z2L"

datasetpath = "/raid/raid8/mhl/HZZ4L_Run2_post2017Moriond/roodatasets/"
#datasetname = "muCurveResidual_pt_"+process
#datasetname = "muPtResidual_allM4l_"+process
#datasetname = "muPtResidual_allM4l_combine124_125_126_" + process
#datasetname = "muPtResidual_allM4l_MuPt4_Z2AT4_noFSR_" + process
#datasetname = "muPtResidual_allM4l_combine_ggH125_zz4L_Z2AT4_L234_" + process
#datasetname = "muPtResidual_allM4l_combine_ggH124_125_126_zz4L_Z2AT12_" + process

#datasetname = "muPtResidual_muMinus_" + process
#datasetname = "muPtCurvature_muMinus_" + process

datasetname = "ZLepDeltaPhi_" + process


'''
lepIndexs = [1,2,3,4]

for lepIndex in lepIndexs:

    datasetname_tmp = datasetname + "_L" + str(lepIndex)
    tmpConfig = 'setup_muPtResidual_' + process + '_makeDataset.py'
#    tmpConfig = 'setup_muPtCurvature_' + process + '_makeDataset.py'

    cmd1 = 'python setups/' + tmpConfig + ' --pts ' + str(pt_fullRange[0]) + ' ' + str(pt_fullRange[1]) + \
                     ' --etas ' + str(eta_fullRange[0]) + ' ' + str(eta_fullRange[1]) + \
                     ' --datasetpath ' + datasetpath + ' --datasetname ' + datasetname_tmp + \
                     ' --lepIndex ' + str(lepIndex)  + ' &'

    print cmd1
    call(cmd1, shell=True)
'''

for index in [1,2]:
    datasetname_tmp = datasetname + "_L" + str(index)
    tmpConfig = 'setup_ZLepDeltaPhi_makeDataset.py'
    cmd1 = 'python setups/' + tmpConfig + ' --dPhis ' + str(dPhi_fullRange[0]) + ' ' + str(dPhi_fullRange[1]) + \
                     ' --datasetpath ' + datasetpath + ' --datasetname ' + datasetname_tmp + \
                     ' --index ' + str(index)  + ' &'

    print cmd1
    call(cmd1, shell=True)

