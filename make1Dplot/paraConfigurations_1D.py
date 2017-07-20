paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170720_ZLepOpenAngle/'

saveName = 'electronPtErr_DY_H_2016'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v1_20170201/',
'rootPath2': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Jan26/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'rootfile2': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 0, 0.1],
'vars1': ['pterr1/pT1', 'pterr2/pT2'],
'vars2': ['lep_pterr[lep_Hindex[0]]/lep_pt[lep_Hindex[0]]', \
          'lep_pterr[lep_Hindex[1]]/lep_pt[lep_Hindex[1]]', \
          'lep_pterr[lep_Hindex[2]]/lep_pt[lep_Hindex[2]]', \
          'lep_pterr[lep_Hindex[3]]/lep_pt[lep_Hindex[3]]'],
'cuts1': ['massZ > 60 && massZ < 120', \
          'massZ > 60 && massZ < 120'], #
'cuts2': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 ', \
          'passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 ', \
          'passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 ', \
          'passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 '], #
'weight1': ['1', '1'],
'weight2': ['1', '1', '1', '1'],
'xTitle': '#sigma_{p_{T}/p_{T}}',
'yTitle': '',
'legend1': '2016MC, DY',
'legend2': '2016MC, H',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'electronPtErr_DY_H_2015'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2015MC_kalman_v4_NOmassZCut/',
'rootPath2': '/cms/data/store/user/t2/users/mhl/',
'rootfile1': 'DYJetsToLL_M-50_kalman_v4_m2e.root',
'rootfile2': 'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIIFall15MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'Ana/passedEvents',
'binInfo': [100, 0, 0.1],
'vars1': ['pterr1/pT1', 'pterr2/pT2'],
'vars2': ['lep_pterr[lep_Hindex[0]]/lep_pt[lep_Hindex[0]]', \
          'lep_pterr[lep_Hindex[1]]/lep_pt[lep_Hindex[1]]', \
          'lep_pterr[lep_Hindex[2]]/lep_pt[lep_Hindex[2]]', \
          'lep_pterr[lep_Hindex[3]]/lep_pt[lep_Hindex[3]]'],
'cuts1': ['massZ > 60 && massZ < 120', \
          'massZ > 60 && massZ < 120'], #
'cuts2': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 ', \
          'passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 ', \
          'passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 ', \
          'passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140 '], #
'weight1': ['1', '1'],
'weight2': ['1', '1', '1', '1'],
'xTitle': '#sigma_{p_{T}/p_{T}}',
'yTitle': '',
'legend1': '2016MC, DY',
'legend2': '2016MC, H',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'm4mu_reco_refit_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'], 
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState == 1 && mass4lREFIT > 105 && mass4lREFIT < 140'], 
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'm_{4#mu}(GeV)',
'yTitle': 'Events/0.35 GeV',
'legend1': 'Reco',
'legend2': 'Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'm4e_reco_refit_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'], 
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState == 2 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'm_{4e}(GeV)',
'yTitle': 'Events/0.35 GeV',
'legend1': 'Reco',
'legend2': 'Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'm2e2mu_reco_refit_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'], 
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState > 2 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'm_{2e2#mu}(GeV)',
'yTitle': 'Events/0.35 GeV',
'legend1': 'Reco',
'legend2': 'Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'#'#1F68FA'
}



