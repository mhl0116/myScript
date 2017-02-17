paraConfigs = { }

savePath = '/home/mhl/public_html/2017/20170206_m4l_reco_refit/'

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
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC.root',
'rootfile2': 'ggH125_2016MC.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'], 
'cuts1': ['passedFullSelection && finalState == 1 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState == 1 && mass4lREFIT > 105 && mass4lREFIT < 140'], 
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
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'm4e_reco_refit_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC.root',
'rootfile2': 'ggH125_2016MC.root',
'tree1': 'passedEvents',
'tree2': 'passedEvents',
'binInfo': [100, 105, 140],
'vars1': ['mass4l'],
'vars2': ['mass4lREFIT'], 
'cuts1': ['passedFullSelection && finalState == 2 && mass4l > 105 && mass4l < 140'],
'cuts2': ['passedFullSelection && finalState == 2 && mass4lREFIT > 105 && mass4lREFIT < 140'],
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
'doFit': True,
'pdfName': 'doubleCB'
}


saveName = 'm2e2mu_reco_refit_2016MC'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootPath2': '/raid/raid9/mhl/HZZ4L_Run2_post2016ICHEP/HiggsMass_HZZ4L/packages/liteUFHZZ4LAnalyzer/Ntuples/',
'rootfile1': 'ggH125_2016MC.root',
'rootfile2': 'ggH125_2016MC.root',
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

