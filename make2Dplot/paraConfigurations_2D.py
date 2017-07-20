paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170711_scouting/'

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


saveName = 'mass4lErr_reco_refit_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootfile1': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['mass4l > 105 && mass4l < 140 && finalState==1'],
'weight1': ['1'],
'xTitle': 'm4lErr/m4l',
'yTitle': 'm4lErrREFIT/m4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}
saveName = 'mass4lErr_reco_refit_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootfile1': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['mass4l > 105 && mass4l < 140 && finalState==2'],
'weight1': ['1'],
'xTitle': 'm4lErr/m4l',
'yTitle': 'm4lErrREFIT/m4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}
saveName = 'mass4lErr_reco_refit_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootfile1': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 0.1],
'binInfo_y': [100, 0, 0.1],
'vars1_x': ['mass4lErr/mass4l'],
'vars1_y': ['mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['mass4l > 105 && mass4l < 140 && finalState>2'],
'weight1': ['1'],
'xTitle': 'm4lErr/m4l',
'yTitle': 'm4lErrREFIT/m4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}



saveName = 'massZ1_diffM4lErr_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootfile1': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 110],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['massZ1'],
'vars1_y': ['mass4lErr/mass4l-mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['mass4l > 105 && mass4l < 140 && finalState>2'],
'weight1': ['1'],
'xTitle': 'mz1',
'yTitle': 'm4lErr/m4l-m4lErrREFIT/m4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'massZ1_diffM4lErr_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootfile1': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 50, 110],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['massZ1'],
'vars1_y': ['mass4lErr/mass4l-mass4lErrREFIT/mass4lREFIT'],
'cuts1': ['mass4l > 105 && mass4l < 140 && finalState==1'],
'weight1': ['1'],
'xTitle': 'mz1',
'yTitle': 'm4lErr/m4l-m4lErrREFIT/m4lREFIT',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'diffPt_gen_reco_vs_genpT'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v3_20170312_afterApproval/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [10, -1, 1],
'vars1_x': ['genLep_pt1','genLep_pt2'],
'vars1_y': ['genLep_pt1-pT1','genLep_pt2-pT2'],
'cuts1': ['genzm > 60 && genzm < 120',\
          'genzm > 60 && genzm < 120'],
'weight1': ['1','1'],
'xTitle': 'pT_{gen}',
'yTitle': 'pT_{gen}-pT_{reco}',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'H4L_mu_eta_pt'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['etaL1','etaL2','etaL3','etaL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': 'muon eta',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'Z4L_mu_eta_pt'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['etaL1','etaL2','etaL3','etaL4'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': 'muon eta',
'savePath': savePath, 
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'ZZ4L_mu_eta_pt'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, 0, 2.4],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['etaL1','etaL2','etaL3','etaL4'],
'cuts1': ['passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': 'muon eta',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'H4L_mu_residual_pt_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL1) < 0.9',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL2) < 0.9',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL3) < 0.9',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL4) < 0.9'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'H4L_mu_residual_pt_eta_0p9_1p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL1) > 0.9 && abs(etaL1) < 1.4',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL2) > 0.9 && abs(etaL2) < 1.4',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL3) > 0.9 && abs(etaL3) < 1.4',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL4) > 0.9 && abs(etaL4) < 1.4'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'H4L_mu_residual_pt_eta_1p4_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL1) > 1.4 && abs(etaL1) < 2.4',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL2) > 1.4 && abs(etaL2) < 2.4',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL3) > 1.4 && abs(etaL3) < 2.4',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL4) > 1.4 && abs(etaL4) < 2.4'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'Z4L_mu_residual_pt_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL1) < 0.9 ',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL2) < 0.9 ',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL3) < 0.9 ',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL4) < 0.9 '],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'Z4L_mu_residual_pt_eta_0p9_1p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL1) > 0.9 && abs(etaL1) < 1.4',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL2) > 0.9 && abs(etaL2) < 1.4',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL3) > 0.9 && abs(etaL3) < 1.4',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL4) > 0.9 && abs(etaL4) < 1.4'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'Z4L_mu_residual_pt_eta_1p4_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL1) > 1.4 && abs(etaL1) < 2.4',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL2) > 1.4 && abs(etaL2) < 2.4',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL3) > 1.4 && abs(etaL3) < 2.4',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL4) > 1.4 && abs(etaL4) < 2.4'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'ZZ4L_mu_residual_pt_eta_0_0p9'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL1) < 0.9 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL2) < 0.9 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL3) < 0.9 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL4) < 0.9 '],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'ZZ4L_mu_residual_pt_eta_0p9_1p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL1) > 0.9 && abs(etaL1) < 1.4 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL2) > 0.9 && abs(etaL2) < 1.4 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL3) > 0.9 && abs(etaL3) < 1.4 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL4) > 0.9 && abs(etaL4) < 1.4 '],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'ZZ4L_mu_residual_pt_eta_1p4_2p4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 100],
'binInfo_y': [100, -0.1, 0.1],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL1) > 1.4 && abs(etaL1) < 2.4 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL2) > 1.4 && abs(etaL2) < 2.4 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL3) > 1.4 && abs(etaL3) < 2.4 ',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL4) > 1.4 && abs(etaL4) < 2.4 '],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'ZZ4L_mu_ptResidual_m4l'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 70, 250],
'binInfo_y': [100, -0.2, 0.2],
'vars1_x': ['mass4l','mass4l','mass4l','mass4l'],
'vars1_y': ['(pTL1-pTGENL1)/pTGENL1','(pTL2-pTGENL2)/pTGENL2','(pTL3-pTGENL3)/pTGENL3','(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 250 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 250 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 250 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 250 && finalState == 1'],
'weight1': ['1','1','1','1'],
'xTitle': 'm4l',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath, 
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'Z4L_mu_residual_pt_eta_test1'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [10, 5, 100],
'binInfo_y': [10, 0, 2.4],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['abs(etaL1)','abs(etaL2)','abs(etaL3)','abs(etaL4)'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL1) > 0 && abs(etaL1) < 2.4 && pTGENL1 > 5 && pTGENL1 < 100',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL2) > 0 && abs(etaL2) < 2.4 && pTGENL2 > 5 && pTGENL2 < 100',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL3) > 0 && abs(etaL3) < 2.4 && pTGENL3 > 5 && pTGENL3 < 100',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && abs(etaL4) > 0 && abs(etaL4) < 2.4 && pTGENL4 > 5 && pTGENL4 < 100'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

