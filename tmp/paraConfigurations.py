paraConfigs = { }

mc2015_dy_path = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/inputRootFiles/'
mc2016_dy_path = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/inputRoot/forApproval/'
mc2015_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/'
mc2016_dy_path_withgenpt = '/raid/raid9/mhl/HZZ4L_Run2/HZZ4L/PereventMassErrCorr_2016ICHEP/getCorrection_ICHEP2016/makeSlimTree/'

mc2015_dy_path_v4 = "/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_2015MC/HZZ4L_Mass/makeSlimTree/DY_2015MC_kalman_v4/"


savePath = '/home/mhl/public_html/2016/20161012_investigateGENZrecoz/'

#make plots in different ptEta bins
skimmedDY_cut = 'massZ > 80 && massZ < 100 && massZErr > 0.2 && massZErr < 7.2 && Met < 30 && '
skimmedDY_cutOnGEN = 'GENmass2l > 80 && GENmass2l < 100 && '

saveName = 'pullZ_2015MC'
paraConfigs['mc_DY15_pullz'] = \
{\
'rootPath1': mc2015_dy_path_v4,
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo': [100, -3, 3],
'vars1': ['(massZ-GENmass2l)/massZErr'],
'cuts1': [skimmedDY_cut + ' genLep_pt1 > 0 && genLep_pt2 > 0'], #
'weight1': ['1'],
'xTitle': '(massZ_{reco}-GENmass2l)/massZErr',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': ' ',
'pdfName': 'doubleCB'
}

cut_hasLeg1 = ' ((pT2 > 40 && pT2 < 50 && abs(eta2) > 0 && abs(eta2) < 0.9) || (pT1 > 40 && pT1 < 50 && abs(eta1) > 0 && abs(eta1) < 0.9))'