saveName = 'm4l_qqzz_reco_refit_2016MC_2e2mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'qqZZ.root',
'rootfile2': 'qqZZ.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 400],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 80 && mass4l < 400'],
'cuts2': ['passedFullSelection && finalState > 2 && mass4lREFIT > 80 && mass4lREFIT < 400'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '2e2mu, Reco',
'legend2': '2e2mu, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}



saveName = 'm4l_qqzz_reco_refit_2016MC_4mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'qqZZ.root',
'rootfile2': 'qqZZ.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 400],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 1  && mass4l > 80 && mass4l < 400'],
'cuts2': ['passedFullSelection && finalState == 1 && mass4lREFIT > 80 && mass4lREFIT < 400'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '4mu, Reco',
'legend2': '4mu, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}



saveName = 'm4l_qqzz_reco_refit_2016MC_4e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'qqZZ.root',
'rootfile2': 'qqZZ.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 80, 400],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 2  && mass4l > 80 && mass4l < 400'],
'cuts2': ['passedFullSelection && finalState == 2 && mass4lREFIT > 80 && mass4lREFIT < 400'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '4e, Reco',
'legend2': '4e, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}




saveName = 'check'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootPath2': '/raid/raid5/dsperka/Run2/HZZ4l/SubmitArea_13TeV/Ana_ZZ4L_80X/',
'rootfile1': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'rootfile2': 'Data_Run2016-03Feb2017_hzz4l_bestCandMela.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [35, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection &&  mass4l > 100 && mass4l < 1000'],
'cuts2': ['passedFullSelection &&  mass4lREFIT > 100 && mass4lREFIT < 1000'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': 'Events/10GeV',
'legend1': 'Reco',
'legend2': 'Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'm2e2mu_reco_refit_2016MC_inclusive'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState > 2 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState > 2 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '2e2mu, Reco',
'legend2': '2e2mu, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'm2e2mu_reco_refit_2016MC_fs_3'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 3 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState == 3 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '2e2mu, Reco',
'legend2': '2e2mu, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'm2e2mu_reco_refit_2016MC_fs_4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && finalState == 4 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState == 4 && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '2e2mu, Reco',
'legend2': '2e2mu, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'm2e2mu_reco_refit_2016MC_more2e2muThan2mu2e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/inputRoot/ggHSampleToMakeErrTemplate/',
'rootfile1': 'mH_125.root',
'rootfile2': 'mH_125.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && ((Event%2==0 && finalState == 4) || finalState ==3) && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && ((Event%2==0 && finalState == 4) || finalState ==3) && mass4lREFIT > 105 && mass4lREFIT < 140'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l(GeV)',
'yTitle': '',
'legend1': '2e2mu, Reco',
'legend2': '2e2mu, Refit',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'nlep_2016Data'
paraConfigs[saveName] = \
{\
'rootPath1': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_Data80X_2lskim_M17_Feb21/',
'rootPath2': '/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_Data80X_2lskim_M17_Feb21/',
'rootfile1': 'SingleDoubleMuon_Run2016-03Feb2017.root',
'rootfile2': 'SingleDoubleEG_Run2016-03Feb2017.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['nisoleptons'],
'vars2': ['nisoleptons'],
'cuts1': ['1'],
'cuts2': ['1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'nisolepton',
'yTitle': '',
'legend1': 'muon dataset',
'legend2': 'electron dataset',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'pT_Z4L_H4L_mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 100],
'vars1': ['pTL1','pTL2','pTL3','pTL4'],
'vars2': ['pTL1','pTL2','pTL3','pTL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL1) == 13',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL2) == 13',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL3) == 13',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL4) == 13'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL1) == 13',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL2) == 13',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL3) == 13',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL4) == 13'],
'weight1': ['1','1','1','1'],
'weight2': ['1','1','1','1'],
'xTitle': 'muon pT (GeV)',
'yTitle': '',
'legend1': '105 < m4l < 140',
'legend2': '70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'pT_Z4L_H4L_e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 0, 100],
'vars1': ['pTL1','pTL2','pTL3','pTL4'],
'vars2': ['pTL1','pTL2','pTL3','pTL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL1) == 11',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL2) == 11',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL3) == 11',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL4) == 11'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL1) == 11',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL2) == 11',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL3) == 11',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL4) == 11'],
'weight1': ['1','1','1','1'],
'weight2': ['1','1','1','1'],
'xTitle': 'electron pT (GeV)',
'yTitle': '',
'legend1': '105 < m4l < 140',
'legend2': '70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'eta_Z4L_H4L_mu'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -2.4, 2.4],
'vars1': ['etaL1','etaL2','etaL3','etaL4'],
'vars2': ['etaL1','etaL2','etaL3','etaL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL1) == 13 && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL2) == 13 && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL3) == 13 && finalState == 1',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL4) == 13 && finalState == 1'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL1) == 13 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL2) == 13 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL3) == 13 && finalState == 1',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL4) == 13 && finalState == 1'],
'weight1': ['1','1','1','1'],
'weight2': ['1','1','1','1'],
'xTitle': 'muon eta',
'yTitle': '',
'legend1': '105 < m4l < 140',
'legend2': '70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'eta_Z4L_H4L_e'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -2.4, 2.4],
'vars1': ['etaL1','etaL2','etaL3','etaL4'],
'vars2': ['etaL1','etaL2','etaL3','etaL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL1) == 11',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL2) == 11',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL3) == 11',\
          'passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL4) == 11'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL1) == 11',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL2) == 11',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL3) == 11',\
          'passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL4) == 11'],