saveName = 'ZZ4L_mu_residual_pt_eta_test1'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'binInfo_x': [10, 0, 100],
'binInfo_y': [10, 0, 2.4],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['abs(etaL1)','abs(etaL2)','abs(etaL3)','abs(etaL4)'],
'cuts1': ['passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL1) > 0 && abs(etaL1) < 2.4 && pTGENL1 > 5 && pTGENL1 < 100',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL2) > 0 && abs(etaL2) < 2.4 && pTGENL2 > 5 && pTGENL2 < 100',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL3) > 0 && abs(etaL3) < 2.4 && pTGENL3 > 5 && pTGENL3 < 100',\
          'passedFullSelection && massZ1 > 80 && massZ1 < 100 && massZ2 > 80 && massZ2 < 100 && finalState == 1 && abs(etaL4) > 0 && abs(etaL4) < 2.4 && pTGENL4 > 5 && pTGENL4 < 100'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'H4L_mu_residual_pt_eta_test1'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'tree1': 'passedEvents',
'binInfo_x': [10, 0, 100],
'binInfo_y': [10, 0, 2.4],
'vars1_x': ['pTL1','pTL2','pTL3','pTL4'],
'vars1_y': ['abs(etaL1)','abs(etaL2)','abs(etaL3)','abs(etaL4)'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL1) > 0 && abs(etaL1) < 2.4 && pTGENL1 > 5 && pTGENL1 < 100',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL2) > 0 && abs(etaL2) < 2.4 && pTGENL2 > 5 && pTGENL2 < 100',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL3) > 0 && abs(etaL3) < 2.4 && pTGENL3 > 5 && pTGENL3 < 100',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && abs(etaL4) > 0 && abs(etaL4) < 2.4 && pTGENL4 > 5 && pTGENL4 < 100'],
'weight1': ['1','1','1','1'],
'xTitle': 'muon pT',
'yTitle': '(pTRECO-pTGEN)/pTGEN',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}



saveName = 'mass4l_massZ2_2016Data'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'tree1': 'passedEvents',
'binInfo_x': [100, 0, 500],
'binInfo_y': [50, 100, 150],
'vars1_x': ['mass4l'],
'vars1_y': ['massZ2'],
'cuts1': ['passedFullSelection'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': 'massZ2',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}


saveName = 'mass4l_massZ_closeMZ1MZ2_2016Data'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'tree1': 'passedEvents',
'binInfo_x': [500, 0, 2500],
'binInfo_y': [500, 0, 2500],
'vars1_x': ['mass4l'],
'vars1_y': ['massZ2'],
'cuts1': ['passedFullSelection && abs(massZ1-massZ2) < 5 && abs(massZ1-91.2) > 2 && abs(massZ2-91.2) > 2'],
'weight1': ['1'],
'xTitle': 'mass4l',
'yTitle': 'massZ2',
'savePath': savePath,
'saveName': saveName, #
'doLogZ': False,
'latexNote1': ' '
}

