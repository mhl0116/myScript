paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170213_refineECorr/'

saveName = 'DY_MC2016_e_eta1_eta2_ifMassZErr_2_3'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v1_20170201/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['abs(eta1)'],
'vars1_y': ['abs(eta2)'],
'cuts1': ['massZ > 60 && massZ < 120 && massZErr > 2 && massZErr < 3', \
          'massZ > 60 && massZ < 120 && massZErr > 2 && massZErr < 3'], #
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'H_MC2016_e_eta1_eta2_ifMassHErr_2_2p5'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Jan26/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['lep_eta[lep_Hindex[0]]'],
'vars1_y': ['lep_eta[lep_Hindex[1]]'],
'cuts1': ['mass4l > 105 && mass4l < 140 && mass4lErr > 2 && mass4lErr < 2.5', \
          'mass4l > 105 && mass4l < 140 && mass4lErr > 2 && mass4lErr < 2.5'], #
'weight1': ['1'],
'xTitle': 'eta1',
'yTitle': 'eta2',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'H_MC2016_e_eta3_eta4_ifMassHErr_2_2p5'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Jan26/',
'rootfile1': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'Ana/passedEvents',
'binInfo_x': [100, 0, 2.5],
'binInfo_y': [100, 0, 2.5],
'vars1_x': ['lep_eta[lep_Hindex[2]]'],
'vars1_y': ['lep_eta[lep_Hindex[3]]'],
'cuts1': ['mass4l > 105 && mass4l < 140 && mass4lErr > 2 && mass4lErr < 2.5', \
          'mass4l > 105 && mass4l < 140 && mass4lErr > 2 && mass4lErr < 2.5'], #
'weight1': ['1'],
'xTitle': 'eta3',
'yTitle': 'eta4',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'DY_2016_relpTErr_eta_ecalDriven_e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v1_20170213/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'tree1': 'passedEvents',
'binInfo_x': [100, -2.5, 2.5],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['genLep_eta1', 'genLep_eta2'],
'vars1_y': ['pterr1/genLep_pt1', 'pterr2/genLep_pt2'],
'cuts1': ['genzm > 80 && genzm < 100 && genLep_pt1 > 7 && genLep_pt1 < 100 && massZ > 80 && massZ < 100 && lep1_ecalDriven ', \
          'genzm > 80 && genzm < 100 && genLep_pt2 > 7 && genLep_pt2 < 100 && massZ > 80 && massZ < 100 && lep2_ecalDriven '], #
'weight1': ['1', '1'],
'xTitle': 'eta',
'yTitle': 'ptErr/genPt',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