'weight1': ['1','1','1','1'],
'weight2': ['1','1','1','1'],
'xTitle': 'electron eta',
'yTitle': '',
'legend1': '105 < m4l < 140',
'legend2': '70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB'
}


saveName = 'PtResidual_Z4L_H4L_mu1'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -0.1,0.1],
'vars1': ['(pTL1-pTGENL1)/pTGENL1'],
'vars2': ['(pTL1-pTGENL1)/pTGENL1'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL1) == 13 && finalState == 1'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL1) == 13 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
'yTitle': '',
'legend1': 'ggH sample, 105 < m4l < 140',
'legend2': 'ZZ4L sample, 70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'PtResidual_Z4L_H4L_mu2'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -0.1,0.1],
'vars1': ['(pTL2-pTGENL2)/pTGENL2'],
'vars2': ['(pTL2-pTGENL2)/pTGENL2'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL2) == 13 && finalState == 1'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL2) == 13 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
'yTitle': '',
'legend1': 'ggH sample, 105 < m4l < 140',
'legend2': 'ZZ4L sample, 70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'PtResidual_Z4L_H4L_mu3'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -0.1,0.1],
'vars1': ['(pTL3-pTGENL3)/pTGENL3'],
'vars2': ['(pTL3-pTGENL3)/pTGENL3'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL3) == 13 && finalState == 1'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL3) == 13 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
'yTitle': '',
'legend1': 'ggH sample, 105 < m4l < 140',
'legend2': 'ZZ4L sample, 70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'PtResidual_Z4L_H4L_mu4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC_20170223.root',
'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, -0.1,0.1],
'vars1': ['(pTL4-pTGENL4)/pTGENL4'],
'vars2': ['(pTL4-pTGENL4)/pTGENL4'],
'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && abs(idL4) == 13 && finalState == 1'],
'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && abs(idL4) == 13 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
'yTitle': '',
'legend1': 'ggH sample, 105 < m4l < 140',
'legend2': 'ZZ4L sample, 70 < m4l < 105',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName_0 = 'PtResidual_Z4L_H4L_'
etas = [0,0.9,1.8,2.4]
pts = [5,20,40,50,60,100]
#pts = [5,10,20,30,40,50,60,70,80,90,100]
for i in range(len(pts)-1):
    for j in range(len(etas)-1):
        saveName = saveName_0 + 'pT_' + str(pts[i]) + '_' + str(pts[i+1]) + '_eta_' + str(etas[j]) + '_' + str(etas[j+1])
        paraConfigs[saveName] = \
        {\
        'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
        'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
        'rootfile1': 'ggH125_2016MC_20170223.root',
        'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
        'tree1': 'passedEvents',
        'tree2': 'passedEvents',
        'binInfo': [100, -0.1,0.1],
        'vars1': ['(pTL1-pTGENL1)/pTGENL1',\
                  '(pTL2-pTGENL2)/pTGENL2',\
                  '(pTL3-pTGENL3)/pTGENL3',\
                  '(pTL4-pTGENL4)/pTGENL4'],
        'vars2': ['(pTL1-pTGENL1)/pTGENL1',\
                  '(pTL2-pTGENL2)/pTGENL2',\
                  '(pTL3-pTGENL3)/pTGENL3',\
                  '(pTL4-pTGENL4)/pTGENL4'],
        'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL1 > ' + str(pts[i]) + ' && pTGENL1 < ' + str(pts[i+1])\
                   + ' && abs(etaL1) > ' + str(etas[j]) + ' && abs(etaL1) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL2 > ' + str(pts[i]) + ' && pTGENL2 < ' + str(pts[i+1])\
                   + ' && abs(etaL2) > ' + str(etas[j]) + ' && abs(etaL2) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL3 > ' + str(pts[i]) + ' && pTGENL3 < ' + str(pts[i+1])\
                   + ' && abs(etaL3) > ' + str(etas[j]) + ' && abs(etaL3) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL4 > ' + str(pts[i]) + ' && pTGENL4 < ' + str(pts[i+1])\
                   + ' && abs(etaL4) > ' + str(etas[j]) + ' && abs(etaL4) < ' + str(etas[j+1])],
        'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL1 > ' + str(pts[i]) + ' && pTGENL1 < ' + str(pts[i+1])\
                   + ' && abs(etaL1) > ' + str(etas[j]) + ' && abs(etaL1) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL2 > ' + str(pts[i]) + ' && pTGENL2 < ' + str(pts[i+1])\
                   + ' && abs(etaL2) > ' + str(etas[j]) + ' && abs(etaL2) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL3 > ' + str(pts[i]) + ' && pTGENL3 < ' + str(pts[i+1])\
                   + ' && abs(etaL3) > ' + str(etas[j]) + ' && abs(etaL3) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL4 > ' + str(pts[i]) + ' && pTGENL4 < ' + str(pts[i+1])\
                   + ' && abs(etaL4) > ' + str(etas[j]) + ' && abs(etaL4) < ' + str(etas[j+1])],
        'weight1': ['1','1','1','1'],
        'weight2': ['1','1','1','1'],
        'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
        'yTitle': '',
        'legend1': 'ggH sample, 105 < m4l < 140',
        'legend2': 'ZZ4L sample, 70 < m4l < 105',
        'savePath': savePath,
        'saveName': saveName, #
        'latexNote1': '', #
        'latexNote2': '',
        'doFit': True,
        'pdfName': 'doubleCB',
        'color1' : '#1427D1'
        }  


saveName_0 = 'PtResidual_H4L_Z2L_'
etas = [0,0.9,1.8,2.4]
pts = [5,20,40,50,60,100]
#pts = [5,10,20,30,40,50,60,70,80,90,100]
for i in range(len(pts)-1):
    for j in range(len(etas)-1):
        saveName = saveName_0 + 'pT_' + str(pts[i]) + '_' + str(pts[i+1]) + '_eta_' + str(etas[j]) + '_' + str(etas[j+1])
        paraConfigs[saveName] = \
        {\
        'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
        'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/outputRoot/DY_2016MC_v3_20170312_afterApproval/',
        'rootfile1': 'ggH125_2016MC_20170223.root',
        'rootfile2': 'DYJetsToLL_M-50_kalman_v4_m2mu.root',
        'tree1': 'passedEvents',
        'tree2': 'passedEvents',
        'binInfo': [100, -0.1,0.1],
        'vars1': ['(pTL1-pTGENL1)/pTGENL1',\
                  '(pTL2-pTGENL2)/pTGENL2',\
                  '(pTL3-pTGENL3)/pTGENL3',\
                  '(pTL4-pTGENL4)/pTGENL4'],
        'vars2': ['(pT1-genLep_pt1)/genLep_pt1',\
                  '(pT2-genLep_pt2)/genLep_pt2'],
        'cuts1': ['passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL1 > ' + str(pts[i]) + ' && pTGENL1 < ' + str(pts[i+1])\
                   + ' && abs(etaL1) > ' + str(etas[j]) + ' && abs(etaL1) < ' + str(etas[j+1]),\
                  'passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL2 > ' + str(pts[i]) + ' && pTGENL2 < ' + str(pts[i+1])\
                   + ' && abs(etaL2) > ' + str(etas[j]) + ' && abs(etaL2) < ' + str(etas[j+1]),\
                  'passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL3 > ' + str(pts[i]) + ' && pTGENL3 < ' + str(pts[i+1])\
                   + ' && abs(etaL3) > ' + str(etas[j]) + ' && abs(etaL3) < ' + str(etas[j+1]),\
                  'passedFullSelection > 0.5 && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL4 > ' + str(pts[i]) + ' && pTGENL4 < ' + str(pts[i+1])\
                   + ' && abs(etaL4) > ' + str(etas[j]) + ' && abs(etaL4) < ' + str(etas[j+1])],
        'cuts2': ['massZ > 80 && massZ < 100 && genLep_pt1 > ' + str(pts[i]) + ' && genLep_pt1 < ' + str(pts[i+1])\
                   + ' && abs(genLep_eta1) > ' + str(etas[j]) + ' && abs(genLep_eta1) < ' + str(etas[j+1]),\
                  'massZ > 80 && massZ < 100 && genLep_pt2 > ' + str(pts[i]) + ' && genLep_pt2 < ' + str(pts[i+1])\
                   + ' && abs(genLep_eta2) > ' + str(etas[j]) + ' && abs(genLep_eta2) < ' + str(etas[j+1])],
        'weight1': ['1','1','1','1'],
        'weight2': ['1','1'],
        'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
        'yTitle': '',
        'legend1': 'ggH sample, 105 < m4l < 140',
        'legend2': 'DY sample, 80 < m4l < 100',
        'savePath': savePath,
        'saveName': saveName, #
        'latexNote1': '', #
        'latexNote2': '',
        'doFit': True,
        'pdfName': 'doubleCB',
        'color1' : '#1427D1',
        'doUnbin': False,
        'rooVars1': [['passedFullSelection',0,2], \
                   ['mass4l',105,140],\
                   ['finalState',0,5],\
                   ['pTGENL1', 0, 100],\
                   ['pTGENL2', 0, 100],\
                   ['pTGENL3', 0, 100],\
                   ['pTGENL4', 0, 100],\
                   ['etaL1', 0, 2.5],\
                   ['etaL2', 0, 2.5],\
                   ['etaL3', 0, 2.5],\
                   ['etaL4', 0, 2.5] ],
        'rooVars2': [['massZ',80,100],\
                     ['genLep_pt1', 0, 100],\
                     ['genLep_pt2', 0, 100],\
                     ['genLep_eta1', 0, 2.5],\
                     ['genLep_eta2', 0, 2.5] ]
        }




saveName_0 = 'PtResidual_Z4L_Z4Lext_'
etas = [0,2.4]#0.9,1.8,2.4]
pts = [5,100]#20,40,50,60,100]
#pts = [5,10,20,30,40,50,60,70,80,90,100]
for i in range(len(pts)-1):
    for j in range(len(etas)-1):
        saveName = saveName_0 + 'pT_' + str(pts[i]) + '_' + str(pts[i+1]) + '_eta_' + str(etas[j]) + '_' + str(etas[j+1])
        paraConfigs[saveName] = \
        {\
        'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
        'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
        'rootfile1': 'ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root',
        'rootfile2': 'ZZTo4L_13TeV_powheg_pythia8_ext1_RunIISummer16MiniAODv2.root',
        'tree1': 'passedEvents',
        'tree2': 'passedEvents',
        'binInfo': [100, -0.1,0.1],
        'vars1': ['(pTL1-pTGENL1)/pTGENL1',\
                  '(pTL2-pTGENL2)/pTGENL2',\
                  '(pTL3-pTGENL3)/pTGENL3',\
                  '(pTL4-pTGENL4)/pTGENL4'],
        'vars2': ['(pTL1-pTGENL1)/pTGENL1',\
                  '(pTL2-pTGENL2)/pTGENL2',\
                  '(pTL3-pTGENL3)/pTGENL3',\
                  '(pTL4-pTGENL4)/pTGENL4'],
        'cuts1': ['passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL1 > ' + str(pts[i]) + ' && pTGENL1 < ' + str(pts[i+1])\
                   + ' && abs(etaL1) > ' + str(etas[j]) + ' && abs(etaL1) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL2 > ' + str(pts[i]) + ' && pTGENL2 < ' + str(pts[i+1])\
                   + ' && abs(etaL2) > ' + str(etas[j]) + ' && abs(etaL2) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL3 > ' + str(pts[i]) + ' && pTGENL3 < ' + str(pts[i+1])\
                   + ' && abs(etaL3) > ' + str(etas[j]) + ' && abs(etaL3) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1 && pTGENL4 > ' + str(pts[i]) + ' && pTGENL4 < ' + str(pts[i+1])\
                   + ' && abs(etaL4) > ' + str(etas[j]) + ' && abs(etaL4) < ' + str(etas[j+1])],
        'cuts2': ['passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL1 > ' + str(pts[i]) + ' && pTGENL1 < ' + str(pts[i+1])\
                   + ' && abs(etaL1) > ' + str(etas[j]) + ' && abs(etaL1) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL2 > ' + str(pts[i]) + ' && pTGENL2 < ' + str(pts[i+1])\
                   + ' && abs(etaL2) > ' + str(etas[j]) + ' && abs(etaL2) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL3 > ' + str(pts[i]) + ' && pTGENL3 < ' + str(pts[i+1])\
                   + ' && abs(etaL3) > ' + str(etas[j]) + ' && abs(etaL3) < ' + str(etas[j+1]),\
                  'passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1 && pTGENL4 > ' + str(pts[i]) + ' && pTGENL4 < ' + str(pts[i+1])\
                   + ' && abs(etaL4) > ' + str(etas[j]) + ' && abs(etaL4) < ' + str(etas[j+1])],
        'weight1': ['1','1','1','1'],
        'weight2': ['1','1','1','1'],
        'xTitle': '(pT_{Reco}-pT_{Gen})/pT_{Gen}',
        'yTitle': '',
        'legend1': 'ZZ4L sample, 70 < m4l < 105',
        'legend2': 'ZZ4L sample(ext), 70 < m4l < 105',
        'savePath': savePath,
        'saveName': saveName, #
        'latexNote1': '', #
        'latexNote2': '',
        'doFit': True,
        'pdfName': 'doubleCB',
        'color1' : '#1427D1'
        }



saveName = 'souting_veto2Z'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'scouting20170620.root',
'rootfile2': 'scouting20170620.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [200,70,1000],
'vars1': ['mass4l'],
'vars2': ['mass4l'],
'cuts1': ['passedFullSelection && (massZ1 < 60 || massZ1 > 120) && (massZ2 < 60 || massZ2 > 120)'],
'cuts2': ['passedFullSelection && (massZ1 < 60 || massZ1 > 120) && (massZ2 < 60 || massZ2 > 120)'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': '',
'legend1': 'massZ_{1,2} > 120 or massZ_{1,2} < 60',
'legend2': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'mass4l_2016Data_300_1200'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [90,300,1200],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/10GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'mass4l_2016Data_0_300'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [150,0,300],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/2GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'mass4l_2016Data_0_100'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [90,10,100],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/1GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'mass4l_2016Data_0_70'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [70,0,70],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/1GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'mass4l_2016Data_70_100'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [30,70,100],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/1GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'mass4l_2016Data_100_400'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [60,100,400],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/5GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'mass4l_2016Data_400_1200'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [80,400,1200],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 0 && mass4l < 10000 '],
'cuts2': ['passedFullSelection && mass4lREFIT > 0 && mass4lREFIT < 10000 '],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/10GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'mass4l_closeMZ1MZ2_2016Data'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [500,0,2500],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'],
'cuts1': ['passedFullSelection && mass4l > 70 && mass4l < 2500 && abs(massZ1-massZ2) < 5 && abs(massZ1-91.2) > 2 && abs(massZ2-91.2) > 2'],
'cuts2': ['passedFullSelection && mass4lREFIT > 70 && mass4lREFIT < 2500 && abs(massZ1-massZ2) < 5 && abs(massZ1-91.2) > 2 && abs(massZ2-91.2) > 2'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/2GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'massZ2_2016Data'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [25,100,150],
'vars1': ['massZ2'],
'vars2': ['massZ2'],
'cuts1': ['passedFullSelection','passedFullSelection || passedZXCRSelection'],
'cuts2': ['passedFullSelection ','passedFullSelection || passedZXCRSelection'],
'weight1': ['1','1'],
'weight2': ['1','1'],
'xTitle': 'massZ2',
'yTitle': 'Events/2GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'massZ2_2016Data_fullRange'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'Data2016.root',
'rootfile2': 'Data2016.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [500,0,2500],
'vars1': ['massZ2'],
'vars2': ['massZ2'],
'cuts1': ['passedFullSelection || passedZXCRSelection'],
'cuts2': ['passedFullSelection || passedZXCRSelection'],
'weight1': ['1','1'],
'weight2': ['1','1'],
'xTitle': 'massZ2',
'yTitle': 'Events/2GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

saveName = 'mass4l_2016Data_all_1TeV_2TeV'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'test.root',
'rootfile2': 'test.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [50,1000,2000],
'vars1': ['mass4l'],
'vars2': ['mass4l'],
'cuts1': [' mass4l < 2000 && mass4l > 1000'],
'cuts2': [' mass4l < 2000 && mass4l > 1000'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'mass4l',
'yTitle': 'Events/20GeV',
'legend1': 'RECO,mZ2 > 4',
'legend2': 'REFIT,mZ2 > 4',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'Z1LepDeltaR_Z4L_H4L'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'ggH125_2016MC_MuPt4_Z2AT4_20170720.root',
'rootfile2': 'ZZTo4L_2016MC_MuPt4_Z2AT4_20170720.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100,0,7],
'vars1': ['Z1LepDeltaR'],
'vars2': ['Z1LepDeltaR'],
'cuts1': [' passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'cuts2': [' passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'Z1LepDeltaR',
'yTitle': 'Events',
'legend1': 'H #rightarrow 4l events',
'legend2': 'Z #rightarrow 4l events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'Z2LepDeltaR_Z4L_H4L'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'ggH125_2016MC_MuPt4_Z2AT4_20170720.root',
'rootfile2': 'ZZTo4L_2016MC_MuPt4_Z2AT4_20170720.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100,0,7],
'vars1': ['Z2LepDeltaR'],
'vars2': ['Z2LepDeltaR'],
'cuts1': [' passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'cuts2': [' passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'Z2LepDeltaR',
'yTitle': 'Events',
'legend1': 'H #rightarrow 4l events',
'legend2': 'Z #rightarrow 4l events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'Z1LepDeltaPhi_Z4L_H4L'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'ggH125_2016MC_MuPt4_Z2AT4_20170720.root',
'rootfile2': 'ZZTo4L_2016MC_MuPt4_Z2AT4_20170720.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100,-3.15,3.15],
'vars1': ['Z1LepDeltaPhi'],
'vars2': ['Z1LepDeltaPhi'],
'cuts1': [' passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'cuts2': [' passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'Z1LepDeltaPhi',
'yTitle': 'Events',
'legend1': 'H #rightarrow 4l events',
'legend2': 'Z #rightarrow 4l events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'Z2LepDeltaPhi_Z4L_H4L'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'ggH125_2016MC_MuPt4_Z2AT4_20170720.root',
'rootfile2': 'ZZTo4L_2016MC_MuPt4_Z2AT4_20170720.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100,-3.15,3.15],
'vars1': ['Z2LepDeltaPhi'],
'vars2': ['Z2LepDeltaPhi'],
'cuts1': [' passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'cuts2': [' passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'Z2LepDeltaPhi',
'yTitle': 'Events',
'legend1': 'H #rightarrow 4l events',
'legend2': 'Z #rightarrow 4l events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'Z2LepDeltaEta_Z4L_H4L'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'ggH125_2016MC_MuPt4_Z2AT4_20170720.root',
'rootfile2': 'ZZTo4L_2016MC_MuPt4_Z2AT4_20170720.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100,-5,5],
'vars1': ['Z2LepDeltaEta'],
'vars2': ['Z2LepDeltaEta'],
'cuts1': [' passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'cuts2': [' passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'Z2LepDeltaEta',
'yTitle': 'Events',
'legend1': 'H #rightarrow 4l events',
'legend2': 'Z #rightarrow 4l events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}


saveName = 'Z1LepDeltaEta_Z4L_H4L'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootPath2': '/raid/raid8/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/Ana_ZZ4L_80X/Ntuples/',
'rootfile1': 'ggH125_2016MC_MuPt4_Z2AT4_20170720.root',
'rootfile2': 'ZZTo4L_2016MC_MuPt4_Z2AT4_20170720.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100,-5,5],
'vars1': ['Z1LepDeltaEta'],
'vars2': ['Z1LepDeltaEta'],
'cuts1': [' passedFullSelection && mass4l > 105 && mass4l < 140 && finalState == 1'],
'cuts2': [' passedFullSelection && mass4l > 70 && mass4l < 105 && finalState == 1'],
'weight1': ['1'],
'weight2': ['1'],
'xTitle': 'Z1LepDeltaEta',
'yTitle': 'Events',
'legend1': 'H #rightarrow 4l events',
'legend2': 'Z #rightarrow 4l events',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': False,
'pdfName': 'doubleCB',
'color1' : '#1427D1'
}

